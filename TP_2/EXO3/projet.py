import xml.etree.ElementTree as ET
import pandas

tree = ET.parse('wsj_0010_sample.txt.disambiguated.xml')
root = tree.getroot()

temp = []

for child in root.iter('vertex'):
	temp3 = ''
	#temp3 += child.find('lemma').text + '_'
	for child2 in child.findall('lemma'):
		temp3 += child2.text + '_'
	for child2 in child.findall('micro'):
		if child2.text == 'SENT':
			temp3 += '.'
		elif child2.text == 'SCONJ':
			temp3 += 'CC'
		elif child2.text == 'COMMA':
			temp3 += ','
		elif child2.text == 'COLON':
			temp3 += ':'
		else:
			temp3 += child2.text
	temp += [temp3]

#print(pandas.DataFrame({'Temp':temp}))

for i in temp:
	print (i + ' ')