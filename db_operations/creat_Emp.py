import mysql.connector

conn = mysql.connector.connect(
    host="localhost", database="mydb", user="root", password="###"
)

if conn.is_connected():
    print("Connected to mydb database")

cursor = conn.cursor()

cursor.execute("select * from emp")

try:
    cursor.execute('insert into emp values(3,"Abhy",30000);')
    conn.commit()
    print("Record Added")
except Exception as e:
    print(e)
    conn.rollback()

cursor.close()
conn.close()
