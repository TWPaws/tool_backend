# ./repo/user_operations.py

import hashlib
from util.database import connect_to_database


def fetch_all_users():
    connection = connect_to_database()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def add_user(nickname, email, hash_password):
    connection = connect_to_database()
    cursor = connection.cursor()

    insert_query = 'INSERT INTO users (nickname, username, hash_password) VALUES (%s, %s, %s)'
    cursor.execute(insert_query, (
        nickname,
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


def search_user_by_username_password(username, hash_password):
    connection = connect_to_database()
    cursor = connection.cursor()

    select_query = "SELECT * FROM users WHERE username = %s AND hash_password = %s"
    cursor.execute(select_query, (username, hash_password,))

    user = cursor.fetchone()

    cursor.close()
    connection.close()

    return user


def search_user_by_id(user_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    select_query = 'SELECT * FROM users WHERE ID = %s'
    cursor.execute(select_query, (user_id,))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user


def search_user_by_username(username):
    connection = connect_to_database()
    cursor = connection.cursor()

    select_query = 'SELECT * FROM users WHERE username = %s'
    cursor.execute(select_query, (username,))

    user = cursor.fetchone()
    cursor.close()
    connection.close()

    return user


def update_broadcaster_id(user_id, boradcaster_id):
    connection = connect_to_database()
    cursor = connection.cursor()

    update_query = 'UPDATE users SET boradcaster_id = %s WHERE ID = %s'
    cursor.execute(update_query, (boradcaster_id, user_id))

    connection.commit()
    cursor.close()
    connection.close()

    return 'True'


def update_access_toekn(user_id, access_token, refresh_token):
    connection = connect_to_database()
    cursor = connection.cursor()

    update_query = 'UPDATE users SET access_token = %s, refresh_token = %s WHERE ID = %s'
    cursor.execute(update_query, (access_token, refresh_token, user_id))

    connection.commit()
    cursor.close()
    connection.close()

    return 'True'
