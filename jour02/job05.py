import mysql.connector

mydb = mysql.connector.connect(host="localhost",
    user="root",
    password="Traverse090",
    database='Laplateforme',

)

mycursor = mydb.cursor()
mycursor.execute("select * from etage ")
mycursor = list(mycursor)
superficie = mycursor[0][3] + mycursor[1][3]
print('La superficie de La Plateforme est de', superficie,'m2')
