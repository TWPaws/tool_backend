import mysql.connector

def connect_to_database():
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': '28627344',
        'database': 'Twitch_API_Repo'
    }
    return mysql.connector.connect(**config)