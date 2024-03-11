import sqlite3

def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

def main():
    # Connect to the database
    conn = sqlite3.connect('quiz_bowl.db')

    # Get table names
    table_names = get_table_names(conn)

    # Display available categories
    print("Available Categories:")
    for i, category in enumerate(table_names, 1):
        print(f'{i}. {category}')

    # Allow the user to choose a category
    try:
        choice = int(input('Enter the number of your chosen category: '))
        if 1 <= choice <= len(table_names):
            selected_category = table_names[choice - 1]
            print(f"\nYou selected '{selected_category}'. Let's play the Quiz!\n")

            # You can add your quiz logic here using the selected_category
            # For example, you can call a function to play the quiz for the selected category
        else:
            print("Invalid choice. Please choose a valid category.")
    except ValueError:
        print("Invalid input. Please enter a number.")

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()