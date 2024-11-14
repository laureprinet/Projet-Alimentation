# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# Pour poursuivre nos analyses, il faut à nouveau faire les modifications déjà faites, afin de rendre le dataset plus lisible !!

# %%
import numpy as np
import pandas as pd

df=pd.read_csv('dataset.zip',compression='zip', header=0, sep=';', quotechar='"',low_memory=False)

df.pop('POPULATION')
df=df.set_index('NUM_LIGNE')
df=df.sort_index()

# %%
df.head(2)

# %% [markdown]
# Nous voulons à présent faire l'étude suivante : comparer les valeurs moyennes de la consommation de protéines, glucides, vitamines (etc.) de l'échantillon aux valeurs recommandées. Nous tracerons de plus un graphe pour représenter cela.

# %% [markdown]
# <b> LES GLUCIDES </b>

# %%
df['glucides'].to_frame().head()

# %%
qte_nourriture_moyenne_jour=2.5e3 
X,Y=[],[] #initialisation, pour le graphe, de deux listes vides
X.append('glucides')
df['qte_glucides_journée']=df['glucides']*qte_nourriture_moyenne_jour/100
display(df['qte_glucides_journée'].to_frame().head())
print(f'La quantité moyenne (en g) de glucides consommée dans la journée est {df['qte_glucides_journée'].mean()}g')

# %% [markdown]
# On peut maintenant créer une nouvelle colonne permettant d'obtenir l'écart, par rapport à la quantité conseillée, de cette quantité de glucides consommée par personne. Or, dans la littérature, est considérée comme quantité correspondant à une alimentation normale, pour un humain "moyen" (la morphologie serait en fait à prendre en compte, ce qui n'est pas possible ici car les infos manques),  275g de glucides par jour.

# %%
qte_conseillée_glucides=275
df['ecart_glucides']=df['qte_glucides_journée']-qte_conseillée_glucides
df['ecart_glucides'].to_frame().head()

# %% [markdown]
# On voit alors que les individus correspondant aux NUM_LIGNE égaux à 3 et 7 consomment moins de glucides que ce qui est considéré comme "normal". Les 3 suivant, cependant, en consomment davantage. Regardons maintenant si, en moyenne, les gens ont tendance à consommer plus ou moins que ces deux valeurs. Pour cela, il suffit de regarder la moyenne des valeurs de la colonne écart. Si celle-ci est négative, la consommation moyenne est inférieure à la valeur conseillée ; si positive, supérieure à cette valeur.

# %%
print(f'écart moyen : {df['ecart_glucides'].mean()}.')
g=df['ecart_glucides']>=0
print(f'dépassement en pourcentage : {df['ecart_glucides'].mean()*100/qte_conseillée_glucides}')
Y.append(df['ecart_glucides'].mean()*100/qte_conseillée_glucides) #on veut pouvoir faire un graphique avec les écarts en pourcentage
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')



# %% [markdown]
# Il s'avère ainsi, que la valeur est en moyenne dépassée (elle l'est par 36% des gens).
#
#
#
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#
#
#
#
# <b> LES PROTEINES </b>
#

# %% [markdown]
# Procédons, de la même façon pour les protéines :

# %%
X.append('proteines')
df['qte_proteines_journée']=df['proteines']*qte_nourriture_moyenne_jour/100
display(df['qte_proteines_journée'].to_frame().head())
print(f'La quantité moyenne (en g) de protéines consommée dans la journée est {df['qte_proteines_journée'].mean()}g')

# %%
qte_conseillée_proteines=56 #en g
df['ecart_proteines']=df['qte_proteines_journée']-qte_conseillée_proteines
df['ecart_proteines'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_proteines'].mean()}.')
g=df['ecart_proteines']>=0
print(f'dépassement en pourcentage : {df['ecart_proteines'].mean()*100/qte_conseillée_proteines}')
Y.append(df['ecart_proteines'].mean()*100/qte_conseillée_proteines)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')



# %% [markdown]
# Il s’avère ainsi, que la valeur est, en moyenne, dépassée.
# Cela concerne 44,2% des individus, qui consomment d'avantage de protéines que ce qui est conseillé (on peut penser à la communanté des grands sportifs qui en consomment bien plus que la 'normale').
# L'écart par rapport à la moyenne est ici assez important.

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b>LE CALCIUM </b>

# %%
X.append('calcium')
df['qte_calcium_journée']=df['calcium']*qte_nourriture_moyenne_jour/100 #en mg
display(df['qte_calcium_journée'].to_frame().head())
print(f'La quantité moyenne (en mg) de calcium consommée dans la journée est {df['qte_calcium_journée'].mean()}mg')

