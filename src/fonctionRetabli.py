#Import des librairies

import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

def FonctionDecoupagePhrase(entree):
	temp = []
	for ligne in entree:
		#print(len(ligne.split()))
		if len(ligne.split())>=2:
			temp += [ligne.split()]
		else:
			temp += [""]
	return temp
	
def ChoixAffiche(temp):
	resultat = ""
	for i in range(len(temp)):
		if len(temp[i])>=2:
			if i != 0:
				resultat += " "
			for j in range(len(temp[i])-1):
				if j != 0:
					resultat += " "
				resultat += temp[i][j]
		else:
			resultat += "\n"
	return resultat

def retablissement(entree):
	temp = FonctionDecoupagePhrase(entree)
	
	resultat = ChoixAffiche(temp)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt("..\data\pos_reference.txt",[resultat],fmt='%s')