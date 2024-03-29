# ./repo/user_operations.py

import mysql.connector
import hashlib


def connect_to_database():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '901017fer',
        'database': 'Twitch_API_Repo'
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


def add_user(username, email, hash_password):
    connection = connect_to_database()
    cursor = connection.cursor()

    insert_query = 'INSERT INTO users (username, email, hash_password) VALUES (%s, %s, %s)'
    cursor.execute(insert_query, (
        username,
        email,
        hash_password,
    ))

    connection.commit()
    cursor.close()
    connection.close()


def search_user(username):
    connection = connect_to_database()
    cursor = connection.cursor()
    password = cursor['password']

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    select_query = 'SELECT * FROM users WHERE username = %s'
    cursor.execute(select_query, (username, hashed_password))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user


def search_user_password(username, password):
    connection = connect_to_database()
    cursor = connection.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    select_query = 'SELECT * FROM users WHERE username = %s AND hash_password = %s'
    cursor.execute(select_query, (username, hashed_password))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user

def search_user_id(user_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    select_query = 'SELECT * FROM users WHERE ID = %s'
    cursor.execute(select_query, (user_id))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user