# %%
qte_conseillée_calcium=975 #en mg
df['ecart_calcium']=df['qte_calcium_journée']-qte_conseillée_calcium
df['ecart_calcium'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_calcium'].mean()}.')
g=df['ecart_calcium']>=0
print(f'dépassement en pourcentage : {df['ecart_calcium'].mean()*100/qte_conseillée_calcium}')
Y.append(df['ecart_calcium'].mean()*100/qte_conseillée_calcium)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')


# %% [markdown]
# On comprend ici que la valeur est, en moyenne, dépassée de manière importante mais que seulement 28% des personnes sondées sont concernées par cette forte consommation de calcium. On peut faire l'hypothèse que ce grand dépassement par peu de monde est dû à la faible quantité de personnes qui prennent des petits déjeuners / goûters (et consomment du lait par exemple) ou qui prennent un produit laitier par repas.

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> L'AMIDON </b>

# %%
X.append('amidon')
df['qte_amidon_journée']=df['amidon']*qte_nourriture_moyenne_jour/100 #en g
display(df['qte_amidon_journée'].to_frame().head())
print(f'La quantité moyenne (en g) d"amidon consommée dans la journée est {df['qte_amidon_journée'].mean()}g')

# %%
qte_conseillée_amidon=125 #en g
df['ecart_amidon']=df['qte_amidon_journée']-qte_conseillée_amidon
df['ecart_amidon'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_amidon'].mean()}.')
g=df['ecart_amidon']>=0
print(f'dépassement en pourcentage : {df['ecart_amidon'].mean()*100/qte_conseillée_amidon}')
Y.append(df['ecart_amidon'].mean()*100/qte_conseillée_amidon)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')



# %% [markdown]
# Ici aussi, la valeur conseillée concernant l'amidon est dépassée (de 44,9%),  et ce dépassement correspond à 21,7% de l'échantillon de cette étude.

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> LES FIBRES </b>

# %%
X.append('fibres')
df['qte_fibres_journée']=df['fibres']*qte_nourriture_moyenne_jour/100 #en g
display(df['qte_fibres_journée'].to_frame().head())
print(f'La quantité moyenne (en g) de fibres consommée dans la journée est {df['qte_fibres_journée'].mean()}g')

# %%
qte_conseillée_fibres=30 #en g
df['ecart_fibres']=df['qte_fibres_journée']-qte_conseillée_fibres
df['ecart_fibres'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_fibres'].mean()}.')
g=df['ecart_fibres']>=0
print(f'dépassement en pourcentage : {df['ecart_fibres'].mean()*100/qte_conseillée_fibres}')
Y.append(df['ecart_fibres'].mean()*100/qte_conseillée_fibres)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')



# %% [markdown]
# La valeur conseillée est ici peu dépassée (de seuleument 153%). 

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> LES LIPIDES </b>

# %%
X.append('lipides')
df['qte_lipides_journée']=df['lipides']*qte_nourriture_moyenne_jour/100 #en g
display(df['qte_lipides_journée'].to_frame().head())
print(f'La quantité moyenne (en g) de lipides consommée dans la journée est {df['qte_lipides_journée'].mean()}g')

# %%
qte_conseillée_lipides=60 #en g
df['ecart_lipides']=df['qte_lipides_journée']-qte_conseillée_lipides
df['ecart_lipides'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_lipides'].mean()}.')
g=df['ecart_lipides']>=0
print(f'dépassement en pourcentage : {df['ecart_lipides'].mean()*100/qte_conseillée_lipides}')
Y.append(df['ecart_lipides'].mean()*100/qte_conseillée_lipides)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')

# %% [markdown]
# Pour les lipides, la consommation moyenne de cette étude est encore au dessus de la valeur consommée (avec un dépassement de plus de 290% !!) et seulement 37% de l'échantillon serait au dessus de la valeur recommendée. 

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> LA VITAMINE C </b>

# %%
X.append('vitamine_c')
df['qte_vitamine_c_journée']=df['vitamine_c']*qte_nourriture_moyenne_jour/100 #en mg
display(df['qte_vitamine_c_journée'].to_frame().head())
print(f'La quantité moyenne (en mg) de vitamine c consommée dans la journée est {df['qte_vitamine_c_journée'].mean()} mg')

# %%
qte_conseillée_vitamine_c=110 #en mg
df['ecart_vitamine_c']=df['qte_vitamine_c_journée']-qte_conseillée_vitamine_c
df['ecart_vitamine_c'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_vitamine_c'].mean()}.')
g=df['ecart_vitamine_c']>=0
print(f'dépassement en pourcentage : {df['ecart_vitamine_c'].mean()*100/qte_conseillée_vitamine_c}')
Y.append(df['ecart_vitamine_c'].mean()*100/qte_conseillée_vitamine_c)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')

