import mysql.connector

def connect_to_database():
    config = {
        'host': 'localhost',
        'user': 'khakit',
        'password': 'LSCSz2tpzvNESyv',
        'database': 'Twitch_API_Repo'
    }
    return mysql.connector.connect(**config)