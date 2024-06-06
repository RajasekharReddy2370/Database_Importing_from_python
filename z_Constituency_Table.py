# import os
# import pandas as pd
# import mysql.connector
#
# conn = mysql.connector.connect(
#     host='localhost',
#     database='Voter_Raw_Data',
#     user='root',
#     password='Raj@2370'
# )
# cur = conn.cursor()
#
# # Function to create the table
# def create_table():
#     cur.execute('''CREATE TABLE IF NOT EXISTS constituencies
#                  (Constituency_number INTEGER, Constituency_Name TEXT, State TEXT)''')
#     conn.commit()
#
# # Function to insert values from Excel files
# def insert_values_from_excel(folder_path):
#     excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
#     for file in excel_files:
#         print(file)
#         constituency_number = int(file.split('-')[0])
#         constituency_name = file.split("-")[1].split(".")[0].replace(" ", "_").title()
#         state = "TELANGANA"
#         df = pd.read_excel(os.path.join(folder_path, file))
#         cur.execute("INSERT INTO constituencies VALUES (%s, %s, %s)", (constituency_number, constituency_name, state))
#         conn.commit()
#
# # Path to the folder containing Excel files
# folder_path = "C:\\Users\\jaswa\\Desktop\\TS\\TRD"
#
# # Create the table
# create_table()
#
# # Insert values from Excel files
# insert_values_from_excel(folder_path)
#
# # Close the connection
# cur.close()
# conn.close()

################################### IF TAble is already present in the Database ########################################


# import os
# import pandas as pd
# import mysql.connector
#
# conn = mysql.connector.connect(
#     host='localhost',
#     database='Voter_Raw_Data',
#     user='root',
#     password='Raj@2370'
# )
# cur = conn.cursor()
#
# # Function to insert values from Excel files
# def insert_values_from_excel(folder_path):
#     excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]
#     for file in excel_files:
#         print(file)
#         constituency_number = int(file.split('-')[0])
#         constituency_name = file.split("-")[1].split(".")[0].replace(" ", "_").title()
#         state = "AndhraPradesh"
#         df = pd.read_excel(os.path.join(folder_path, file))
#         cur.execute("INSERT INTO constituencies (Constituency_number, Constituency_Name, State) VALUES (%s, %s, %s)", (constituency_number, constituency_name, state))
#         conn.commit()
#
# # Path to the folder containing Excel files
# folder_path = "C:\\Users\\jaswa\\Desktop\\AP\\Andhra Pradesh_RAW_DATA_Excel_Files"
#
# # Insert values from Excel files
# insert_values_from_excel(folder_path)
#
# # Close the connection
# cur.close()
# conn.close()

########################### ADDING of New column and Values ###########################################
import mysql.connector

# Connect to your MySQL database
conn = mysql.connector.connect(
    host='localhost',
    database='voter_raw_data',
    user='root',
    password='Raj@2370'
)
cur = conn.cursor()

# Step 1: Add a new column to the table
alter_query = "ALTER TABLE constituencies ADD COLUMN ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL"
cur.execute(alter_query)
# Move to the next result set
cur.nextset()
# Close and reopen the cursor
cur.close()
cur = conn.cursor()

# Step 2: Update the new column with values
update_query = "SET @id := 0; UPDATE constituencies SET ID = (@id := @id + 1)"
cur.execute(update_query)
# Move to the next result set
cur.nextset()

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()


