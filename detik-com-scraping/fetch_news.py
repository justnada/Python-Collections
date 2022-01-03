import psycopg2
from config import config

def fetch_news():
    sql = "SELECT * FROM detik_com;"

    connect = None
    data = None

    try:
        params = config()
        connect = psycopg2.connect(**params)
        cursor = connect.cursor()

        cursor.execute(sql)

        connect.commit()

        data = cursor.fetchall()

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as err:
        print(f'error : {err}')
    finally:
        if data is not None:
            connect.close()

    return data