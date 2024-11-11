from werkzeug.security import generate_password_hash
from db import User  # Import the User model from your models file
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Set up the database engine and session
engine = create_engine("sqlite:///todo.db")  # Use your actual database URI
Session = sessionmaker(bind=engine)
db_session = Session()

# Define user details
username = "mrfong"
password = "abc123"  # Replace with the actual password you want to use

# Hash the password
hashed_password = generate_password_hash(password)

# Create a new user instance
new_user = User(username=username, password=hashed_password)

# Add the user to the database
db_session.add(new_user)
db_session.commit()

print("User 'mrfong' added successfully with a hashed password.")
