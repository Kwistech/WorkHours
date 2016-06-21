from datetime import date
from sqlite3 import *


def create_conn():
    conn = connect("hours.db")
    return conn


def create_table(conn):
    sql = 'CREATE TABLE hours (ID, Date, Times, Hours)'

    try:
        conn.execute(sql)
    except OperationalError:
        pass


def select_all_len(conn):
    sql = 'SELECT * FROM hours'

    try:
        results = conn.execute(sql)
    except OperationalError:
        raise
    else:
        entries = results.fetchall()
        return len(entries)


def insert_row(conn, num_entries, times, hours):
    sql = 'INSERT INTO hours VALUES ("{ID}", "{Date}", "{Times}", "{Hours}")'
    today = date.today()

    try:
        conn.execute(sql.format(ID=num_entries + 1, Date=today,
                                Times=times, Hours=hours))
    except OperationalError:
        raise
    else:
        conn.commit()
