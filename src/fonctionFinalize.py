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

def FonctionAffiche2(temp3):
	resultat = ""
	for i in temp3:
		resultat += i[0] + "	" + i[-1] + "\n"
	return resultat

def finalize(source,entree,sortieSource,sortieEntree):
	
	print("Preparation fichier")
	
	temp = []

	for ligne in source:
		temp3 = [ligne.split()]
		if len(temp3)==1:
			temp += temp3

	temp2 = []

	for ligne in entree:
		temp3 = [ligne.split()]
		if len(temp3)==1:
			temp2 += temp3
	
	for i in range(len(temp)-1,0,-1):
		#print(len(temp))
		#print(i)
		#print(temp[i])
		#print(len(temp[i]))
		if len(temp[i])==0:
			del(temp[i])
			
	#print(temp)
			
	for i in range(len(temp2)-1,0,-1):
		#print(temp2[i])
		#print(len(temp2[i]))
		if len(temp2[i])==0:
			del(temp2[i])
	
	print("Fichier pret")
	
	#print(temp)
	#print(temp2)

	print("Premier traitement")

	temp3 = []

	for i in range(len(temp)):
		continu = 0
		print("Traitement produit : ")
		print(i)
		if continu == 0:
			for j in range(len(temp2)):
				#print(temp[i][0])
				#print(temp2[j][0])
				#print("Traitement sous-produit : ")
				#print(j)
				saute = 0
				for k in temp3:
					if k[1]==j:
						saute = 1
				#print(temp[i])
				#print(temp2[j])
				if(temp[i][0]==temp2[j][0]):
					if saute == 0:
						temp4 = [i,j]
						temp3 += [temp4]
						continu = 1

	for i in range(len(temp3)):
		for j in range(i+1,len(temp3)):
			if temp3[i][1]>temp3[j][1]:
				del(temp3[i])
			
	#print(temp3)

	print("Second traitement")

	temp4 = []
	temp5 = []

	for i in range(len(temp)):
		ok = 0
		for j in temp3:
			if i == j[0]:
				ok = 1
		if ok == 1:
			temp4 += [temp[i]]

	for i in range(len(temp2)):
		ok = 0
		for j in temp3:
			if i == j[1]:
				ok = 1
		if ok == 1:
			temp5 += [temp2[i]]
			
	print("Enregistrement des fichiers")
		
	resultat = FonctionAffiche2(temp4)

	numpy.savetxt(sortieEntree,[resultat],fmt='%s')

	resultat = FonctionAffiche2(temp5)

	numpy.savetxt(sortieSource,[resultat],fmt='%s')