# %% [markdown]
# En terme de vitamine C, la population étudiée semble être en dessous de la valeur conseillée mais de très peu.

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> LA VITAMINE D </b>

# %%
X.append('vitamine_d')
df['qte_vitamine_d_journée']=df['vitamine_d']*qte_nourriture_moyenne_jour/100 #en micro g
display(df['qte_vitamine_d_journée'].to_frame().head())
print(f'La quantité moyenne (en micro g) de vitamine d consommée dans la journée est {df['qte_vitamine_d_journée'].mean()} µg')

# %%
qte_conseillée_vitamine_d=15 #en mg
df['ecart_vitamine_d']=df['qte_vitamine_d_journée']-qte_conseillée_vitamine_d
df['ecart_vitamine_d'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_vitamine_d'].mean()}.')
g=df['ecart_vitamine_d']>=0
print(f'dépassement en pourcentage : {df['ecart_vitamine_d'].mean()*100/qte_conseillée_vitamine_d}')
Y.append(df['ecart_vitamine_d'].mean()*100/qte_conseillée_vitamine_d)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')

# %% [markdown]
# De même que pour la Vitamine C, la consommation de vitamine D de l'échantillon de population étudié est en dessous de la valeur conseillée. L'écart est de 55% et seulement 11% des personnes ont une alimentation avec plus de Vitamine D que la valeur recommandée.

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> LE SEL </b>

# %%
X.append('sel')
df['qte_sel_journée']=df['sel']*qte_nourriture_moyenne_jour/100 #en g
display(df['qte_sel_journée'].to_frame().head())
print(f'La quantité moyenne (en g) de sel consommée dans la journée est {df['qte_sel_journée'].mean()}g')

# %%
qte_conseillée_sel=5 #en g
df['ecart_sel']=df['qte_sel_journée']-qte_conseillée_sel
df['ecart_sel'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_sel'].mean()}.')
g=df['ecart_sel']>=0
print(f'dépassement en pourcentage : {df['ecart_sel'].mean()*100/qte_conseillée_sel}')
Y.append(df['ecart_sel'].mean()*100/qte_conseillée_sel)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')

# %% [markdown]
# Comme on s'y attendait, on voit que la population étudiée consomme bien plus de sel que ce qui est conseillé : un écart de 875% !!!!!
# De plus, en comprenant que seulement 35% des personnes dépassent la valeur conseillée, on peut s'inquiéter sur les conséquences de leur consommation de sel sur leur santé...

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> LE FER </b>

# %%
X.append('fer')
df['qte_fer_journée']=df['fer']*qte_nourriture_moyenne_jour/100 #en mg
display(df['qte_fer_journée'].to_frame().head())
print(f'La quantité moyenne (en mg) de fer consommée dans la journée est {df['qte_fer_journée'].mean()} mg')

# %%
qte_conseillée_fer=11 #en mg
df['ecart_fer']=df['qte_fer_journée']-qte_conseillée_fer
df['ecart_fer'].to_frame().head()

# %%
print(f'écart moyen : {df['ecart_fer'].mean()}.')
g=df['ecart_fer']>=0
print(f'dépassement en pourcentage : {df['ecart_fer'].mean()*100/qte_conseillée_fer}')
Y.append(df['ecart_fer'].mean()*100/qte_conseillée_fer)
print(f'pourcentage de personnes ayant dépassé la valeur conseillée : {g.sum()*100/g.shape[0]}')

# %% [markdown]
# Ici aussi, la quantité de fer consommée dépasse la valeur recommandée. Cette-dernière étant très basse, il est très facil de la dépasser très fortement (ici écart de 109.5%).

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
#

# %% [markdown]
# <b> ANALYSE FINALE </b>

# %%
print(X)
print(Y)
print(len(X)==len(Y))

# %%
import matplotlib.pyplot as plt

# %%
plt.bar(X,Y)
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# En conclusion, on voit grâce à cette étude, les consommations alimentaires dépassent souvent l'apport nutritiel conseillé. Il y a cependant des exception : la vitamine C et surtout la vitamine D ne sont pas assez présentes dans l'alimentation. On voit aussi que le sel pose un réel problème. De plus, consommer trop de sel peut augmenter la pression artérielle, ce qui est un facteur de risque pour les maladies cardiovasculaires et les AVC. Il faudrait donc augmenter les campagnes alimentaires, visant à diminuer la consommation trop forte de sel.

# %% [markdown]
#
