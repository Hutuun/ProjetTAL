import nltk
import numpy

nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')

from nltk import pos_tag
from nltk import RegexpParser as RP

entree = open("../data/pos_test.txt","r")

text = []

token_tag = pos_tag(text)

temp = []
temp2 = []

for ligne in token_tag:
	#print(ligne)
	temp += [ligne[0]]
	temp2 += [ligne[1]]
	
#print(temp)

resultat = ""

for i in range(len(temp)):
	resultat += temp[i] + "	" + temp2[i] + "\n"

numpy.savetxt("../data/pos_test.txt.pos.nltk",[resultat],fmt='%s')