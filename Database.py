import sqlite3

# Function to create a new table
def create_table(conn, table_name):
    query = f'''
    CREATE TABLE IF NOT EXISTS {table_name} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT
    );
    '''
    conn.execute(query)

# Function to add data to a table
def add_data(conn, table_name, questions):
    query = f'INSERT INTO {table_name} (question, answer) VALUES (?, ?);'
    conn.executemany(query, questions)

# Main function to create tables and add data
def main():
    categories = ['Strategic Management', 'Digital Marketing', 'Personal Sales', 'Information Systems']

    # Connect to the database
    conn = sqlite3.connect('quiz_bowl.db')

    for category in categories:
        create_table(conn, category)

    # You can use generative AI to get the questions and answers in a suitable format
    # Example questions for each category
    strategic_management_questions = [('What is SWOT analysis?', 'Strengths, Weaknesses, Opportunities, Threats'),
                                      # Add more questions here...]

    digital_marketing_questions = [('What is SEO?', 'Search Engine Optimization'),
                                   # Add more questions here...]

    personal_sales_questions = [('Define relationship selling.', 'Building and maintaining relationships with clients'),
                                # Add more questions here...]

    information_systems_questions = [('What is a database?', 'A structured collection of data'),
                                     # Add more questions here...]

    # Add data to tables
    add_data(conn, 'Strategic Management', strategic_management_questions)
    add_data(conn, 'Digital Marketing', digital_marketing_questions)
    add_data(conn, 'Personal Sales', personal_sales_questions)
    add_data(conn, 'Information Systems', information_systems_questions)

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
