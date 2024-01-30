import mysql.connector

class Salarie:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="310104",
            database="runtrack"
        )
        self.cursor = self.conn.cursor()

    def create_salarie(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_salarie(self, salaire_min):
        query = "SELECT * FROM employe WHERE salaire > %s"
        values = (salaire_min,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def update_salarie(self, salarie_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, salarie_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_salarie(self, salarie_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (salarie_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

salarie_manager = Salarie()

salarie_manager.create_salarie("MAUl", "Nance", 4100.00, 2)

result = salarie_manager.read_salarie(3000.00)
print(result)

salarie_manager.update_salarie(3, 3000.00)

salarie_manager.delete_salarie(4)

salarie_manager.close_connection()