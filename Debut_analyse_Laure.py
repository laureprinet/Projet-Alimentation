# Pour commencer l'analyse de notre dataset, il faut voir sa taille, le type de ses données, si certaines sont manquantes ...
# Faisons donc cela :)

# +
import numpy as np
import pandas as pd

df=pd.read_csv('dataset.zip',compression='zip', header=0, sep=';', quotechar='"',low_memory=False)
# -



# Les séparateurs de notre fichier (zipcar trop gros) sont des ';' ce que nous devons spécifier à l'ouverture du dataset. 
# De plus, certaines colonnes mélangent différents types de données ce qui pose problème lors de l'ouvertur si l'on impose pas low_memory=False (cela permet de lire le fichier en entier avant de deviner les types de données)



df.head(2)

df.shape

df.info()



# On voit ici que l'on a affaire a un dataframe très conséquent en terme de place mémoire avec 109 colonnes et plus de 25 000 lignes. 



df.columns



# La notice de ce dataset nous informe que ce-dernier considère les 4114 individus de ce qu'ils appellent la "population 3". Ainsi, dans la colonne 'POPULATION', il y aura la même valeur pour tous les individus : Pop3. Cette colonne nous étant alors inutile, nous pouvons l'enlever des données à analyser.



df.pop('POPULATION')
df.head(2)   #on vérifie bien que .pop() ait directement modifier notre dataframe



#
#
#
# La notice nous indique aussi que la colonne NUM_LIGNE correspond à un identifiant unique. Nous pouvons alors l'utiliser comme index :
#
#
#
#

df=df.set_index('NUM_LIGNE')
df.head()



# Nous réorganisons alors selon l'index les lignes :

df=df.sort_index()
df.head()

# On remarque alors qu'il faudra bien distinguer les indexs du numéro de la ligne car tous les chiffres n'apparaissent pas dans les indexs (ce qui est dû au premier tri de la population Pop3).



df.index



display(df.isna().head(10))
display(df.isna().tail(10))



# Il semblerait que sur les 10 premières et dernières lignes, dans les colonnes affichées, il n'y ait pas de valeurs manquantes. Cependant, pour être sûres de ne pas en avoir dans l'entièreté du dataframe, comptons-les.

df.isna().sum()

df.isna().sum().sum()

df.isna().sum(axis=1)



# On se rend ainsi compte qu'il y a finalement beaucoup de valeurs manquantes mais qu'elles sont peu nombreuses sur une même ligne. Retirons alors les colonnes comprenant des valeurs manquantes.




