#Import des librairies

import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

def FonctionConvertion(temp3,convertion):
	for i in temp3:
		for j in convertion:
			if i[1]==j[0]:
				i[1]=j[1]
	return temp3

def FonctionDecoupagePhrase(entree):
	temp = []
	for ligne in entree:
    if len(ligne.split())==2:
		  temp += [ligne.split()]

	return temp

def ChoixAffiche(temp3):
	resultat = ""
	for i in temp3:
		resultat += i[0] + "	" + i[1] + "\n"
	return resultat

def convertisseur(source,sortie):
	temp3 = FonctionDecoupagePhrase(entree)
	
	#print(pandas.DataFrame({'temp3':temp3}))

	temp3 = FonctionConvertion(temp3,convertion)

	resultat = ChoixAffiche(temp3)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
  
  numpy.savetxt("../data/pos_reference.txt.univ",[resultat],fmt='%s')
  
  