#print("\nex3\n")

def mot_plus_long(fichier):
    try:
        with open(fichier, 'r') as f:
            mots = []
            for ligne in f:
                # Supprimer les espaces inutiles au début et à la fin de la ligne.
                mot_nettoye = ligne.strip()
                # Si la ligne n'est pas vide, l'ajouter à la liste.
                if mot_nettoye:
                    mots.append(mot_nettoye)
            
            if not mots:
                raise ValueError("Le fichier est vide.")
            mot_long = max(mots, key=len)
            return mot_long, len(mot_long)
    
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")
    except IOError:
        print("Erreur lors de la lecture du fichier.")
    except ValueError as e:
        print(e)

print( mot_plus_long("file.txt") )
