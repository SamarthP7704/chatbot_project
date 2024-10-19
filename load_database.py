import sqlite3
import pandas as pd

# Load the CSV dataset
df = pd.read_csv('faq_dataset.csv')  # Ensure faq_dataset.csv is in the project folder

# Create or connect to the SQLite database
conn = sqlite3.connect('faq_chatbot.db')
cursor = conn.cursor()

# Create a table in the database (if it doesn’t already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    answer TEXT
)
''')

# Insert the CSV data into the FAQ table
df.to_sql('faq', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

print("FAQ database loaded successfully!")
