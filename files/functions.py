from datetime import date
from sqlite3 import *


def create_conn():
    """Create connection to hours.db."""
    conn = connect("./files/hours.db")
    return conn


def create_table(conn):
    """Attempt to create sqlite3 table "hours."

    Args:
        conn (sqlite3.Connection): Connection to hours.db.

    Raises:
        OperationalError: If table "hours" already exists.
    """
    sql = 'CREATE TABLE hours (ID, Date, Times, Hours, Memo)'

    try:
        conn.execute(sql)
    except OperationalError:
        pass


def select_all_len(conn):
    """Select all entries in table "hours."

    Used for ID purposes so that each entry is uniquely identified.

    Args:
        conn (sqlite3.Connection): Connection to hours.db.

    Returns:
        int: Number of entries in table "hours."

    Raises:
        OperationalError: If sql statement was not executed properly.
    """
    sql = 'SELECT * FROM hours'

    try:
        results = conn.execute(sql)
    except OperationalError:
        raise
    else:
        entries = results.fetchall()
        return len(entries)


def insert_row(conn, num_entries, times, hours, memo):
    """Insert info into hours.db table "hours."

    Args:
        conn (sqlite3.Connection): Connection to hours.db.
        num_entries (int): Total number of entries in table hours.
        times (str): Hours worked between (eg. 800 - 1600).
        hours (str): Total number of hours.
        memo (str): Memo for entry.

    Raises:
        OperationalError: If sql statement was not executed properly.
    """
    sql = 'INSERT INTO hours VALUES ' \
          '("{ID}", "{Date}", "{Times}", "{Hours}", "{Memo}")'
    today = date.today()

    try:
        conn.execute(sql.format(ID=num_entries + 1, Date=today,
                                Times=times, Hours=hours, Memo=memo))
    except OperationalError:
        raise
    else:
        conn.commit()
