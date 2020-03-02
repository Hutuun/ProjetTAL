#Import des librairies

import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

def decoupe(entree,sortie):
	
	temp = []
	
	for ligne in entree:
		temp2 = ligne.split()
		temp += [temp2]
	#print(pandas.DataFrame({'Resultat':temp}))
	
	temp2 = []
	
	for i in temp:
		for j in range(len(i)-1):
			temp3 = [i[j],i[-1]]
			temp2 += [temp3]
			
	#print(pandas.DataFrame({'Resultat':temp2}))
	
	resultat = ""
	
	for i in temp2:
		resultat += i[0]
		resultat += "	"
		resultat += i[1]
		resultat += "\n"
	
	#print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt(sortie,[resultat],fmt='%s')

def decoupe2(entree,sortie):
	
	temp = []
	
	for ligne in entree:
		temp2 = ligne.split()
		temp += [temp2]
		
	#print(pandas.DataFrame({'Resultat':temp}))
	
	temp2 = []
	
	for i in temp:
		for j in range(len(i)-1):
			temp3 = [i[j],i[-1]]
			temp2 += [temp3]
	
	temp3 = []
	
	for i in temp2:
		if i[0] == "''":
			i[0] = "\""
		if i[0] == "n't":
			i[0] = "n\"t"
		
		temp4 = i[0].split('\'')
		#print(temp4)
		for j in temp4:
			if len(j) != 0:
				temp3 += [[j,i[1]]]
			if "," in j:
				if j[-1] == ",":
					if len(j)!=1:
						temp3 += [[",","."]]
			#if "." in j and "U.S." not in j and "S.P.A" not in j and "Mr." not in j and "E." not in j and "Mass." not in j:
			#	if "Oct." not in j and "S.P.A" not in j and "Mr." not in j and "E." not in j and "Mass." not in j:
			#		if j[-1] == ".":
			#			if len(j)!=1:
			#				temp3 += [[".","."]]
	
	#print(pandas.DataFrame({'Resultat':temp3}))
	
	resultat = ""
	
	for i in temp3:
		resultat += i[0]
		resultat += "	"
		resultat += i[1]
		resultat += "\n"
	
	#print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt(sortie,[resultat],fmt='%s')
	
def decoupe3(entree,sortie):
	
	#print("Coucou")
	
	temp = []
	
	for ligne in entree:
		temp2 = ligne.split()
		temp += [temp2]
		
	#print(pandas.DataFrame({'Resultat':temp}))
	
	temp2 = []
	
	for i in temp:
		for j in range(len(i)-1):
			temp3 = [i[j],i[-1]]
			temp2 += [temp3]
	
	#print(pandas.DataFrame({'Resultat':temp2}))
	
	temp3 = []
	
	for i in temp2:
		if i[0] != "'" and i[0] != "``" and i[0] != "\"" and i[0] != "''":
			temp3 += [[i[0],i[1]]]
		#else:
		#	print(i[0])
	
	#print(pandas.DataFrame({'Resultat':temp3}))
	
	resultat = ""
	
	for i in temp3:
		resultat += i[0]
		resultat += "	"
		resultat += i[1]
		resultat += "\n"
	
	#print(pandas.DataFrame({'Resultat':resultat}))
	#print(resultat)
	
	numpy.savetxt(sortie,[resultat],fmt='%s')