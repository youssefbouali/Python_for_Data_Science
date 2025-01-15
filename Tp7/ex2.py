import pandas as pd
import re
from fuzzywuzzy import process

#1
print ("\r\n 1")
titanic = pd.read_csv('titanic.csv')
missing_values_per_column = titanic.isnull().sum()
print("Valeurs manquantes par colonne :")
print(missing_values_per_column)

#2
print ("\r\n 2")
titanic['Age'] = titanic['Age'].fillna(titanic['Age'].median())
print(titanic['Age'])

#3
print ("\r\n 3")
titanic['Embarked'] = titanic['Embarked'].fillna(titanic['Embarked'].mode()[0])
print(titanic['Embarked'])

#4
print ("\r\n 4")
old_lignes = len(titanic)
titanic_no_na = titanic.dropna(subset=['Cabin', 'Ticket'])
lignes_removed = old_lignes - len(titanic_no_na)
print(f"Nombre de lignes supprimées : {lignes_removed}")

#5
print ("\r\n 5")
titanic['Title'] = titanic['Name'].apply(lambda x: re.findall(r',\s*(\w+)\.', x)[0] if re.findall(r',\s*(\w+)\.', x) else '')
titanic['Name'] = titanic['Name'].apply(lambda x: re.findall(r'\.(.*)', x)[0] if re.findall(r'\.(.*)', x) else '')
print(titanic['Name'])

#6
print ("\r\n 6")
titanic['Sex'] = titanic['Sex'].map(lambda x: 0 if x == 'male' else 1 if x == 'female' else None)
print(titanic['Sex'])

#7
print ("\r\n 7")
titanic['Embarked'] = titanic['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
print(titanic['Embarked'])

#8
print ("\r\n 8")
name_list = titanic['Name'].tolist()
matches = []
for name in name_list:
    match = process.extract(name, name_list, limit=10)
    matches.extend([(name, matched_name, score) for matched_name, score in match if score >= 90 and name != matched_name])
matches_sorted = sorted(matches, key=lambda x: x[2], reverse=True)
print("Paires de noms similaires avec un score >= 90 :")
for match in matches_sorted:
    print(match)
