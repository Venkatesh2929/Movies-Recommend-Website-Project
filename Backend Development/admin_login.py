import mysql.connector

# Database connection details
db_config = {
    'host': '127.0.0.3',
    'user': 'root',
    'password': '123456789',
    'database': 'MovieDB'
}

def admin_login(username, password):
    try:
        # Connect to the database
        mydb = mysql.connector.connect(**db_config)

        # Create cursor
        cursor = mydb.cursor()

        # Execute query
        query = "SELECT * FROM admin WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))

        # Fetch result
        admin = cursor.fetchone()

        if admin:
            return True
        else:
            return False

    except mysql.connector.Error as err:
        # Handle database errors
        print("Error:", err)

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'mydb' in locals() and mydb is not None:
            mydb.close()

    return False
