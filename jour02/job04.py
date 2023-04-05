import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Traverse090",
    database='Laplateforme',

)

mycursor = mydb.cursor()
mycursor.execute("select nom,capacite from salles")
print(list(mycursor))
