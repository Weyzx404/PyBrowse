texte = ''' ____        ____                             
|  _ \\ _   _| __ ) _ __ _____      _____  ___ 
| |_) | | | |  _ \\| '__/ _ \\ \\ /\\ / / __|/ _ \\
|  __/| |_| | |_) | | | (_) \\ V  V /\\__ \\  __/
|_|    \\__, |____/|_|  \\___/ \\_/\\_/ |___/\\___|
       |___/                                  
'''

print(texte)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

Research = input("Rechercher : ")

def extract_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = response.url

        links = [urljoin(base_url, link.get('href')) for link in soup.find_all('a') if link.get('href') is not None]

        return links
    else:
        print(f"Erreur : Impossible d'accéder à la page. Code d'erreur : {response.status_code}")
        return []

url = f"https://www.google.com/search?q={Research}"
links = extract_links(url)

for link in links:
    print(link)
    print("")  # Ajoute une ligne d'espace après chaque lien

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_links(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        base_url = response.url

        links = [urljoin(base_url, link.get('href')) for link in soup.find_all('a') if link.get('href') is not None]

        return links
    else:
        print(f"Erreur : Impossible d'accéder à la page. Code d'erreur : {response.status_code}")
        return []

while True:
    Research = input("Rechercher : ")

    # Exécuter la recherche
    url = f"https://www.google.com/search?q={Research}"
    links = extract_links(url)

    for link in links:
        print(link)
        print("")  
