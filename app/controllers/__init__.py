import psycopg2
import os


config = {
    'host': os.environ.get('HOST'),
    'database': os.environ.get('DB'),
    'user': os.environ.get('USER'),
    'password': os.environ.get('PASSWORD')
    }


def conn_cur():

    conn = psycopg2.connect(**config)
    cur = conn.cursor()

    return conn, cur


def create_table():
    conn, cur = conn_cur()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS animes(
        id BIGSERIAL PRIMARY KEY,
        anime VARCHAR(100) NOT NULL UNIQUE,
        released_date DATE NOT NULL,
        seasons INTEGER NOT NULL
    );
    """)
    conn.commit()
    cur.close()
    conn.close()


def commit_close():
    conn, cur = conn_cur()

    return conn.commit(), cur.close(), conn.close()
