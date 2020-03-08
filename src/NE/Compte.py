#Import des librairies

import numpy


#Fonction

def FonctionDecoupagePhrase1(entree):
	temp = []
	
	for ligne in entree:
		# print(ligne)
		temp += [ligne.split("\n")]

	# print(temp)
	temp2 = []
	for i in temp:
		# print(i)
		temp2 += i
	
	
	# print(temp2)
	temp3 = []
	for i in temp2:
		# print(i)
		
		for j in [i.split("/")]:
			for k in j:
				temp3 += k.split(" ")
			
	# print(temp3[0])
	temp4 = ""
	n = 0
	for i in temp3:
		# print(i)
		if n%2 == 0:
			temp4 += i + " "
			# print(temp4)
		else:
			temp4 +=  i +"\n"
		n = n + 1
	# print(temp4)
	return temp4

# Ouverture des fichiers sources

# source = open("../../data/ne_test.txt.ne.stanford.wrongformat","r")

# temp = FonctionDecoupagePhrase1(source)

# source.close()

# fout = open("../../data/ne_test.txt.ne.stanford","w")
# fout.write(temp)
# fout.close()