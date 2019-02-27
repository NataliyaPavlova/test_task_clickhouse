import sqlite3
from sqlite3 import Error
import config


def create_conn(db_file):
    ''' create connection to SQL dbase'''
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error:
        print('Connection error')
        return None
    finally:
        conn.close()


def create_table(conn):
    ''' create table in SQL dbase'''
    try:
        db = conn.cursor()
        db.execute(config.sql_create_statement)
        db.execute(config.sql_insert_statement)
        db.execute(config.sql_add_keys_statement)
    except Error as e:
        print('Connection error: {}'.format(e))


