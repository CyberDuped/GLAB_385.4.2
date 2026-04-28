# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect(id, name, price, purchase_date):
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
        
        record =(id, name, price, purchase_date)
        
        # Execute query
        cursor.execute(mySql_insert_query, record)

        # Commit changes to DB
        conn.commit()
        print("✅ Record inserted successfully into Laptop Table")

        cursor.close()

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        # Close Connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 Db connection closed')


if __name__ == '__main__':
    connect(23, 'HP', 1000, '2026-01-01')
    connect(24, 'Chromebook', 750, '2025-12-13')