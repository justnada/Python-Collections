import psycopg2
from config import config

def insert_news(news_title, news_link):
    sql = """ INSERT INTO detik_com(title, link)
            VALUES (%s, %s); """

    connect = None

    try:
        params = config()
        connect = psycopg2.connect(**params)
        cursor = connect.cursor()

        cursor.execute(sql, (news_title, news_link))

        connect.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f'error : {error}')
    finally:
        if connect is not None:
            connect.close()