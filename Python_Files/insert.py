import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='demodb',
                                         user='root',
                                         password='')

    mySql_insert_query = """INSERT INTO laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")