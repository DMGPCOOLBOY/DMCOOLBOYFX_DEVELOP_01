
import sqlite3

connexion = sqlite3.connect('../01_database/app.db')

def inscrire_utilisateur(pseudo, parrain_id):
    curseur = connexion.cursor()
    
    # --- C'EST ICI QU'ON AJOUTE LA SÉCURITÉ ---
    # 1. On cherche si l'ID existe
    curseur.execute("SELECT id FROM users WHERE id = ?", (parrain_id,))
    resultat = curseur.fetchone()
    
    # 2. On teste le résultat
    if resultat is None:
        print("Erreur : Ce parrain n'existe pas !")
    else:
        # Si on l'a trouvé, on fait l'inscription (tes anciennes lignes)
        curseur.execute("INSERT INTO users (username, referrer_id) VALUES (?, ?)", (pseudo, parrain_id))
        connexion.commit()
        print("Utilisateur inscrit !")


pseudo_choisi = input("Entrez votre pseudo : ")
parrain_choisi = input("Entrez l'ID du parrain : ")


inscrire_utilisateur(pseudo_choisi, parrain_choisi)







