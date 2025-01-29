import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1.
print("\r\n 1:")
data = pd.read_csv('LA-museums.csv', index_col='Date', parse_dates=True)

# 2.
print("\r\n 2:")
print("\n--- 5 Premières Lignes ---\n")
print(data.head(5))
print("\n--- 5 Dernières Lignes ---\n")
print(data.tail(5))

# 3.
print("\r\n 3:")
plt.figure(figsize=(10, 6))
plt.title("3. Evolution du nombre de visiteurs pour chaque musée au fil du temps", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Nombre de Visiteurs", fontsize=12)
sns.lineplot(data=data)
#sns.barplot(data=data)
#sns.heatmap(data=data)
#sns.scatterplot(data=data)
#sns.histplot(data=data)
#sns.kdeplot(data=data)
#sns.boxplot(data=data)
plt.legend(title="Musée", loc="upper right")
plt.grid()
plt.tight_layout()
plt.show()

# 4. Avila Adobe
print("\r\n 4:")
plt.figure(figsize=(10, 6))
plt.title("4. Nombre Moyen de Visiteurs par Musée", fontsize=14)
plt.xlabel("Musée", fontsize=12)
plt.ylabel("Visiteurs Moyens", fontsize=12)
print(data.mean(axis=0).idxmax())
sns.barplot(data=data.mean())
plt.grid()
plt.tight_layout()
plt.show()

# 5.
print("\r\n 5:")
plt.figure(figsize=(10, 8))
plt.title("5. Variations Mensuelles des Visiteurs", fontsize=14)
plt.xlabel("Mois", fontsize=12)
plt.ylabel("Musée", fontsize=12)
date_by_month = data.groupby(data.index.month).sum()
sns.heatmap(data=date_by_month, cmap="YlGnBu")
plt.xticks(rotation=15)
plt.tight_layout()
plt.show()

# 6.
print("\r\n 6:")
avila_adobe = data['Avila Adobe']
fall_winter = avila_adobe[avila_adobe.index.month.isin([9, 10, 11, 12, 1, 2])].sum()
spring_summer = avila_adobe[avila_adobe.index.month.isin([3, 4, 5, 6, 7, 8])].sum()
plt.title("6. Visiteurs d'Avila Adobe par Saison", fontsize=14)
plt.xlabel("Saison", fontsize=12)
plt.ylabel("Visiteurs Totaux", fontsize=12)
plt.bar(["Automne/Hiver", "Printemps/Été"], [fall_winter, spring_summer])
plt.tight_layout()
plt.show()
