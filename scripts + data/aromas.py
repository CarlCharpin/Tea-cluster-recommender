import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

# Rend les graphiques plus gros
sns.set(rc={'figure.figsize':(11.7,8.27)})

varitest =  pd.read_csv('data/varitest.csv',  encoding='latin-1')

#Afin de voir s'il existe une explication pour les autres clusters, j'ai décidé d'analyser l'intensité des arômes présents dans un cluster.
#Pour cela, on somme la valeur de chaque arôme pour un cluster donné et on divise par le nombre de thés présents dans le cluster.

#Initialisation des listes
arom_flora =  []
arom_fruit =  []
arom_bois =  []
arom_terre =  []
arom_epice =  []
arom_vege =  []

#Pour chaque cluster, on fais la moyenne des valeurs d'arômes des thés.
i = 0
while i<5:
    arom_flora.append(varitest[varitest['cluster']==i]['floral'].sum()/len(varitest[varitest['cluster']==i]))
    arom_fruit.append(varitest[varitest['cluster']==i]['fruite'].sum()/len(varitest[varitest['cluster']==i]))
    arom_bois.append(varitest[varitest['cluster']==i]['boise'].sum()/len(varitest[varitest['cluster']==i]))
    arom_terre.append(varitest[varitest['cluster']==i]['terreux'].sum()/len(varitest[varitest['cluster']==i]))
    arom_epice.append(varitest[varitest['cluster']==i]['epice'].sum()/len(varitest[varitest['cluster']==i]))
    arom_vege.append(varitest[varitest['cluster']==i]['vegetal'].sum()/len(varitest[varitest['cluster']==i]))
    i+=1

	
arom_cluster = [1,2,3,4,5]
clusters = [0,1,2,3,4]
i=0
while i<5:
    arom_cluster[i] = [arom_flora[i], arom_fruit[i], arom_bois[i],arom_terre[i], arom_epice[i], arom_vege[i]]
#    arom_cluster.append(arom_flora[i], arom_fruit[i])
    i+=1

	
dicts = {}
keys = range(5)
for i in keys:
    dicts[i] = arom_cluster[i]
	
aromas = pd.DataFrame(dicts)

aromasT=aromas.transpose()
aromasT['clusters'] = clusters
aromasT.columns = ['floral','fruite','boise','terreux','epice','vegetal','clusters']
aromasT.set_index('clusters', inplace=True)
aromasTbar = aromasT.reset_index().melt(id_vars=['clusters'])
color_aromas = ['#e6e600', '#ff0000', '#996633', '#4d2600' ,'#ff8000','#006600']
plt.title('Distribution des arômes dans les clusters')
plt.xlabel('Clusters')
plt.ylabel('Moyenne des arômes')
ax2 =sns.barplot(x='clusters', y='value', hue='variable', data=aromasTbar, palette = color_aromas)
plt.draw()
plt.pause(5)


