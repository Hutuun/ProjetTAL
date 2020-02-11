import xml.etree.ElementTree as ET
import pandas

tree = ET.parse('wsj_0010_sample.txt.se.xml')
root = tree.getroot()

print(root)

temp = []
temp2 = []

for child in root.iter('string'):
	temp += [child.text]
	
for child in root.iter('type'):
	temp2 += [child.text]
		
var = []
for i in range(len(temp)):
	temp3 = [temp[i],temp2[i]]
	var += [temp3]

#print(pandas.DataFrame({'Entite nommee':var}))

var2 = []
for i in var:
	stop = 0
	for j in var2:
		if i[0]==j[0]:
			stop = 1
	if stop == 0:
		temp = [i[0],i[1],0.0,0.0]
		for j in var:
			if i[0]==j[0]:
				temp[2]+=1
		var2 += [temp]
	
#print(pandas.DataFrame({'Entite nommee':var2}))

for i in var2:
	i[3]=i[2]/len(var)

aff = []
aff1 = []
aff2 = []
aff3 = []

for i in var2:
	aff += [i[0]]
	aff1 += [i[1]]
	aff2 += [i[2]]
	aff3 += [i[3]]	

print(pandas.DataFrame({'Entite nommee':aff,'Type':aff1,'Nombre d\'occurence':aff2,'Proportion dans le texte':aff3}))