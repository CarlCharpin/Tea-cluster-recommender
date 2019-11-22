import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
#%matplotlib inline  
#Importation des algorithmes dont nous aurons besoin pour classifier les thés
from sklearn.cluster import KMeans
from sklearn.cluster import SpectralClustering


#On importe les données dans un nouveau dataframe pour l'analyse
data =  pd.read_csv('data\cleaned_data.csv',  encoding='latin-1')

# Rend les graphiques plus gros
sns.set(rc={'figure.figsize':(11.7,8.27)})

#Nous allons grouper les différents thés par rapport à leur profil d'arôme
pro = data[['floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal']]

#En regardant les données, on peut savoir en combien de clusters l'ensemble se divise le mieux.
#Pour cela, on utilise la méthode du coude (elbow method) ou le nombre optimal de clusters se situe à l'endroit ou l'inertie 
# selon le nombre de groupe forme un coude.
wcss = []

for i in range(1,21):
    kmeans = KMeans( n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(pro)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 21), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
#plt.savefig('images\elbowMethod.png')
plt.draw()
plt.pause(2)
plt.clf()
#5 clusters

kmeans = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=10, random_state=0)
pred_y = kmeans.fit_predict(pro)

# On rajoute a nos données les groupements faits
data['cluster'] = pred_y 

varitest = data[['nom','variete','pays','temperature', 'cluster', 'url','floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal']]

# On exporte le dataframe 
export_csv = varitest.to_csv(r'data\varitest.csv', index=None, header=True)

# Les couleurs choisies pour les thés sont celles du site internet.
color = ["#63CABA", "#886479", "#A5BACA", "#ABC37D", "#005970", "#D6223D"]

#On trace le nombre de thés de chaque variété pour chaque cluster
ax = sns.countplot(x="cluster", hue='variete', data=varitest, palette = color)
plt.draw()
plt.pause(5)
plt.clf()

import aromas