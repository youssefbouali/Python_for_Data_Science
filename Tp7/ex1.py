import pandas as pd

#1
print ("\r\n 1")
sf_permits = pd.read_csv('Building_Permits.csv')

#2
print ("\r\n 2")
print("Premières lignes du DataFrame :")
print(sf_permits.head())

#3 Oui
print ("\r\n 3")
print(sf_permits.isnull().sum())

#4
print ("\r\n 4")
missing_percentage = (sf_permits.isnull().sum().sum() / sf_permits.size) * 100
print(f"Nombre total de valeurs manquantes : {sf_permits.isnull().sum().sum()}")
print(f"Pourcentage de valeurs manquantes : {missing_percentage:.2f}")

#5
print ("\r\n 5")
sf_permits_no = sf_permits.dropna()
print(f"Nombre de lignes restantes après suppression: {len(sf_permits_no)}")

#6
print ("\r\n 6")
#a
sf_permits_with_na_dropped = sf_permits.dropna(axis=1)
columns_dropped = sf_permits.shape[1] - sf_permits_with_na_dropped.shape[1]
#b
print(f"Nombre de colonnes supprimées : {columns_dropped}")

#7
print ("\r\n 7")
sf_permits_with_na_imputed = sf_permits.bfill().fillna(0)
print(f"Valeurs manquantes imputées : {sf_permits_with_na_imputed}")