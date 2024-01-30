import mysql.connector

mydp = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "310104",
    database = "LaPlateforme",
)
cursor = mydp.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
result = cursor.fetchone()
total_surface = result[0]
print("La capacite de toutes les salles est de :", total_surface)
cursor.close()
mydp.close()