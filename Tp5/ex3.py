import pandas as pd
#1
Produits = pd.read_csv("Produits.csv")
produits_df = pd.DataFrame(Produits)
Ventes = pd.read_csv("Ventes.csv")
ventes_df = pd.DataFrame(Ventes)
Magasin = pd.read_csv("Magasin.csv")
magasin_df = pd.DataFrame(Magasin)
#2
ventes_et_produits = ventes_df.merge( produits_df[['Produit_ID', 'Prix']] , on='Produit_ID')
ventes_et_produits["CA"] = ventes_et_produits["Prix"] * ventes_et_produits["Quantité"]
chiffres_daffaires = ventes_et_produits.groupby('Magasin_ID')["CA"].sum()
print ("\r\n\r\n2: \r\nChiffre d'affaires par magasin : \r\n", chiffres_daffaires)

#3
ventes_produits = ventes_df.merge(produits_df[['Produit_ID', 'Produit', 'Catégorie']], on='Produit_ID')
plusvendu_par_categorie = ventes_produits.groupby(['Catégorie', 'Produit']).agg({'Quantité': 'sum'}).idxmax()
print ("\r\n\r\n3: \r\nProduit le plus vendu par catégorie : \r\n", plusvendu_par_categorie)

#4
ventes_magasin_A = ventes_df[ventes_df['Magasin_ID'] == 101]
print ("\r\n\r\n4: \r\nVentes pour Magasin A : \r\n", ventes_magasin_A)

#5
chiffres_daffaires.to_csv("chiffres_daffaires.csv")
plusvendu_par_categorie.to_csv("plusvendu_par_categorie.csv")
ventes_magasin_A.to_csv("ventes_magasin_A.csv")
