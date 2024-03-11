# Quarterly-Assesment
# Quiz Bowl Application

## Overview

This Quiz Bowl application is designed for a quarterly assessment, allowing users to play quizzes on various categories. Users can choose a specific category, answer questions, and receive feedback on their performance.

## Database

The application uses a SQLite database to store questions and answers. Each category has its own table in the database, and questions are retrieved randomly for the quiz. A separate file (`database.py`) is provided to create and populate the database with questions.

## Categories

The application supports multiple categories, each with its own set of questions. The available categories include:

- Strategic Management
- Digital Marketing
- Personal Sales
- Information Systems
- Project Management

## Create File

The `create.py` file is used to populate the database with questions. It includes two parts: one to create a new table for a category and another to add data to that table. Generative AI can be utilized to output questions and answers in a format easily pasted into the Python file.

## Read File

The `app.py` file contains the main functionality of the application. Users can select a category, play the quiz, and receive feedback on their answers. The `get_table_names` function retrieves the available categories from the database.

## How to Run

To run the application, follow these steps:

1. Run `database.py` to create and populate the database with questions.
2. Execute `app.py` to play the Quiz Bowl.

## Usage

1. Run `app.py`.
2. Choose a category by entering the corresponding number.
3. Answer the displayed questions.
4. Receive feedback on each answer.

## Dependencies

- Python 3.x
- SQLite

## Author

William Carter
