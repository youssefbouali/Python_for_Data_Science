import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1.
print("\r\n 1:")
df = pd.read_csv('ign_scores.csv', index_col="Platform")
print(df)

# 2.
print("\r\n 2:")
print(df.loc["PC"].max())

# 3.
print("\r\n 3:")
print(df.loc["PlayStation Vita"].idxmin())

# 4.
print("\r\n 4:")
plt.figure(figsize=(10, 6))
plt.title('4. Score moyen des jeux de course par plateforme')
plt.xlabel('Plateformes')
plt.ylabel('Score moyen')
sns.barplot(data=df["Racing"])
plt.xticks(rotation=67)
plt.tight_layout()
plt.show()

# 5.
print("\r\n 5:")
plt.figure(figsize=(12, 8))
plt.title('5. Heatmap des scores moyens par plateforme et genre')
plt.xlabel('Genres')
plt.ylabel('Plateformes')
sns.heatmap(data=df, cmap="YlGnBu")
plt.xticks(rotation=50)
plt.show()

# 6.
max_genres_per_platform = df.idxmax(axis=1)
max_scores_per_platform = df.max(axis=1)
bar_data = pd.DataFrame({
    'Platform': max_genres_per_platform.index,
    'Genre': max_genres_per_platform.values,
    'Score': max_scores_per_platform.values })
plt.figure(figsize=(12, 6))
plt.title('6. Genres avec les scores moyens les plus élevés pour chaque plateforme')
bar_plot = sns.barplot(data=bar_data, x='Platform', y='Score', hue='Genre', dodge=False, palette="viridis")
for index, row in bar_data.iterrows():
    bar_plot.text(index, row['Score'], f"{row['Genre']}",  color='black',  ha="center",  fontsize=8)
plt.xlabel('Plateformes')
plt.ylabel('Score moyen le plus élevé')
plt.xticks(rotation=67)
plt.tight_layout()
plt.show()
