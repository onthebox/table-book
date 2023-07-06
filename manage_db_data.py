""" Fill the databse with test data."""
import os
import pathlib

import psycopg

PARAMS = {
    'dbname': 'test_db',
    'user': 'test_user',
    'password': 'test_password',
    'host': '127.0.0.1',
    'port': '8080',
}

DATA_FOLDER = pathlib.Path('C:/Users/onthe/Documents/table-book/test_db_data')
# Name of the files in needed order avoiding foreign key violation
DATA_TABLES = [
    'restaurant_chain',
    'restaurant_branch',
    'branch_adress',
]


def fill_data():
    """
    Наполнить таблицы бд из .csv в папке test_db_data.
    """
    csv_list = [DATA_FOLDER / f'{file}.csv' for file in DATA_TABLES]

    conn = psycopg.connect(**PARAMS)
    cur = conn.cursor()

    for file in csv_list:

        if not file.exists():
            print(f'Missing data file, exiting: {file}')
            break

        copy_sql = f'''COPY {file.with_suffix('').name} FROM stdin WITH (format CSV, delimiter ',', header)'''

        print(copy_sql)

        with open(file, 'r') as f:
            with cur.copy(copy_sql) as copy:
                while data := f.read(100):
                    copy.write(data)

        conn.commit()

    conn.close()


def clear_data():
    """
    Удалить все данные из всех таблиц.
    """

    conn = psycopg.connect(**PARAMS)
    cur = conn.cursor()

    clear_sql = f'''TRUNCATE {', '.join(DATA_TABLES)} CASCADE;'''
    cur.execute(clear_sql)

    conn.commit()
    conn.close()


def drop_tables():
    """
    Удалить все таблицы вместе с данными.
    """

    conn = psycopg.connect(**PARAMS)
    cur = conn.cursor()

    drop_sql = '''
        SELECT 'drop table if exists "' || tablename || '" cascade;'
        FROM pg_catalog.pg_tables
        WHERE schemaname = 'public';
    '''
    cur.execute(drop_sql)
    list_of_sql = [tup[0] for tup in cur.fetchall()]

    for sql in list_of_sql:
        cur.execute(sql)

    conn.commit()
    conn.close()


if __name__ == '__main__':
    drop_tables()
