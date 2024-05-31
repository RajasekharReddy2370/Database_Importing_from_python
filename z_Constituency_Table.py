import os
import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    database='Voter_Raw_Data',
    user='root',
    password='Raj@2370'
)
cur = conn.cursor()

# Function to create the table
def create_table():
    cur.execute('''CREATE TABLE IF NOT EXISTS constituencies
                 (Constituency_number INTEGER, Constituency_Name TEXT, State TEXT)''')
    conn.commit()

# Function to insert values from Excel files
def insert_values_from_excel(folder_path):
    excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
    for file in excel_files:
        print(file)
        constituency_number = int(file.split('-')[0])
        constituency_name = file.split("-")[1].split(".")[0].replace(" ", "_").title()
        state = "TELANGANA"
        df = pd.read_excel(os.path.join(folder_path, file))
        cur.execute("INSERT INTO constituencies VALUES (%s, %s, %s)", (constituency_number, constituency_name, state))
        conn.commit()

# Path to the folder containing Excel files
folder_path = "C:\\Users\\jaswa\\Desktop\\TS\\TRD"

# Create the table
create_table()

# Insert values from Excel files
insert_values_from_excel(folder_path)

# Close the connection
cur.close()
conn.close()
