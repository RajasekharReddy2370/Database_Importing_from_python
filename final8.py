import os
import mysql.connector
import pandas as pd
import time

start_time = time.time()
# Establish MySQL connection
conn = mysql.connector.connect(
    host='localhost',
    database='Voter_raw_data',
    user='root',
    password='Raj@2370'
)
cur = conn.cursor()

cur.execute("SELECT MAX(ID) FROM data")
last_id = cur.fetchone()[0]
print(last_id)
if last_id is None:
    last_id = 0

# Get list of Excel files in folder
folder_path = r"C:\Users\jaswa\Desktop\AP\Andhra Pradesh_Raw_Data_Folders\Vizainagaram"
excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# Read the first Excel file to define table columns
first_excel_file = excel_files[0]
first_df = pd.read_excel(os.path.join(folder_path, first_excel_file))
# first_df["ID"] = ''
# first_df["State"] = ''

# first_df.insert(0, 'ID', 0)
# first_df.insert(1, 'State', '')

# Define columns with ID column as integer auto-increment primary key
columns = ', '.join([f"`{col}` VARCHAR(255)" for col in first_df.columns])  # Backticks around column names

# cur.execute("CREATE TABLE IF NOT EXISTS data ({})".format(columns))

# Initialize ID counter
# last_id = 0

# Iterate through each Excel file
for excel_file in excel_files:
    print(excel_file)
    # Read Excel file into a DataFrame
    df = pd.read_excel(os.path.join(folder_path, excel_file))

    # Add ID column with values starting from the last ID in the table
    df['ID'] = range(last_id + 1, last_id + len(df) + 1)
    # df.insert(0, 'ID', range(int(last_id) + 1, int(last_id) + len(df) + 1))

    last_id += len(df)  # Update last_id to the last ID used in this iteration

    # Add State column with value 'Telangana' at first position
    df.insert(1, 'State', 'AndhraPradesh')

    # Iterate through DataFrame and insert rows into MySQL table
    for _, row in df.iterrows():
        # Truncate string values exceeding maximum length
        max_length = 255
        row = tuple(val[:max_length] if isinstance(val, str) and len(val) > max_length else val for val in row)

        placeholders = ', '.join(['%s'] * len(df.columns))
        query = f"INSERT INTO data ({', '.join(df.columns)}) VALUES ({placeholders})"  # Specify columns in INSERT statement
        values = tuple(None if pd.isna(val) else val for val in row)  # Convert NaN to None
        cur.execute(query, values)

    # Commit the transaction for each Excel file
    conn.commit()

# Close cursor and connection


cur.close()
conn.close()

end_time = time.time()
print(end_time-start_time)
print("SUCCESS")
