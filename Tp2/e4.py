#print("\nex4\n")

import csv
import json

def csv_to_json(fichier_csv, fichier_json):
    try:
        with open(fichier_csv, 'r') as csvfile:
            lecteur = csv.DictReader(csvfile)
            data = []
            for ligne in lecteur:
                data.append(ligne)

        with open(fichier_json, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print(f"Conversion réussie. Fichier JSON sauvegardé dans {fichier_json}")
    except FileNotFoundError:
        print("Le fichier CSV spécifié n'existe pas.")
    except IOError:
        print("Erreur lors de la lecture/écriture des fichiers.")

csv_to_json("file.csv", "file.json")
