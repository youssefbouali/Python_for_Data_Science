import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.wandaloo.com/neuf/promo-voiture-neuve-maroc.html"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36' }
voitures = []

def obtenir_liens_voitures(page_url):
    try:
        response = requests.get(page_url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            liens = soup.select('.owl-carousel .marque-modele a')
            for lien in liens:
                if 'href' in lien.attrs:
            return [lien['href'] for lien in liens if 'href' in lien.attrs]
    except Exception as e:
        print(f"Erreur lors de la récupération des liens: {e}")
        return []

def obtenir_informations_voiture(lien):
    response = requests.get(lien, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        modele = soup.select_one('.hide-xs').text.strip()        
        all_items = soup.select('.col11 .items > li:not(.millesime)')
        for li in all_items:
            version = li.select_one('.finition a').text.strip()
            details = [detail.text.strip() for detail in li.select('.detail li')]
            prix_initial = li.select_one('.prix-promo')
            prix_initial = float(prix_initial.text.replace('DH *', '').replace(',', '').strip()) if prix_initial else None
            prix_promo = li.select_one('.prix')
            prix_promo = float(prix_promo.text.replace('DH *', '').replace(',', '').strip()) if prix_promo else None
            voitures.append([modele, version, details, prix_initial, prix_promo])
    except AttributeError:
        pass

page_url = url
while page_url:
    liens_voitures = obtenir_liens_voitures(page_url)
    for lien in liens_voitures:
        obtenir_informations_voiture(lien)
    soup = BeautifulSoup(requests.get(page_url, headers=headers).content, 'html.parser')
    next_page = soup.select_one('a.page:last-child')
    page_url = next_page['href'] if next_page else None

df_voitures = pd.DataFrame(voitures, columns=['Modèle', 'Version', 'Détails', 'Prix Initial', 'Prix Promo'])
df_voitures.to_csv('promotions_voitures.csv', index=False)
print("Les promotions et sauvegardées dans promotions_voitures.csv ")