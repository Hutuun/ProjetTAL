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
		temp += [ligne.split()]

	temp2 = []
	for i in temp:
		temp2 += i

	temp3 = []
	for i in temp2:
		temp3 += [i.split("_")]
	return temp3
	
def FonctionAffiche(temp3):
	resultat = ""
	for i in temp3:
		#print(i)
		if len(i) == 2:
			resultat += i[0] + "	" + i[1] + "\n"
	return resultat

def formatage(entree,sortie):
	temp = FonctionDecoupagePhrase(entree)
	#print(temp)
	resultat = FonctionAffiche(temp)
	numpy.savetxt(sortie,[resultat],fmt='%s')