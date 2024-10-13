CREATE DATABASE LaxStore;
USE LaxStore;

-- Tailor Made For The Customers/clients

CREATE TABLE Registration (
    Username VARCHAR(30) UNIQUE,
    First_Names CHAR(50),
    Surname CHAR(40),
    Full_Name CHAR(100),
    Email_Address VARCHAR(50),
    Phone_Number VARCHAR(10),
    Alternate_Number VARCHAR(10),
    Location VARCHAR(150),
    Password VARCHAR(255), -- Increased length for hashed passwords
    Profile_Photo VARCHAR(255), -- Added data type
    Date_of_registration DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Sign_In (
    Username VARCHAR(30) UNIQUE,
    Email_Address VARCHAR(50),
    Password VARCHAR(255) -- Increased length for hashed passwords
);

CREATE TABLE Financials (
    Username VARCHAR(30),
    Group_By CHAR(8),
    Item_Type CHAR(15),
    Item_Name VARCHAR(100),
    Product_Name VARCHAR(100),
    Size_Selected VARCHAR(10),
    Number_of_Items INT,
    Item_Price DECIMAL(5, 2),
    Product_Price DECIMAL(6, 2),
    Subtotal DECIMAL(6, 2),
    Current_Tax DECIMAL(2, 2),
    VAT_Amount DECIMAL(5, 2),
    Final_Amount DECIMAL(6, 2),
    Amount_Paid DECIMAL(6, 2),
    Change_Returned DECIMAL(5, 2), -- Added data type
    Date_of_purchase DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE History (
    Receipt_ID INT,
    Username VARCHAR(30),
    First_Names CHAR(50),
    Surname CHAR(40),
    Full_Name CHAR(100),
    Email_Address VARCHAR(50),
    Phone_Number VARCHAR(10),
    Alternate_Number VARCHAR(10),
    Location VARCHAR(150),
    Name_Of_The_Brand VARCHAR(100),
    Group_By CHAR(8),
    Item_Type CHAR(15),
    Item_Name VARCHAR(100),
    Product_Name VARCHAR(100),
    Number_of_Items INT,
    Size_Selected VARCHAR(10),
    Item_Price DECIMAL(5, 2),
    Product_Price DECIMAL(6, 2),
    Subtotal DECIMAL(6, 2),
    Current_Tax DECIMAL(2, 2),
    VAT_Amount DECIMAL(5, 2),
    Discount_Percent DECIMAL(3, 2),
    Final_Amount DECIMAL(6, 2),
    Amount_Paid DECIMAL(6, 2),
    Change_Returned DECIMAL(5, 2), -- Added data type
    Date_of_purchase DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Tailor Made For the Sellers

CREATE TABLE Brands (
    Name_Of_The_Brand VARCHAR(100),
    Contact_Number VARCHAR(15),
    Brand_Email_Address VARCHAR(50),
    Address VARCHAR(150),
    Date_Joined DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Social_links (
    Name_Of_The_Brand VARCHAR(100),
    Facebook VARCHAR(250),
    Instagram VARCHAR(250),
    X VARCHAR(250),
    YouTube VARCHAR(250),
    TikTok VARCHAR(250),
    Website VARCHAR(250)
);

CREATE TABLE Products_Available (
    Name_Of_The_Brand VARCHAR(100),
    Group_By CHAR(8),
    Item_Type CHAR(15),
    Item_Name VARCHAR(100),
    Product_Name VARCHAR(100),
    Item_Price DECIMAL(5, 2),
    Product_Price DECIMAL(6, 2),
    Product_Info VARCHAR(100),
    Product_Size VARCHAR(50), -- Added data type
    Item_Media VARCHAR(255), -- Added data type
    Product_Media VARCHAR(255), -- Added data type
    Date_Posted DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Discounts (
    Name_Of_The_Brand VARCHAR(100),
    Group_By CHAR(8),
    Item_Type CHAR(15),
    Item_Name VARCHAR(100),
    Product_Name VARCHAR(100),
    Item_Price DECIMAL(5, 2),
    Product_Price DECIMAL(6, 2),
    Discount_Percent DECIMAL(3, 2),
    Discount_EXP_Date DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Banking_Details (
    Name_Of_The_Brand VARCHAR(100),
    Bank_Name CHAR(30),
    Account_Type CHAR(30),
    Account_Number INT,
    Branch_Name CHAR(30),
    Branch_Code INT
);

-- Tailor Made For All Users

CREATE TABLE Auto_Message (
    Email_Address VARCHAR(50),
    Brand_Email_Address VARCHAR(50),
    Registration CHAR(250),
    Registration_Error CHAR(100),
    Login_Error CHAR(100),
    Insufficient_Funds VARCHAR(200),
    Successful_Purchase VARCHAR(250),
    Electronic_Receipt VARCHAR(3000),
    Promotion_Message VARCHAR(3000)
);

CREATE TABLE Media (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(30),
    file_path VARCHAR(255),
    upload_date DATETIME DEFAULT CURRENT_TIMESTAMP
);


-- INSERT ROWS ON A TABLE

INSERT INTO Brands
VALUES ("Swear Ex", "0159625106", "swearex@gmail.com", "Johannesburg Gauteng ZA", NOW()),
		("Fake People", "0113246787", "fakepeople@gmail.com", "North West ZA", NOW()),
		("Exactly Clothing", "0792345478", "exactly@gmail.com", "Pretoria, Gauteng ZA", NOW());


