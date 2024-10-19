# chatbot_project
Chatbot Project

This project is a simple FAQ-based chatbot built using Python, Flask, and an SQLite database. The chatbot can answer a predefined set of frequently asked questions (FAQs) and can be extended to support more complex queries.

Features

FAQ-based: The chatbot uses a dataset of frequently asked questions to respond to user queries.
Database-backed: FAQ data is stored in an SQLite database, and the chatbot queries this database for relevant answers.
Easy to Extend: You can easily add more questions and answers to the dataset to expand the chatbot's knowledge base.
Table of Contents

Installation
Usage
Database Setup
How to Extend the Dataset
Technologies Used
Installation

Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/SamarthP7704/chatbot_project.git
Navigate to the project directory:
bash
Copy code
cd chatbot_project
Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Make sure you have Python 3 installed. If you don't have Python 3, install it from here.
Database Setup

Before running the chatbot, you need to load the FAQ dataset into the SQLite database.

Run the load_database.py script to load the dataset into the database:
bash
Copy code
python load_database.py
This will create an faq_chatbot.db file and populate it with the questions and answers from the faq_dataset.csv file.
Usage

To run the chatbot locally:

Start the Flask development server:
bash
Copy code
python chatbot.py
Open your web browser and go to http://127.0.0.1:5000/.
Type in a question from the FAQ dataset (e.g., "What is the capital of France?") and the chatbot will return an appropriate answer.
How to Extend the Dataset

To add more questions and answers:

Open the faq_dataset.csv file in a text editor or spreadsheet editor.
Add your new questions and corresponding answers in the appropriate columns.
Save the file.
Re-run the load_database.py script to update the database with the new entries.
Technologies Used

Python: Programming language for the backend.
Flask: Lightweight web framework for creating the chatbot’s web interface.
SQLite: Database to store the FAQ dataset.
HTML, CSS, Bootstrap: For the frontend user interface.
jQuery: For handling asynchronous communication between the frontend and backend.
Contributing

Feel free to submit pull requests to improve the project or add new features.

