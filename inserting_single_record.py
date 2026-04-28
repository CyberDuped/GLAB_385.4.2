import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:
        conn = mydbconnection.connect(database='userdb', user='root', password='toor')
        print('👌 Connection established')

        cursor = conn.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """
    
        cursor.execute(mySql_insert_query)

        conn.commit()
        print(cursor.rowcount, "✅ Record inserted succesfully into Laptop Table")

        cursor.close()
    
    except Error as e:
        print(f'❌ Error {e}') 

    finally:
        
        if conn is not None and conn.is_connected():
            conn.close()
            print('🔴 Db connection closed')



if __name__ == '__main__':
    connect()

            # Import libraries
