import os
import psycopg2
import csv
from dotenv import load_dotenv
from datetime import date

# Load environment variables from .env file
load_dotenv()

# Retrieve database connection details from environment variables
host = os.environ.get('DB_HOST')
database = os.environ.get('DB_DATABASE')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')

# CSV file path
B200_date = date.today()
csv_file_path = f"B200_Weekly/{B200_date}.csv"

# Connect to the database
conn = psycopg2.connect(host=host, database=database, user=user, password=password)
cursor = conn.cursor()

print("Connection successful")

# Create a table to hold the CSV data
table_name = 'song'

# Open the CSV file
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)  

    # Insert data from the CSV file into the table
    insert_query = """
        INSERT INTO song (position, title, authors, last_week_position, peak_position, num_weeks_on_chart, chart_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """.format(table_name)
    cursor.executemany(insert_query, reader)
    conn.commit()

# Close the database connection
cursor.close()
conn.close()