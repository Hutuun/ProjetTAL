#Import des librairies

import numpy


#Fonction

def FonctionDecoupagePhrase1(entree):
	temp = []
	
	for ligne in entree:
		print(ligne)
		temp += [ligne.split()]

	# print(temp)
	temp2 = []
	for i in temp:
		# print(i)
		temp2 += i
	
	
	# print(temp2)
	temp3 = []
	for i in temp2:
		# print(i)
		if(i == ""):
			temp3 += "\n"
		else:
			temp3 += [i.split("/")]
	return temp3

#Ouverture des fichiers sources

source = open("../../data/ne_test.txt.ne.stanford.wrongformat","r")

temp = FonctionDecoupagePhrase1(source)

numpy.savetxt("../../data/ne_test.txt.ne.stanford",temp,fmt='%s')