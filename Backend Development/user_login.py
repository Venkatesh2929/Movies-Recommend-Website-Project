import mysql.connector

def user_login(username, password):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="127.0.0.3",
        user="root",
        password="123456789",
        database="MovieDB"
    )
    mycursor = mydb.cursor()
    
    # Check user credentials
    mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = mycursor.fetchone()
    
    if user:
        return True, user[0]  # Return True and the username if user is found
    else:
        return False, None  # Return False if user is not found

def register_user(username, password, mobile_number):
    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="127.0.0.3",
        user="root",
        password="123456789",
        database="MovieDB"
    )
    mycursor = mydb.cursor()

    # Check if the username already exists
    mycursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = mycursor.fetchone()
    if existing_user:
        return False  # User already exists, registration failed

    # Insert new user into the database
    mycursor.execute("INSERT INTO users (username, password, mobile_number) VALUES (%s, %s, %s)", (username, password, mobile_number))
    mydb.commit()
    return True  # Registration successful

def get_logged_in_user(username, password):
    # Function to get the logged-in user's username
    logged_in, username = user_login(username, password)
    if logged_in:
        return username
    else:
        return None
