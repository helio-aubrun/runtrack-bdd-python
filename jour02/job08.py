import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="310104",
    database="zoo"
)
cursor = conn.cursor()

def ajouter_animal(nom, race, id_cage, date_naissance, pays_origine):
    query = """
        INSERT INTO animal (nom, race, id_cage, naissance, pays)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (nom, race, id_cage, date_naissance, pays_origine)
    cursor.execute(query, values)
    conn.commit()

def ajouter_cage(superficie, capacite_max):
    query = """
        INSERT INTO cage (superficie, max)
        VALUES (%s, %s)
    """
    values = (superficie, capacite_max)
    cursor.execute(query, values)
    conn.commit()

def afficher_animaux():
    query = "SELECT * FROM animal"
    cursor.execute(query)
    animaux = cursor.fetchall()

    for animal in animaux:
        print(animal)

def afficher_animaux_cages():
    query = """
        SELECT cage.id, cage.superficie, cage.max, GROUP_CONCAT(animal.nom SEPARATOR ', ')
        FROM cage
        LEFT JOIN animal ON cage.id = animal.id_cage
        GROUP BY cage.id
    """
    cursor.execute(query)
    cages = cursor.fetchall()

    for cage in cages:
        print(cage)

def calculer_superficie_totale():
    query = "SELECT SUM(superficie) FROM cage"
    cursor.execute(query)
    superficie_totale = cursor.fetchone()[0]

    print("Superficie totale de toutes les cages :", superficie_totale)

def main():
    while True:
        print("\n1. Ajouter un animal")
        print("2. Ajouter une cage")
        print("3. Afficher tous les animaux")
        print("4. Afficher les animaux dans les cages")
        print("5. Calculer la superficie totale des cages")
        print("0. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            nom = input("Nom de l'animal : ")
            race = input("Race de l'animal : ")
            id_cage = input("ID de la cage (laissez vide si l'animal n'est pas dans une cage) : ")
            date_naissance = input("Date de naissance (format YYYY-MM-DD) : ")
            pays_origine = input("Pays d'origine : ")
            ajouter_animal(nom, race, id_cage, date_naissance, pays_origine)

        elif choix == "2":
            superficie = float(input("Superficie de la cage : "))
            capacite_max = int(input("Capacité maximale de la cage : "))
            ajouter_cage(superficie, capacite_max)

        elif choix == "3":
            afficher_animaux()

        elif choix == "4":
            afficher_animaux_cages()

        elif choix == "5":
            calculer_superficie_totale()

        elif choix == "0":
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
