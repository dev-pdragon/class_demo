#imports 
import sqlite3 as sq
from faker import Faker
from tabulate import tabulate

#constants
DATABASE_NAME = ':memory:' #the database will be in RAM
TABLE_NAME = 'tb_employee'
TABLE_COL_ID = 'emp_id_pk'
TABLE_COL_NAME = 'EMP_NAME'
MAX_EMPLOYEES = 10

#create a connection
with sq.connect(DATABASE_NAME)  as conn:
    
    #create a SQL statement to create a database
    SQL = f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME}
        (
            {TABLE_COL_ID} INTEGER PRIMARY KEY AUTOINCREMENT,
            {TABLE_COL_NAME} TEXT NOT NULL UNIQUE
        );'''

    #create a cursor
    curr = conn.cursor()
    #execute the SQL statement aginst the cursor
    curr.execute(SQL)
    #commit the change
    conn.commit()

    print(f'Table Created: {DATABASE_NAME}')

    #create the faker object
    faker = Faker()

    employees_list = [(faker.first_name(),) for each in \
                      range(MAX_EMPLOYEES)]
    
    SQL = f'''INSERT INTO {TABLE_NAME} ({TABLE_COL_NAME}) \
        VALUES (?);'''

    #execute the cursor using the list of tuples
    #and the SQL statement
    curr.executemany(SQL,employees_list)
    conn.commit()
    print(f'{MAX_EMPLOYEES} rows were written to {DATABASE_NAME}')

    #query 
    SQL = F'''SELECT 
        {TABLE_COL_ID},
        {TABLE_COL_NAME}
        FROM {TABLE_NAME};'''

    #execute
    result = curr.execute(SQL)

    #create a Header
    HEADERS = ['ID','EMP_NAME']
    print(tabulate(result,headers=HEADERS))

    #close the cursor
    curr.close()


    







