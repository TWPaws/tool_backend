import mysql.connector
import config as cfg

def connect_to_database():
    config = {
        'host': config.host_name,
        'user': cfg.database_user,
        'password': cfg.database_password,
        'database': cfg.database_name
    }
    return mysql.connector.connect(**config)