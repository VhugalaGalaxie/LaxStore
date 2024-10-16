import os

from flask import render_template
from mysql.connector import cursor
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import mysql.connector
from dotenv import load_dotenv
import lax_access

# Load environment variables from a .env file
load_dotenv()

# Database connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root@321edf558fef",
    password="#@VHUgal357.",
    database="LaxStore"
)

class CalcuMan:
    def __init__(self):
        # Financial Manipulation
        self.product_prices = []  # List to store prices of selected products
        self.subtotal = 0.0
        self.total = 0.0
        self.TAX = 0.18  # VAT is set to 18%
        self.VAT_amount = 0.0
        self.final_amount = 0.0
        self.paid_amount = 0.0
        self.change = 0.0
        self.no_of_items = 0

    def add_product(self, price):
        """Add a product price to the list and update calculations."""
        self.product_prices.append(price)
        self.no_of_items += 1
        self.calculate_totals()

    def calculate_totals(self):
        """Calculate subtotal, VAT, and final amount."""
        self.subtotal = sum(self.product_prices)
        self.VAT_amount = self.subtotal * self.TAX
        self.final_amount = self.subtotal + self.VAT_amount

    def make_payment(self, amount_paid):
        """Process the payment and calculate change."""
        self.paid_amount = amount_paid
        self.change = self.paid_amount - self.final_amount

    def get_summary(self):
        """Return a summary of the financial details."""
        return {
            "subtotal": self.subtotal,
            "VAT_amount": self.VAT_amount,
            "final_amount": self.final_amount,
            "paid_amount": self.paid_amount,
            "change": self.change,
            "no_of_items": self.no_of_items
        }

    def send_receipt(self, username):
        """Send a purchase receipt to the user's email."""
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT Email_Address FROM Registration WHERE Username = %s", (username,))
        user = cursor.fetchone()

        if not user:
            print("User not found.")
            return

        email = user['Email_Address']
        receipt_details = self.get_summary()
        items_list = '\n'.join([f"Item {i + 1}: R{price:.2f}" for i, price in enumerate(self.product_prices)])

        # Construct the receipt email
        message = Mail(
            from_email='your-email@example.com',  # Your verified SendGrid email address
            to_emails=email,
            subject='Your Purchase Receipt from LaxStore',
            html_content=f"""
            <p>Dear {username},</p>
            <p>Thank you for your purchase!</p>
            <h3>Receipt Details:</h3>
            <p>Items Purchased:</p>
            <pre>{items_list}</pre>
            <p>Subtotal: R{receipt_details['subtotal']:.2f}</p>
            <p>VAT (18%): R{receipt_details['VAT_amount']:.2f}</p>
            <p>Total: R{receipt_details['final_amount']:.2f}</p>
            <p>Amount Paid: R{receipt_details['paid_amount']:.2f}</p>
            <p>Change Returned: R{receipt_details['change']:.2f}</p>
            <p>Thank you for shopping with us!</p>
            <p>Best Regards,<br>LaxStore Team</p>
            """
        )

        # Send the email
        try:
            sg = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))  # Fetch the SendGrid API Key from environment variable
            response = sg.send(message)
            print(f"Receipt sent. Status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send receipt: {str(e)}")

        try:
            # Store receipt in the History table
            cursor.execute("""
                INSERT INTO History (Username, First_Names, Surname, Full_Name, Email_Address, 
                                     Phone_Number, Alternate_Number, Location, 
                                     Name_Of_The_Brand, Group_By, Item_Type, 
                                     Item_Name, Product_Name, Number_of_Items, 
                                     Size_Selected, Item_Price, Product_Price, 
                                     Subtotal, Current_Tax, VAT_Amount, 
                                     Final_Amount, Amount_Paid, Change_Returned, 
                                     Date_of_purchase)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, %s, 
                        %s, %s, %s, %s, %s, %s, %s, NOW())
            """, (
                username, first_name, surname, f"{first_name} {surname}", email,
                Phone_Number, Alternate_Number, Location, Name_Of_The_Brand,
                '--', '--', '--',  # Group_By, Item_Type, etc.
                '', '', self.no_of_items, '',  # Item_Name, Product_Name, Number_of_Items
                '',  # Size_Selected
                self.subtotal / self.no_of_items if self.no_of_items else 0,  # Item_Price
                self.final_amount,  # Product_Price (this might be adjusted)
                receipt_details['subtotal'],  # Subtotal
                self.TAX,  # Current_Tax
                receipt_details['VAT_amount'],  # VAT_Amount
                receipt_details['final_amount'],  # Final_Amount
                receipt_details['paid_amount'],  # Amount_Paid
                receipt_details['change'],  # Change_Returned
            ))

            db.commit()  # Commit the transaction
            print("Receipt stored in the History table.")

        except Exception as e:
            print(f"Failed to send receipt or store in history: {str(e)}")

        finally:
            cursor.close()

