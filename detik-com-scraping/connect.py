import psycopg2
from config import config

# connect to database
def connect():
    connect = None

    try:
        # read connection parameters
        params = config()

        # connect to db
        print('Connecting to postgresql database...')
        connect = psycopg2.connect(**params)

        # create cursor
        cursor = connect.cursor()

        print('PostgreSQL database version:')
        cursor.execute('SELECT version()')

        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connect is not None:
            connect.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()