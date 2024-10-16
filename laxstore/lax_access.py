import random
import string
import re
from datetime import datetime

import cursor
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import os
import bcrypt
import hashlib  # For password hashing
import mysql.connector
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Load environment variables from a .env file (ensure you've set up .env with SENDGRID_API_KEY)
load_dotenv()

app = Flask(__name__)
app.secret_key = "laxStore_secret_key_here"  # Replace with a random string

db = mysql.connector.connect(
    host="127.0.0.1",  # This is the IP address of MySQL server
    user="localhost",  # MySQL username
    password="#@VHUgal357.",  # MySQL password
    database="LaxStore"  # The name of the database
)


@app.route('/')
def index():
    return "Hello, LaxStore!"


if __name__ == '__main__':
    app.run(debug=True)


# Register a user
class UserRegistration:

    def __init__(self):
        self.cursor = db.cursor()
        self.first_name = ""
        self.surname = ""
        self.name = ""
        self.email_address = ""
        self.phone_number = ""
        self.alt_number = ""
        self.location = ""
        self.username = ""
        self.password = bytes
        self.image = ""

    def set_name(self):
        self.name = self.first_name + " " + self.surname

    # validating email address formation using regex
    def validate_email_address(self):
        email = self.email_address.strip()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not re.fullmatch(regex, email):
            print("Invalid email address format.")
            return False
        cursor.execute("SELECT * FROM users WHERE email = %s", (self.email_address,))
        if cursor.fetchone():
            print("Email already exists.")
            return False
        return True

    # Validate Password Strength (length, complexity)
    def validate_password(self):
        password = self.password.strip()
        if len(password) < 8 or not any(c.isalnum() for c in password) or not any(c in '@#$%^&*' for c in password):
            print("Password should be at least 8 characters long and contain alphanumeric and special characters.")
            return False
        return True

    # Encrypting the password using bcrypt
    def hash_password(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, user_password):
        return bcrypt.checkpw(user_password.encode('utf-8'), self.password)

    # Validate if username is unique (placeholder for actual implementation)
    def validate_username_unique(self):
        cursor.execute("SELECT * FROM users WHERE username = %s", (self.username,))
        result = cursor.fetchone()
        if result:
            print("Username already exists.")
            return False
        return True

    # Uploading Profile Photo/Image (placeholder for actual implementation)
    def upload_photo(self, file):
        # Implement actual photo upload logic here
        pass

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'uploads/'
    app.secret_key = 'your_secret_key'

    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # Save the file path to the database
            save_file_path_to_db(filename)
            return redirect(url_for('uploaded_file', filename=filename))
        return redirect(url_for('index'))

    def save_file_path_to_db(filename):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        cursor.execute("INSERT INTO your_table (file_path) VALUES (%s)", (file_path,))
        db.commit()

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return f'The file {filename} has been uploaded successfully.'

    if __name__ == '__main__':
        app.run(debug=True)

    # Function to send welcome email using SendGrid
    def send_welcome_email(email, name):
        message = Mail(
            from_email='your-email@example.com',  # Your verified SendGrid email address
            to_emails=email,
            subject='Welcome to LaxStore!',
            html_content=f"<p>Dear {name},</p>"
                         f"<p>Thank you for registering with LaxStore! We are delighted to have you on board."
                         f"</p><p>Best Regards,<br>LaxStore Team</p>"
        )
        try:
            sg = SendGridAPIClient(
                os.getenv('SENDGRID_API_KEY'))  # Fetch the SendGrid API Key from environment variable
            response = sg.send(message)
            print(f"Email sent. Status code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")

    # Route for the index page
    @app.route('/')
    def index():
        return render_template('access.html')

    # Route for user registration
    @app.route('/register', methods=['POST'])
    def register():
        # Retrieve form data
        first_name = request.form.get('first_name')
        surname = request.form.get('surname')
        email = request.form.get('email')
        password = request.form.get('password')

        # Ensure the data is valid (you can add more validation)
        if not first_name or not email or not password:
            flash('All fields are required!')
            return redirect(url_for('index'))

        # Create a UserRegistration instance and set user details
        user = UserRegistration()
        user.first_name = first_name
        user.surname = surname
        user.email_address = email
        user.password = password.encode('utf-8')

        # Validate email and password, then hash the password
        if not user.validate_email_address():
            flash("Invalid email format.")
            return redirect(url_for('index'))

        if not user.validate_password():
            flash("Weak password.")
            return redirect(url_for('index'))

        user.hash_password()

        # Check if the username or email already exists
        if not user.validate_username_unique():
            flash("Username or email already exists.")
            return redirect(url_for('index'))

        # Insert user data into the database
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO users (first_name, surname, email, password) VALUES (%s, %s, %s, %s)",
            (user.first_name, user.surname, user.email_address, user.password)
        )
        db.commit()

        # Send welcome email via SendGrid
        send_welcome_email(user.email_address, user.first_name)

        # Flash success message
        flash('Registration successful! A welcome email has been sent.')
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run(debug=True)

    def register_user(self, username, first_name, surname, email, phone_number, alt_number, location, password):
        # Hash the password for security
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            # Insert into the Registration table
            self.cursor.execute("""
                INSERT INTO Registration (Username, First_Names, Surname, Full_Name, Email_Address, 
                                          Phone_Number, Alternate_Number, Location, Password, 
                                          Date_of_registration)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
            """, (username, first_name, surname, f"{first_name} {surname}", email,
                  phone_number, alt_number, location, hashed_password))

            # Insert into the Sign_In table
            self.cursor.execute("""
                INSERT INTO Sign_In (Username, Email_Address, Password)
                VALUES (%s, %s, %s)
            """, (username, email, hashed_password))

            db.commit()  # Commit the transaction
            print("Registration successful!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            db.rollback()  # Rollback in case of error
        finally:
            self.cursor.close()


# User Login
class UserLogin:
    def __init__(self):
        self.cursor = db.cursor()

    def login_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        try:
            # Check the user's credentials
            self.cursor.execute("""
                SELECT * FROM Sign_In WHERE Username = %s AND Password = %s
            """, (username, hashed_password))
            user = self.cursor.fetchone()

            if user:
                print("Login successful!")
                return True
            else:
                print("Invalid username or password.")
                return False
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            self.cursor.close()


class UploadPhoto:
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    UPLOAD_FOLDER = 'uploads'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    @staticmethod
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in UploadPhoto.ALLOWED_EXTENSIONS

    @app.route('/')
    def index():
        return render_template('access.html')

    @app.route('/upload', methods=['POST'])
    def upload_file():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and UploadPhoto.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
        return redirect(url_for('index'))

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return f'The file {filename} has been uploaded successfully.'

    if __name__ == '__main__':
        app.run(debug=True)


# Welcoming Message
class ConfirmAndWelcome:
    @staticmethod
    def generate_confirmation_message(name):
        confirmation_message = f"Dear {name}, \n\n" \
                               "Thank you for registering with LaxStore!\n" \
                               "We are delighted to have you on board.\n" \
                               "FOR ANY QUERY\n" \
                               "Please feel free to contact us."
        return confirmation_message


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@localhost/LaxStore'  # Set your database URI
app.secret_key = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize SQLAlchemy with the Flask app


class User(db.Model):
    """Model representing a user in the registration table."""
    username = db.Column(db.String(30), unique=True, primary_key=True)  # Unique username
    first_name = db.Column(db.String(50))  # User's first name
    surname = db.Column(db.String(40))  # User's surname
    email = db.Column(db.String(50))  # User's email address
    phone_number = db.Column(db.String(10))  # User's phone number
    alternate_number = db.Column(db.String(10))  # Optional alternate number
    location = db.Column(db.String(150))  # User's address
    password = db.Column(db.String(255))  # User's hashed password

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/register', methods=['POST'])
def register():
    """Handles user registration form submission."""
    username = request.form['username']  # Get the username from the form
    password = generate_password_hash(request.form['password'])  # Hash the password for security
    first_name = request.form['first_name']  # Get the user's first name
    surname = request.form['surname']  # Get the user's surname
    email = request.form['email']  # Get the user's email address
    phone_number = request.form['phone_number']  # Get the user's phone number
    alternate_number = request.form['alternate_number']  # Get the user's alternate number
    location = request.form['location']  # Get the user's address

    new_user = User(username=username, first_name=first_name, surname=surname,
                    email=email, phone_number=phone_number,
                    alternate_number=alternate_number, location=location, password=password)
    db.session.add(new_user)  # Add the new user to the session
    db.session.commit()  # Commit the changes to the database
    flash('Registration successful! You can now log in.')  # Notify the user
    return redirect('/login')  # Redirect to the login page


@app.route('/login', methods=['POST'])
def login():
    """Handles user login form submission."""
    username = request.form['username']  # Get the username from the form
    password = request.form['password']  # Get the password from the form
    user = User.query.filter_by(username=username).first()  # Find the user by username

    if user and check_password_hash(user.password, password):  # Validate the password
        flash('Login successful!')  # Notify the user
        return redirect('/home')  # Redirect to the home page
    else:
        flash('Invalid username or password.')  # Notify the user of failure
        return redirect('/login')  # Redirect back to the login page

