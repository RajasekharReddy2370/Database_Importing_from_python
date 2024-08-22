import pandas as pd
import sqlite3

# Read the Excel file
df = pd.read_excel('/home/rajashekar/Desktop/demo.xlsx')

# Connect to SQLite database (or create if not exists)
conn = sqlite3.connect('Demo.db')
cursor = conn.cursor()

# Create table with column names from first row of Excel file
df.head(0).to_sql('Details', conn, if_exists='replace', index=False)

# # Insert data into table
# df.to_sql('your_table_name', conn, if_exists='append', index=False)

# Commit changes and close connection
conn.commit()
conn.close()