import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()

def create_connection():
    conn = None

    try:
        conn = psycopg2.connect(
            host=os.getenv('HOST'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            database=os.getenv('DATABASE'),
            port=os.getenv('PORT')
        )
    except Error as e:
        print('Error' + str(e))
    return conn