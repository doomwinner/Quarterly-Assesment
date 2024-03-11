import sqlite3

# Function to get table names
def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

# Function to get all data from a table
def get_table_data(conn, table_name):
    query = f'SELECT * FROM {table_name};'
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# Main function to demonstrate reading data
def main():
    # Connect to the database
    conn = sqlite3.connect('quiz_bowl.db')

    # Get table names
    table_names = get_table_names(conn)
    print(f'Table Names: {table_names}')

    # Get data from each table
    for table_name in table_names:
        table_data = get_table_data(conn, table_name)
        print(f'\n{table_name} Data:')
        for row in table_data:
            print(row)

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()