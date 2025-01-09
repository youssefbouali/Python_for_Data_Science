import requests
import pandas as pd
import json

API_KEY = "****************************"
villes = ['Agadir', 'Casablanca', 'Rabat', 'Fes', 'Tanger', 'Safi', 'Kenitra', 'Marrakech', 'Taza', 'Ouarzazate', 'Tiznit', 'Nador']
data = []

def obtenir_donnees_meteo(ville):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ville}&appid={API_KEY}&units=metric")
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return None

df = pd.DataFrame(columns=['Ville', 'Température Min', 'Température Max', 'Humidité', 'Longitude', 'Latitude', 'Température Moyenne', 'Catégorie'])
for ville in villes:
    meteo = obtenir_donnees_meteo(ville)
    if meteo:
        temp_min = meteo['main']['temp_min']
        temp_max = meteo['main']['temp_max']
        humidite = meteo['main']['humidity']
        longitude = meteo['coord']['lon']
        latitude = meteo['coord']['lat']
        temp_moyenne = (lambda t_min, t_max: round((t_min + t_max) / 2, 2))(temp_min, temp_max)
        categorie = (lambda temp: "Chaud" if temp > 20 else "Froid")(temp_moyenne)
        df2 = pd.DataFrame([{
            'Ville': ville,
            'Température Min': temp_min,
            'Température Max': temp_max,
            'Humidité': humidite,
            'Longitude': longitude,
            'Latitude': latitude,
            'Température Moyenne': temp_moyenne,
            'Catégorie': categorie
        }])
        df = df.dropna(axis=1, how='all')
        df = pd.concat([df, df2], ignore_index=True)



df.to_csv('meteo_villes_maroc.csv', index=False)
print("Les données et sauvegardées dans meteo_villes_maroc.csv")
