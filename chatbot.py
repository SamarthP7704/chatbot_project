from flask import Flask, render_template, request, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Function to query the SQLite database
def query_knowledge_base(user_message):
    conn = sqlite3.connect('faq_chatbot.db')
    cursor = conn.cursor()

    # Search for a question in the database that matches the user's input
    cursor.execute("SELECT answer FROM faq WHERE question LIKE ?", ('%' + user_message + '%',))
    result = cursor.fetchone()

    conn.close()

    if result:
        return result[0]  # Return the matched answer
    else:
        return "Sorry, I don't have an answer for that."

# Generate a response using the database query
def generate_response(user_message):
    return query_knowledge_base(user_message)

# Homepage route
@app.route("/")
def home():
    return render_template("index.html")

# Handle user input and return chatbot response
@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["msg"]
    bot_response = generate_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
