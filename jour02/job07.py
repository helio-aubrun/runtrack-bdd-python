import mysql.connector

mydp = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "310104",
    database = "runtrack",
)

cursor = mydp.cursor()

cursor.execute("SELECT * FROM employe WHERE salaire > 3000.00")

result = cursor.fetchall()
print (result)

cursor.close()

cursor = mydp.cursor()

cursor.execute("SELECT e.nom, e.prenom, e.salaire, s.nom AS service FROM employe e JOIN service s ON e.id_service = s.id;")

result = cursor.fetchall()
print (result)

cursor.close()

mydp.close()