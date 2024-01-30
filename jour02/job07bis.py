import mysql.connector

class Employe:

    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="310104",
            database="runtrack"
        )
        self.cursor = self.conn.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_employe(self, salaire_min):
        query = "SELECT * FROM employe WHERE salaire > %s"
        values = (salaire_min,)
        self.cursor.execute(query, values)
        result = self.cursor.fetchall()
        return result

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

employe_manager = Employe()

employe_manager.create_employe("MAUl", "Nance", 4100.00, 2)

result = employe_manager.read_employe(3000.00)
print(result)

employe_manager.update_employe(3, 3000.00)

employe_manager.delete_employe(4)

employe_manager.close_connection()