import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas

actif = open("wsj_0010_sample.txt.conll","r")

temp = []

for ligne in actif:
	temp += [ligne.split()]
	#temp += [temp2]

#print(pandas.DataFrame({'Temp':temp}))

var = []
for i in temp:
	if len(i)==11:
		temp3 = ''
		if i[4] == 'SENT':
			temp3 += '.'
		elif i[4] == 'SCONJ':
			temp3 += 'CC'
		elif i[4] == 'COMMA':
			temp3 += ','
		elif i[4] == 'COLON':
			temp3 += ':'
		elif i[4] == 'PRP$':
			temp3 += 'PRP'
		else:
			temp3 += i[4]
		temp2 = i[2] + '	' + temp3
		#print(temp2)
		var += [temp2]

#print(pandas.DataFrame({'Temp':var}))

for i in var:
	print (i)