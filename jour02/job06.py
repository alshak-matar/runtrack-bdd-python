import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Traverse090",
    database='Laplateforme',

)

mycursor = mydb.cursor()
mycursor.execute('select * from salles')
capcite = 0
for i in mycursor:
    capcite = capcite + i[3]

print('La capacité de toutes les salles est de :',capcite)
