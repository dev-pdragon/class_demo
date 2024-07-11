#import libraries
import sqlite3 as sq
from faker import Faker
from tabulate import tabulate

#constants
DATABASE_NAME = ':memory:'
TABLE_NAME ='tb_employees'
TABLE_COL_ID = 'emp_id_pk'
TABLE_COL_NAME = 'emp_name'
MAX_EMPLOYEES = 10

with sq.connect(DATABASE_NAME) as conn:

    SQL = F'''CREATE TABLE IF NOT EXISTS {TABLE_NAME}
        (
            {TABLE_COL_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
            {TABLE_COL_NAME}  TEXT NOT NULL UNIQUE
        );'''
    curr = conn.cursor()
    curr.execute(SQL)
    conn.commit()

    print(f"Table Created: {TABLE_NAME}")

    faker = Faker()

    employees_list = [ (faker.first_name(),) \
                      for each in range(MAX_EMPLOYEES)]

    SQL = f'''INSERT INTO {TABLE_NAME} ({TABLE_COL_NAME})
        VALUES (?);'''

    curr.executemany(SQL,employees_list)
    conn.commit()

    print(f"{MAX_EMPLOYEES} rows were written to {TABLE_NAME}")

    SQL = F'''SELECT {TABLE_COL_ID},
         {TABLE_COL_NAME} FROM {TABLE_NAME};'''
    result = curr.execute(SQL)
    print(result)
    HEADERS = ['ID','EMP_NAME']
    print(tabulate(result,headers=HEADERS))

    curr.close()

