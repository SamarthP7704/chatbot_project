# 🤖 Chatbot Project

This project is a simple FAQ-based chatbot built using **Python**, **Flask**, and an **SQLite** database. The chatbot answers a predefined set of frequently asked questions (FAQs) and can be extended to support more complex queries.

## ✨ Features

- **FAQ-based**: Responds to predefined questions based on an FAQ dataset.
- **Database-driven**: FAQ data is stored in an SQLite database for efficient querying.
- **Easily extendable**: Add more questions and answers to the dataset to increase the chatbot's knowledge base.
- **Web Interface**: Interact with the bot via a simple web interface using Flask and Bootstrap.

## 📦 Installation

Follow these steps to set up the project on your local machine.

1. **Clone the repository**:

    ```bash
    git clone https://github.com/SamarthP7704/chatbot_project.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd chatbot_project
    ```

3. **Install dependencies**:

    Use `pip` to install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

    Ensure you have **Python 3** installed. If not, download and install it from [Python's official website](https://www.python.org/downloads/).

## ⚙️ Database Setup

Before running the chatbot, load the FAQ dataset into the SQLite database:

1. **Run the database loading script**:

    ```bash
    python load_database.py
    ```

   This will create an SQLite database (`faq_chatbot.db`) and populate it with the data from `faq_dataset.csv`.

## 🚀 Usage

To run the chatbot locally:

1. **Start the Flask server**:

    ```bash
    python chatbot.py
    ```

2. **Open your browser** and navigate to:

    ```
    http://127.0.0.1:5000/
    ```

3. **Interact with the chatbot** by typing in questions. The chatbot will respond with answers from the FAQ dataset.

## 📚 How to Extend the Dataset

1. **Open the `faq_dataset.csv` file** in a text editor or spreadsheet software (like Excel or Google Sheets).
2. **Add new questions and answers** to the file.
3. **Save the file**.
4. **Re-run the `load_database.py` script** to update the SQLite database with the new data:

    ```bash
    python load_database.py
    ```

## 🛠 Technologies Used

- **Python**: Backend language.
- **Flask**: Web framework used to serve the chatbot.
- **SQLite**: Lightweight database for storing FAQ data.
- **HTML, CSS, Bootstrap**: Frontend design and layout.
- **jQuery**: For asynchronous communication between frontend and backend.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for more information.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to fork the repository and submit pull requests.

---

**Author**: Samarth P7704  
**Project**: [Chatbot Project](https://github.com/SamarthP7704/chatbot_project)
