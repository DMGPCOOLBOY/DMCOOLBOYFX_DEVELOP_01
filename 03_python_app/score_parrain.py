import sqlite3

# Connexion à la base de données
connexion = sqlite3.connect('../01_database/app.db')
curseur = connexion.cursor()

id_parrain = input("Entrez l'ID du parrain pour voir son score : ")

# On exécute la requête pour compter
curseur.execute("SELECT COUNT(*) FROM users WHERE referrer_id = ?", (id_parrain,))

# On récupère le résultat
resultat = curseur.fetchone()

nombre_filleuls = resultat[0]

print(f"Ce parrain a actuellement {nombre_filleuls} filleul(s).")

connexion.close()
