import string
import pandas as pd
import numpy as np
import scipy

#On importe les données dans un nouveau dataframe pour l'analyse
df =  pd.read_csv('data/scraped_data.csv',  encoding='latin-1')

#On retire les espaces superflus de la valeur "temperature"
df['temperature']= df['temperature'].str.strip()

# On cherche les thés dont le profil d'arôme n'est pas connu
arome_vide = np.where(df['floral']=='A remplir')
arome_vide[0][1]
df.loc[arome_vide[0][0]]['url']

#En comparant la description du matcha sora avec les trois autres matcha, j'ai décidé du profil d'arome suivant : 0 0 0 0 0 3
#La description ne parle que du côté végétal contrairement aux autres thés.
df.loc[arome_vide[0][0]]['floral']=0
df.loc[arome_vide[0][0]]['fruite']=0
df.loc[arome_vide[0][0]]['boise']=0
df.loc[arome_vide[0][0]]['terreux']=0
df.loc[arome_vide[0][0]]['epice']=0
df.loc[arome_vide[0][0]]['vegetal']=3

#Pour le pu er yongde da shan, vieux théiers, j'ai décidé de ne pas le garder dans la liste. Beaucoups de pu er sont déjà présents
#et je ne m'y connais pas assez dans ce type de thé pour extrapoler les profils des autres pu ers.
df = df.drop([arome_vide[0][1]], axis=0)

temp_vide = df[df['temperature']=='A remplir'].index.tolist()

#Tous les thés Pu Er semblent être infusés à 95 degrés C.
df.at[temp_vide[0],'temperature'] = 95
df.at[temp_vide[1],'temperature'] = 95
df.at[temp_vide[2],'temperature'] = 95

#La température et les arômes sont des integer
df.temperature = df.temperature.astype(np.int64)
df.floral = df.floral.apply(np.int64)
df.fruite = df.fruite.apply(np.int64)
df.boise = df.boise.apply(np.int64)
df.terreux = df.terreux.apply(np.int64)
df.epice = df.epice.apply(np.int64)
df.vegetal = df.vegetal.apply(np.int64)


df = df[['nom', 'variete', 'pays', 'temperature', 'floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal', 'url']]

# On exporte le dataframe nettoyé
export_csv = df.to_csv(r'data/cleaned_data.csv', index=None, header=True)