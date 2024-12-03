import sqlite3
import csv
from io import StringIO




def sql_to_csv(dataBase, table_Name):
    # Connect to SQLite database
    conn = sqlite3.connect(dataBase)
    cursor = conn.cursor()


    # Fetch all rows from the table
    cursor.execute(f"SELECT * FROM {table_Name};")
    rows = cursor.fetchall()


    # Get column names
    cursor.execute(f"PRAGMA table_info({table_Name});")
    columns = [col[1] for col in cursor.fetchall()]


    # Prepare CSV content
    csv_output = StringIO()
    csv_writer = csv.writer(csv_output, lineterminator='\n')  # Ensure consistent line endings


    # Write header
    csv_writer.writerow(columns)


    # Write rows
    csv_writer.writerows(rows)


    # Close database connection
    conn.close()


    # Return CSV formatted string
    return csv_output.getvalue().strip()




# Function to convert CSV content to SQL and insert into a table


def csv_to_sql(csv_content, dataBase, table_Name):
    # Connect to SQLite database
    conn = sqlite3.connect(dataBase)
    cursor = conn.cursor()
   
    # Read CSV content from StringIO object
    reader = csv.reader(csv_content)
    heaDer = next(reader)


    # Sanitize column names
    sanitized_Header = [f'"{coLumn}"' for coLumn in heaDer]


    # Create table
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_Name} (
            {', '.join([f"{coLumn} TEXT" for coLumn in sanitized_Header])}
        )
    ''')


    # Prepare to insert query
    query = f'INSERT INTO {table_Name} ({",".join(sanitized_Header)}) VALUES ({",".join("?" * len(heaDer))})'


    # Insert data into the table
    for row in reader:
        cursor.execute(query, row)


    # Commit and close connection
    conn.commit()
    conn.close()

