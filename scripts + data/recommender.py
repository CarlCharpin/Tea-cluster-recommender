import pandas as pd
import numpy as np
import scipy.spatial
from rec_function import recommendTea

data =  pd.read_csv('data/varitest.csv',  encoding='latin-1')

data = data[['nom', 'variete', 'pays', 'temperature', 'floral', 'fruite', 'boise', 'terreux', 'epice', 'vegetal', 'url','cluster']]

name = data[['nom']]
print(format(name[0:20]),'\n',format(name[21:40]),'\n')
print(format(name[41:60]),'\n',format(name[61:80]))
print(format(name[81:100]),'\n',format(name[100:120]))

print('Enter the number of your favorite tea : ')
num1 = int(input())
the = name.nom.values[num1]
print(the)
recommendTea(the)