import mysql.connector
import config

def connect_to_database():
    config = {
        'host': 'localhost',
        'user': config.database_user,
        'password': 'LSCSz2tpzvNESyv',
        'database': 'Twitch_API_Repo'
    }
    return mysql.connector.connect(**config)