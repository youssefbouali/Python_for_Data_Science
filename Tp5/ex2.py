import pandas as pd

#1
df = pd.read_csv('winemag-data_first150k.csv')
print("\r\n\r\n1: \r\nHead : \r\n", df.head())

#2
prixsuperieur = df[df['price'] > 50] [['designation', 'description']]
print ("\r\n\r\n2: \r\nVins avec un prix supérieur à 50 $ : \r\n", prixsuperieur)

#3
countryprice = df.groupby('country')['price'].agg(['min', 'max'])
print ("\r\n\r\n3: \r\nValeur minimale et maximale du prix par pays : \r\n", countryprice)

#4
df['rapport'] = df.apply(lambda x: x['points'] / x['price'] if x['price'] > 0 else 0 , axis=1)
print ("\r\n\r\n4: \r\nDataFrame avec le rapport qualité/prix : \r\n", df)

#5
prixpluseleve = df.groupby('region_1')['price'].mean().idxmax()
print("\r\n\r\n5: \r\nRégion avec le prix moyen le plus élevé : \r\n", prixpluseleve)

#6
sorted_df = df.sort_values(by='rapport', ascending=False)
print("\r\n\r\n6: \r\nDataFrame trié par rapport qualité/prix : \r\n", sorted_df)
