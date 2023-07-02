# Dictionary---Flask---Application

Flask Translation App

This Flask application allows users to translate words to different languages and create a personal list of words. It also includes a login and registration system, allowing users to manage their own word list.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Eddiequal/flask---translation---app.git
```
2. Change to the project directory:
```
cd flask-translation-app
```
4. Create a virtual environment:
```
python3 -m venv venv
```
6. Activate the virtual environment:
```
source venv/bin/activate
```

Configuration

Open the config.py file and update the configuration options as needed. Set the appropriate values for the database connection and any other required settings.

Database Setup

Create a database for the application in your preferred database management system (e.g., PostgreSQL, MySQL, SQLite).
Update the database connection URL in the Database Info file with your database credentials.

Usage

Register a new account or log in if you already have one.
Enter a word in the translation form and select the desired language.
Click the "Create" button to see the translation.
Navigate to the "Dictionary" page to view, update, or delete your saved words.

Folder Structure

The project follows the following folder structure:
```
├── app.py
├── auth_forms.py
├── database_info.py
├── views.py
├── config.py
├── static
│   ├── stylesheets
│       └── style.css
└── templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dictionary.html
└── sql_queries
    ├── user_queries.py
    ├── word_queries.py
```
Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature or bug fix.
Make the necessary changes and commit your code.
Push your changes to your forked repository.
Submit a pull request describing your changes.

