import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:

        conn = mydbconnection.connect(
            database='userdb', user='root', password='toor'
            ) 
        print('👌 Connection Established')
        
        cursor = conn.cursor()

        myquery2 = "CREATE TABLE `laptop` (`Id` int(11) NOT NULL,\
            `Name` varchar(250) NOT NULL,\
             `Price` float NOT NULL,\
             `Purchase_date` date NOT NULL)"
        
        cursor.execute(myquery2)
        print('✅ Table Success')




    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        if conn.is_connected():
            conn.close()
            print('🔴 Connection Closed')







if __name__ == '__main__':
    connect()