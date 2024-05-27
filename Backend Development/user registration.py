import mysql.connector

def create_user_table():
    try:
        conn = mysql.connector.connect(
            host="127.0.0.3",
            user="root",
            password="123456789",
            database="MovieDB"
        )
        cursor = conn.cursor()
        
        # Assuming the table name for user registration is 'users'
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                username VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                mobile_number BIGINT(10) NOT NULL,
                PRIMARY KEY (username)
            )
        """
        cursor.execute(create_table_query)
        conn.commit()
        
        print("User table created successfully")
    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    create_user_table()
