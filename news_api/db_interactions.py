import psycopg
from psycopg import sql

from .config import POSTGRES_CONFIG


def create_news_table() -> None:
    create_table_command = """
    CREATE TABLE IF NOT EXISTS news (
        country VARCHAR(255),
        source_website VARCHAR(255),
        author VARCHAR(255),
        title VARCHAR(255),
        published_at TIMESTAMP
    );
    """
    with psycopg.connect(**POSTGRES_CONFIG) as connection:
        cursor = connection.cursor()
        cursor.execute(create_table_command)
        connection.commit()

def insert_news(rows) -> None:
    """ 
        Insert multiple news into the vendors table.
    """

    insert_statement = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
        sql.Identifier('news'),
        sql.SQL(', ').join(map(sql.Identifier, 
                               ['country', 'source_website', 'author', 'title', 'published_at'])),
        sql.SQL(', ').join(sql.Placeholder() * 5)
    )
    with psycopg.connect(**POSTGRES_CONFIG) as connection:
        cursor = connection.cursor()
        for values in rows:
            cursor.execute(insert_statement, values)
        connection.commit()
    
