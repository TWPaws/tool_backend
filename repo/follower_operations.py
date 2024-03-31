# ./repo/follower_operations.py

from util.database import connect_to_database


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

    insert_query = 'INSERT INTO users (id, username, email) VALUES (%s, %s, %s)'
    cursor.execute(insert_query, (user_data['id'], user_data['username'], user_data['email']))

    connection.commit()
    cursor.close()
    connection.close()
