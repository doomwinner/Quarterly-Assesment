import sqlite3
import random

def get_table_names(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
    return [table[0] for table in cursor.fetchall()]

# ANSI escape codes for text color
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def get_questions(conn, category, num_questions=5):
    query = f'SELECT question, answer FROM {category} ORDER BY RANDOM() LIMIT {num_questions};'
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

def play_quiz_category(conn, category, num_questions=5):
    questions = get_questions(conn, category, num_questions)
    score = 0

    for question, answer in questions:
        user_answer = input(f'Q: {question}\nYour Answer: ')

        if user_answer.lower() == answer.lower():
            print(f'{GREEN}Correct!{RESET}')
            score += 1
        else:
            print(f'{RED}Incorrect!{RESET} Correct answer: {answer}')

    print(f'\nQuiz Completed! Your Score: {score}/{num_questions}')

    for question, answer in questions:
        user_answer = input(f'Q: {question}\nYour Answer: ')

        if user_answer.lower() == answer.lower():
            print('Correct! (in green)')
            score += 1
        else:
            print('Incorrect! (in red) Correct answer: ', answer)

    print(f'\nQuiz Completed! Your Score: {score}/{num_questions}')
    for question, answer in questions:
        user_answer = input(f'Q: {question}\nYour Answer: ')

        if user_answer.lower() == answer.lower():
            print('Correct! (in green)')
            score += 1
        else:
            print('Incorrect! (in red) Correct answer: ', answer)

    print(f'\nQuiz Completed! Your Score: {score}/{len(questions)}')

def main():
    conn = sqlite3.connect('quiz_bowl.db')
    table_names = get_table_names(conn)

    print("Available Categories:")
    for i, category in enumerate(table_names, 1):
        print(f'{i}. {category}')

    while True:
        user_input = input('Enter the number of your chosen category: ')
        if user_input.isdigit():
            choice = int(user_input)
            if 1 <= choice <= len(table_names):
                selected_category = table_names[choice - 1]
                print(f"\nYou selected '{selected_category}'. Let's play the Quiz!\n")
                play_quiz_category(conn, selected_category)
                break  # Exit the loop if the quiz is completed
            else:
                print("Invalid choice. Please choose a valid category.")
        else:
            print("Invalid input. Please enter a number.")

    conn.close()

if __name__ == '__main__':
    main()
