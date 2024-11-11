from flask import Flask, render_template, request, flash, session
from werkzeug.security import check_password_hash
from db import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

app = Flask(__name__)
app.secret_key = "12sen"  # Replace with a secure, random key in production

# Set up the database engine and session
engine = create_engine("sqlite:///todo.db")  # Replace with your actual db name
Session = sessionmaker(bind=engine)  # Creates a session factory bound to this engine
db_session = Session()  # Instantiate a session to use for database operations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Retrieve data from the form
        username = request.form.get("username")
        password = request.form.get("password")

        # Query the database to find the user with the given username
        user = db_session.query(User).filter_by(username=username).first()

        # Check if the user exists and if the password matches
        if user and check_password_hash(user.password, password):
            # Placeholder for successful login, which will be replaced later
            flash("Login successful!", "info")
\
        else:
            # Placeholder for failed login
            flash("Invalid username or password", "danger")


    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
    