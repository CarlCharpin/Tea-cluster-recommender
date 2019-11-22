import pandas as pd
import numpy as np
import scipy.spatial

data =  pd.read_csv('data/varitest.csv',  encoding='latin-1')
#print(data.columns)
#df = df[['nom', 'variete', 'pays', 'temperature', 'floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal', 'url']]
data = data[['nom', 'variete', 'pays', 'temperature', 'floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal', 'url','cluster']]
def recommendTea(input_string):
# Récupère les infos du thé connu
    input_tea = data.loc[data['nom']==input_string]
    variete_the = input_tea.variete.values[0]
# Isole tous les thés du même cluster
    cluster_the = input_tea.cluster.values[0]
    new_df = data.loc[data['cluster']==cluster_the].copy()
    new_df = new_df[new_df['nom'] != input_string].copy()

# Calcule la distance euclidienne entre tous les thés du cluster et le thé connu
    distance_sameC = scipy.spatial.distance.cdist(new_df.iloc[:,3:9], input_tea.iloc[:,3:9], metric='euclidean')
    dist_clust = distance_sameC.tolist()
    new_df['distance'] = dist_clust
    
# Crée 2 dataframe pour séparer les thés s'ils sont de la même variété que le thé connu ou non
    same_type = new_df[new_df['variete'] == variete_the].copy()
    different_type = new_df[new_df['variete'] != variete_the].copy()

# Recommande 3 thés de la même variété dans le même cluster (si possible)
    resultat1 = same_type.sort_values(['distance'])[0:3].copy()
# Recommande 2 thés du même cluster mais de variété différentes (si possible)
    resultat1 = resultat1.append(different_type.sort_values(['distance'])[0:2].copy())


    resultat = resultat1[['nom','variete','pays', 'distance']]
    res = print('Les thés recommandés pour vous sont : \n{}'.format(resultat))
    return  res
	
ceylan = 'Ceylan New Vithanakande'
recommendTea(ceylan)