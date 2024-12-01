import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Password123',

)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE raktco")
print("ALL DONE!")