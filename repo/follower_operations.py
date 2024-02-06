# ./repo/follower_operations.py

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


def add_user(user_data):
    connection = connect_to_database()
    cursor = connection.cursor()

    # 假設 user_data 包含欲插入的使用者資料
    # 假設欄位包括 id、username、email 等等

    insert_query = 'INSERT INTO users (id, username, email) VALUES (%s, %s, %s)'
    cursor.execute(insert_query, (user_data['id'], user_data['username'], user_data['email']))

    connection.commit()
    cursor.close()
    connection.close()
