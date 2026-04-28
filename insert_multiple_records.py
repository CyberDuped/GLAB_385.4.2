import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:
        # Establish connection
        conn = mydbconnection.connect(
            database='userdb',
            user='root',
            password='toor'
        )
        print('🎉 Connected to SQL DB')

        # Perform SQL Action
        cursor = conn.cursor()

        # Create query
        mySql_insert_query = """INSERT INTO laptop (Id, Name, Price, Purchase_date) 
        VALUES (%s, %s, %s, %s)"""
        
        records_to_insert = [(4, 'HP Pavilion Power', 1999, '2019-01-11'),
        (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
        (6, 'Microsoft Surface', 2330, '2019-07-23')]
        
        
        # Execute query
        cursor.executemany(mySql_insert_query, records_to_insert)

        # Commit changes to DB
        conn.commit()
        print(f"✅ {cursor.rowcount}: Record inserted successfully into Laptop Table")

        cursor.close()

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        # Close Connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 Db connection closed')


if __name__ == '__main__':
    connect()

