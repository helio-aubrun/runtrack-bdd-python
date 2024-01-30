import mysql.connector

mydp = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "310104",
    database = "LaPlateforme",
)
cursor = mydp.cursor()
cursor.execute("SELECT SUM(superficie) FROM etage")
result = cursor.fetchone()
total_surface = result[0]
print("La superficie de La Plateforme est de", total_surface, "m2")
cursor.close()
mydp.close()