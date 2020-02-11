#Import des librairies

import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

def FonctionConvertion(temp,convertion):
	for i in temp:
		for j in convertion:
			if len(i)==2:
				if i[1]==j[0]:
					i[1]=j[1]
	return temp

def FonctionDecoupagePhrase(entree):
	temp = []
	for ligne in entree:
		if len(ligne.split())==2:
			temp += [ligne.split()]
		else:
			temp += []
	return temp

def ChoixAffiche(temp):
	resultat = ""
	for i in temp:
		if len(i)==2:
			resultat += i[0] + "	" + i[1] 
		resultat += "\n"
	return resultat

def convertisseur(source,entree):
	convertion = []
	for ligne in source:
		convertion += [ligne.split()]
	
	temp = FonctionDecoupagePhrase(entree)
	
	#print(pandas.DataFrame({'temp':temp}))

	temp = FonctionConvertion(temp,convertion)

	resultat = ChoixAffiche(temp)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt("..\data\pos_reference.txt.univ",[resultat],fmt='%s')