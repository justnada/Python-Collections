import psycopg2
from config import config

# creating tables in postgresql
def create_tables():
    command = (
        """
        CREATE TABLE detik_com (
            id SERIAL PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            link TEXT
            )
        """
    )

    connect = None

    try:
        # read connection
        params = config()

        connect = psycopg2.connect(**params)

        cursor = connect.cursor()


        cursor.execute(command)

        # close communication with db
        cursor.close()

        # commit changes
        connect.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'error : {error}')
    finally:
        if connect is not None:
            connect.close()

if __name__ == '__main__':
    create_tables()