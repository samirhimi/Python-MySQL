"""
Script to set up the MySQL database for the Flask application
Run this script once to create the database
"""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def create_database():
    """Create the database and tables"""
    try:
        # Connect to MySQL server (without selecting a database initially)
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            db_name = os.getenv('MYSQL_DATABASE')
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"✓ Database '{db_name}' created/verified")
            
            # Select the database
            cursor.execute(f"USE {db_name}")
            
            # Create users table
            create_table_sql = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(120) UNIQUE NOT NULL,
                age INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
            cursor.execute(create_table_sql)
            print("✓ 'users' table created/verified")
            
            connection.commit()
            cursor.close()
            connection.close()
            
            print("\n✓ Database setup completed successfully!")
            
    except Error as e:
        print(f"Error: {e}")
        return False
    
    return True


if __name__ == '__main__':
    print("Setting up MySQL database...\n")
    create_database()
