#Import des librairies

import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

#Fonction

def FonctionDecoupagePhrase1(entree):
	temp = []
	for ligne in entree:
		temp += [ligne.split()]

	temp2 = []
	for i in temp:
		temp2 += i

	temp3 = []
	for i in temp2:
		temp3 += [i.split("/")]
	return temp3

#Ouverture des fichiers sources

source = open("wsj_0010_sample.txt.ner.stanford","r")

temp = FonctionDecoupagePhrase1(source)

#print(pandas.DataFrame({'temp':temp}))

var = []
for i in temp:
	dedans = 0
	for j in var:
		if i[1]==j:
			dedans=1
	if dedans==0:
		var += [i[1]]
		
#print(pandas.DataFrame({'var':var}))

num = numpy.zeros(len(var))
for i in range(len(var)):
	for j in temp:
		if var[i]==j[1]:
			num[i] += 1.0
			
print(pandas.DataFrame({'Entite':var,'Nombre':num}))

#print(pandas.DataFrame({'temp':temp}))

var2 = []
#var2 += [["temp","temp",0,0]]
for i in temp:
	dedans = 0
	if i[1]=="O":
			dedans=1
	else:
		for j in var2:
			if i[0]==j[0]:
				if i[1]==j[1]:
					j[2] += 1
					dedans=1
	if dedans==0:
		var2 += [[i[0],i[1],1.0,0.0]]

#del (var2[0])

#print(pandas.DataFrame({'var2':var2}))
	
for i in var2:
	for j in range(len(var)):
		if var[j]==i[1]:
			i[3]=i[2]/num[j]

#print(pandas.DataFrame({'var2':var2}))

aff = []
aff1 = []
aff2 = []
aff3 = []

for i in var2:
	aff += [i[0]]
	aff1 += [i[1]]
	aff2 += [i[2]]
	aff3 += [i[3]]
	
print(pandas.DataFrame({'Entite nommee':aff,'Type':aff1,'Nombre d\'occurence':aff2,'Proportion dans le texte':aff3}))