import sqlite3

connexion = sqlite3.connect('../01_database/app.db')
curseur = connexion.cursor()

id_parrain = input("Entrez l'ID du parrain : ")

curseur.execute("SELECT username FROM users WHERE referrer_id = ?", (id_parrain,))
filleuls = curseur.fetchall()

if not filleuls:
    print("Ce parrain n'a aucun filleul.")
else:
    print("Liste des filleuls :")
    for f in filleuls:
        # f est un tuple (un groupe de données), on prend le premier élément
        print(f"- {f[0]}")

connexion.close()
