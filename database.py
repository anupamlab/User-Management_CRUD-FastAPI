import mysql.connector
import os
from dotenv import load_dotenv

#------------------------------------------------
# Load environment variables
load_dotenv()

# Get DB details from .env file
DB_HOST = os.getenv("HOST")
DB_USER = os.getenv("USER")
DB_PASSWORD = os.getenv("PASSWORD")
DB_NAME = os.getenv("DATABASE")

#------------------------------------------------

# Create DB connection
db = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

# Cursor to run SQL
cursor = db.cursor()







import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anupam@25",
    database="testdb"
)

# Create cursor to run SQL queries
cursor = db.cursor()