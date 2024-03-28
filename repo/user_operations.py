# ./repo/user_operations.py

import mysql.connector


def connect_to_database():
    config = {
        'host': 'localhost',
        'user': '',
        'password': 'your_password',
        'database': 'your_database',
    }
    return mysql.connector.connect(**config)


def fetch_all_users():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def add_user(access_token, username, email, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    insert_query = 'INSERT INTO users (accesss_token, username, email, password) VALUES (%s, %s, %s, %s)'
    cursor.execute(insert_query, (
        access_token,
        username,
        email,
        password
    ))

    connection.commit()
    cursor.close()
    connection.close()

def search_user(username):
    connection = connect_to_database()
    cursor = connection.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    select_query = 'SELECT * FROM users WHERE username = %s'
    cursor.execute(select_query, (username, hashed_password))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user

def search_user(username, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    select_query = 'SELECT * FROM users WHERE username = %s AND password = %s'
    cursor.execute(select_query, (username, hashed_password))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user
