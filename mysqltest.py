import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="aakash",passwd="1234",database='aa')

mycusrosr=mydb.cursor()

mycusrosr.execute("select * from stu")

for i in mycusrosr:
  print(i)
