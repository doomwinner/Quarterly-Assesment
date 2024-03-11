import sqlite3
import random
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "quiz_bowl.db")
with sqlite3.connect(db_path) as db:

    def play_quiz(conn, category):
    # Retrieve questions for the selected category
        query = f'SELECT * FROM {category};'
        cursor = conn.cursor()
        cursor.execute(query)
        questions = cursor.fetchall()

    # Shuffle the questions
        random.shuffle(questions)

    # Play the quiz
        for question, answer in questions:
            user_answer = input(f'Q: {question}\nYour Answer: ')

        if user_answer.lower() == answer.lower():
            print('Correct! (in green)')
        else:
            print('Incorrect! (in red) Correct answer: ', answer)

def main():
    # Connect to the database
    conn = sqlite3.connect('quiz_bowl.db')

    # Allow the user to choose a category
    categories = ['Strategic Management', 'Digital Marketing', 'Personal Sales', 'Information Systems','Project Management']
    print('Choose a category:')
    for i, category in enumerate(categories, 1):
        print(f'{i}. {category}')

    choice = int(input('Enter the number of your choice: '))
    selected_category = categories[choice - 1]

    # Play the quiz
    play_quiz(conn, selected_category)

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()