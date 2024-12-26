import pandas as pd

#1
data = {
    'Étudiant':   ['Aicha', 'Ali', 'Nawal', 'Salim', 'Kamal'],
    'Math':         [85,     92,    88,      70,      96],
    'Physique':     [90,     81,    94,      68,      89],
    'Chimie':       [78,     85,    91,      76,      92],
    'Informatique': [88,     91,    79,      85,      95]
}
df = pd.DataFrame(data)
print ("\r\n1: \r\n", df)

#2
df = df.set_index("Étudiant") 
# note minimale, maximale et moyenne par étudiant
result = df.agg(['min', 'max', 'mean'], axis=1) #colonne
print ("\r\n\r\n2: \r\nMin,Max,Moyenne par étudiant : \r\n", result)

# note minimale, maximale et moyenne par matiere
result = df.agg(['min', 'max', 'mean'], axis=0) #ligne
print ("\r\nMin,Max,Moyenne par matière : \r\n", result)

#3
df['sum'] = df.sum(axis=1) #colonne sum
filtered_df = df[df['sum'] > 350]
print ("\r\n\r\n3: \r\nÉtudiants ayant un score total supérieur à 350 : \r\n", filtered_df)
