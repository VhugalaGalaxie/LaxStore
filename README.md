# LaxStore

**Developer:** Vhugala Mutshembele (Solo Developer)  
**Project Name:** LaxStore  
**Technologies:** Python, Flask, HTML5, CSS, JavaScript, SQL (for database management), APIs (for ID validation and insurance data integration)  
**Security:** Enhanced with bcrypt for strong password hashing and additional security measures to protect user data.  
**Status:** Ongoing

---

## Description

LaxStore is a vibrant and dynamic online platform dedicated to streetwear enthusiasts. Our website is designed to be a hotspot for all streetwear brands, offering a diverse and colorful shopping experience.

### Streetwear at its finest

**Mission:** LaxStore aims to be the go-to destination for streetwear lovers, offering a curated selection of the latest and greatest brands. We strive to provide a secure, user-friendly, and visually appealing shopping experience that celebrates the spirit of streetwear fashion.

---

## Features

- User Registration and Authentication
- Product Filtering
- Shopping Cart Management
- Checkout and Payment Processing
- Automated Email Receipts
- User Purchase History

---

## Installation

### Prerequisites

Make sure you have Python and pip installed on your machine.

### Packages to Install

Run the following command to install the necessary packages:

```bash
pip install Flask
pip install Flask-SQLAlchemy
pip install Flask-Mail
pip install bcrypt
pip install python-dotenv
pip install mysql-connector-python
pip install Flask-WTF
pip install Flask-Testing
pip install pytest
pip install Flask-CORS
pip install Flask-Login
```
<b>AND/OR</b>
```
pip install Flask Flask-SQLAlchemy Flask-Mail bcrypt python-dotenv mysql-connector-python Flask-WTF Flask-Testing pytest Flask-CORS Flask-Login
```
---
## Clone the Repository
```
git clone <repository-url>
cd LaxStore
```
---
## Setup the Database
* Create a MySQL database named LaxStore.
* Run the SQL script lax_tab.sql to create the necessary tables.

---
# Database(MySQL)

### Install MySQL on Linux
<br>
<b>Steps to Install MySQL on Linux</b>

* Step 1: Open the terminal and paste the following code:

```
sudo apt install mysql-server
```
Then insert your own password & press Enter
* Step 2: Press “y” to continue.
* Step 3: Verify the installation
```
mysql --version
```
* Step 4: set the VALIDATE PASSWORD component.
```
sudo mysql_secure_installation
```
* Step 5: Then press “y” to set the password. Next press “0” for the low-level password or choose as you want to set the password.
* Step 6: Set up or create a password
<br>
<b> _Now the whole setup is done. Hence, MySQL installation is successfully done!_ </b>

### Start Database
```
sudo mysql -u root
```
create database (commands)
```
Command 1: create database LaxStore;
Command 2: show databases;
```
---


## Running the Application
Set Environment Variables: If you are using a .env file, ensure it contains your database credentials and other necessary configuration.

### Run the Application: Start the Flask server by running:
```
python lax_access.py
```

Access the Application: Open your web browser and navigate to http://127.0.0.1:5000 to access LaxStore.

---
# Contact
For inquiries, feel free to reach out to Vhugala Mutshembele at vhugalagabriel@gmail.com.


### Notes:
- Replace `<repository-url>` with the actual URL of your repository if you're using a version control system.

---
# Contributing
As a solo developer, contributions are currently not accepted. However, feedback and suggestions are always welcome!

