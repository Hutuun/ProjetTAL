import nltk
import numpy

nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')

from nltk import pos_tag
from nltk import RegexpParser as RP

entree = open("wsj_0010_sample.txt","r")

text = []

for ligne in entree:
	#print(ligne)
	text += ligne.split()

#text = "learn php from guru99 and make study easy".split()

#print("Après découpage : ", text)

token_tag = pos_tag(text)

print("Après token", token_tag)
#Compound:{<DT>?<JJ>*<NN>}
patterns= """P1:{<JJ><NN>}
P2:{<NN><NN>}
P3:{<JJ><NN><NN>}
P4:{<JJ><JJ><NN>}"""

chunker = RP(patterns)

print("After Regex:",chunker)

output = chunker.parse(token_tag)

print("After Chunking",output)

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

numpy.savetxt("wsj_0010_sample.txt.pos.nltk",[resultat],fmt='%s')