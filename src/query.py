import psycopg2
from psycopg2 import Error

from .connection import create_connection

def add_movies(data):
    conn = create_connection()

    sql = """INSERT INTO movies(title, premiere, country) VALUES (%s, %s, %s)"""

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return cur.lastrowid

    except Error as e:
        print(f'Error at add_movies : {str(e)}')
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def list_movies():
    conn = create_connection()

    sql = """SELECT * FROM movies ORDER BY id ASC"""

    try:
        cur = conn.cursor()
        cur.execute(sql)
        all_movie = cur.fetchall()
        return all_movie

    except Error as e:
        print(f'Error at list_movies: {str(e)}')
        return False
    finally:
        if conn:
            cur.close()
            conn.close()


def reanme_movies(_id, new_title):
    conn = create_connection()

    sql = """UPDATE movies SET title = '{new_title}' WHERE id = {_id}""".format(new_title=new_title, _id = _id)


    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.lastrowid

    except Error as e:
        print(f'Error at rename_movies: {str(e)}')
        return False
    finally:
        if conn:
            cur.close()
            conn.close()

def remove_movies(_id):
    conn = create_connection()

    sql = """ DELETE FROM movies WHERE id = {_id}""".format(_id=_id)

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.lastrowid

    except Error as e:
        print(f'Error at remove_movies: {str(e)}')
        return False
    finally:
        if conn:
            cur.close()
            conn.close()



