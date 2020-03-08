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
			resultat += "\n"
	return resultat

def retablissement(entree,sortie):
	temp = FonctionDecoupagePhrase(entree)
	
	resultat = ChoixAffiche(temp)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt(sortie,[resultat],fmt='%s')
	
	
	
	
	
	
	
	
	
	
	
	
	
def FonctionDecoupagePhrase2(entree):
	temp = []
	for ligne in entree:
		#print(len(ligne.split()))
		if len(ligne.split())>=2:
			temp += [ligne.split()]
		else:
			temp += [""]
	return temp
	
def ChoixAffiche2(temp):
	resultat = ""
	for i in range(len(temp)):
		if len(temp[i])>=2:
			resultat += temp[i][0]
			resultat += " "
		else:
			resultat += "\n"
			resultat += "\n"
	return resultat
	
def retablissement2(entree,sortie):
	temp = FonctionDecoupagePhrase2(entree)
	
	resultat = ChoixAffiche2(temp)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt(sortie,[resultat],fmt='%s')
	
	
	
	
	
	

	
def retablissement3(entree,sortie):

	resultat = ""

	for i in entree:
		temp = i.split()
		if len(temp)!=0:
			if temp[0] == "I'":
				resultat += "I" + "	" + temp[1] + "\n"
				resultat += "'" + "	" + temp[1] + "\n"
			else:
				resultat += temp[0] + "	" + temp[1] + "\n"

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt(sortie,[resultat],fmt='%s')