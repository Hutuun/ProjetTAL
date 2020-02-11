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

def FonctionAffiche1(temp3):
	resultat = ""
	for i in temp3:
		resultat += i[0] + "_" + i[1] + " "
	return resultat

def FonctionAffiche2(temp3):
	resultat = ""
	for i in temp3:
		resultat += i[0] + "	" + i[1] + "\n"
	return resultat

def FonctionConvertion(temp3,convertion):
	#print(pandas.DataFrame({'Convertion':convertion}))
	#print(pandas.DataFrame({'Temp3':temp3}))
	for i in temp3:
		for j in convertion:
			if i[1]==j[0]:
				i[1]=j[1]
	return temp3

def FonctionDecoupagePhrase1(entree):
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

def FonctionDecoupagePhrase2(entree):
	temp = []
	for ligne in entree:
		temp += [ligne.split()]
	return temp

def ChoixAffiche(temp3):
	return FonctionAffiche2(temp3)

def Fonction1(entree,convertion):
	temp3 = FonctionDecoupagePhrase2(entree)
	
	#print(pandas.DataFrame({'temp3':temp3}))

	temp3 = FonctionConvertion(temp3,convertion)

	resultat = ChoixAffiche(temp3)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	return resultat

def Fonction2(entree,convertion):
	temp3 = FonctionDecoupagePhrase1(entree)
	
	#print(pandas.DataFrame({'temp3':temp3}))

	temp3 = FonctionConvertion(temp3,convertion)

	resultat = ChoixAffiche(temp3)

	# print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	return resultat

#Ouverture des fichiers sources

source = open("POSTags_PTB_Universal_Linux.txt","r")
entree = open("wsj_0010_sample.txt.pos.nltk","r")
#entree2 = open("wsj_0010_sentence.pos.ref","r")
entree3 = open("wsj_0010_sample.pos.ref","r")

convertion = []
for ligne in source:
	convertion += [ligne.split()]
	
#print(pandas.DataFrame({'Convertion':convertion}))

resultat = Fonction1(entree,convertion)

numpy.savetxt("wsj_0010_sample.txt.pos.ntlk.ref",[resultat],fmt='%s')

#print(pandas.DataFrame({'Convertion':convertion}))

#resultat2 = Fonction2(entree2,convertion)

#numpy.savetxt("wsj_0010_sentence.pos.univ.ref",[resultat2],fmt='%s')

#print(pandas.DataFrame({'Convertion':convertion}))

resultat3 = Fonction1(entree3,convertion)

numpy.savetxt("wsj_0010_sample.pos.univ.ref",[resultat3],fmt='%s')