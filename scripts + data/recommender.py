# Script principal qui se base sur les clusters établis par le modèle et sur le profil d'arômes
# pour recommander un thé similaire à celui entré.

# Le script affiche la liste des thés et demande un numéro (index) correspondant
# ensuite il propose les recommandations.

import pandas as pd
import numpy as np
import scipy.spatial
from rec_function import recommendTea

# Ouvre le fichier csv contenant les thés déjà classifiés.
data =  pd.read_csv('data/varitest.csv',  encoding='latin-1')
data = data[['nom', 'variete', 'pays', 'temperature', 'floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal', 'url','cluster']]

# Cré un dataframe avec juste le nom du thé et affiche la liste des thés.
name = data[['nom']]
print(format(name[0:20]),'\n',format(name[21:40]),'\n')
print(format(name[41:60]),'\n',format(name[61:80]))
print(format(name[81:100]),'\n',format(name[100:120]))

# Demande à l'utilisateur d'entrer le numéro du thé voulu
print('Enter the number of your favorite tea : ')
num1 = int(input())
the = name.nom.values[num1]
#print(the)

#Fais les recommandations.
recommendTea(the)
input("Press enter to exit.")