# -*- coding: UTF-8 -*-

#Libraries needed

import requests
import urllib.request
import time
import string
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import scipy


# Cette fonction va nous servir à "lire" chaque page produit pour récupérer les infos voulues
def getAndParseURL(url):
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    return(soup)
	
#Cette fonction récupère les infos du profil aromatique et garde uniquement les 6 caractéristiques voulues.
def profil(resultat):
    aromas = []
    aroma_str = str(resultat)

    aroma_list = aroma_str.splitlines()
#    print(len(aroma_list))
#    print(aroma_list)
    del aroma_list[0], aroma_list[-1]

    aromas = aroma_list

    j=0
    while j < 6:
#        print(aromas[j])
        aromas[j] = aromas[j][-9]
        j+=1
#    print(len(aroma_list))
    return aromas


# Tous les thés peuvent être trouvés sur ces 2 pages de produits (90 produits/page)
url_page_1 = 'https://camellia-sinensis.com/fr/thes/?types=nature&formats=vrac&name=asc&page_size=90&page=1'
url_page_2 = 'https://camellia-sinensis.com/fr/thes/?types=nature&formats=vrac&name=asc&page_size=90&page=2'

# On recupère les éléments html de la page grâce à Beautifulsoup
response1 = requests.get(url_page_1)
response2 = requests.get(url_page_2)

soup1 = BeautifulSoup(response1.text, 'html.parser')
soup2 = BeautifulSoup(response2.text, 'html.parser')

#On construit la liste d'adresses URL en scrapant chaque lien de produit sur les 2 pages
list_url = []
for a in soup1.find_all('a', class_= 'm-product-tile__link m-product-tile__link--image'):
    list_url.append(a['href'])
for a in soup2.find_all('a', class_= 'm-product-tile__link m-product-tile__link--image'):
    list_url.append(a['href'])
	
liste = []
for url in list_url:
    liste.append(url)
print(len(liste))


#On souhaite garder uniquement le thé en vrac dans notre liste. Pour cela, on récupère les indices de la liste contenant le mo boîte ou sac
	
k = 0
index = []
while k < len(liste):
    if 'boite' in liste[k]:
        index.append(k)
    if 'sac' in liste[k]:
        index.append(k)
    k+=1
	
# Une fois les indices connus, on supprime ces éléments de notre liste d'adresses en commençant par les indices les plus hauts.
# Ceci afin de ne pas décaler nos éléments.

l = 1
while l <len(index)+1:
    ind = index[-l]
    del(liste[ind])
    l+=1

# Informations générales
nom = []
variete = []
pays = []
temperature = []

# Profil d'arômes

floral = []
fruite = []
boise = []
terreux = []
epice = []
vegetal = []

# Liste vide pour comparer
vide = []

# En passant par toutes les adresses URL, on récupère les informations de chaque thé

i = 0
aRemplir = 'A remplir'

for url in liste:
    soup = getAndParseURL(url)
    
    # Noms du thé
    nom.append(soup.find('h1', class_= 'product-details__name').string)
    
    #Pays et type de thé
    
    # Récupère le pays et la variété ("couleur") du thé si disponible.
    genre = soup.find_all('span', class_= 'colored-label')
    if len(genre) < 2:
        variete.append(aRemplir)
        pays.append(aRemplir)
        print('OOO Ajouter manuellement les infos de ce thé OOO')
    else:
        variete.append(genre[0].string)
        pays.append(genre[1].string)
    #Récupère la température d'infusion
    prep = soup.find_all('span', class_= 'product-prep__content-row-value')
    if len(prep)>0:
        temperature.append(prep[1].string)
    elif len(prep)==0:
            temperature.append(aRemplir)
    # Récupère le profil aromatique du thé
    aroms = soup.find_all('div', class_= 'product-attributes__aroma-wrapper')
    if aroms != vide:
        aroma = profil(aroms)
        floral.append(aroma[0])
        fruite.append(aroma[1])
        boise.append(aroma[2])
        terreux.append(aroma[3])
        epice.append(aroma[4])
        vegetal.append(aroma[5])
    else:
        floral.append(aRemplir)
        fruite.append(aRemplir)
        boise.append(aRemplir)
        terreux.append(aRemplir)
        epice.append(aRemplir)
        vegetal.append(aRemplir)        
    print(nom[i], variete[i], pays[i], temperature[i], floral[i], fruite[i], boise[i], terreux[i], epice[i], vegetal[i])
    i+=1
    # Ce délai permet de ne pas surcharger le serveur et de ne pas être bloqué.
    time.sleep(1)

	#Vérification de la longueur de chaque liste
print(len(nom))
print(len(variete))
print(len(pays))
print(len(temperature))
print(len(floral))
print(len(fruite))
print(len(boise))
print(len(terreux))
print(len(epice))
print(len(vegetal))
print(len(liste))


#Sauver la liste d'url
with open("data/url_liste.txt", "w") as output:
    output.write(str(liste))
	
#Crée le dataframe pandas avec les listes
df = pd.DataFrame({'nom' : nom, 'variete' : variete, 'pays' : pays, 'temperature' : temperature, 'floral' : floral, 'fruite':fruite, 'boise':boise, 'terreux':terreux, 'epice':epice, 'vegetal':vegetal, 'url':liste})
# On exporte le dataframe nettoyé
export_csv = df.to_csv(r'data/scraped_data.csv', index=None, header=True)
