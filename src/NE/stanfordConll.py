import sys
import os
import re
import convEnToEtiq as convert


#input = sys.argv[1];

#output = sys.argv[2];

input = "../../data/ne_test.txt.ne.stanford"

output = "../../data/ne_test.txt.ne.stanford.conll"




text = open(input, "r+");

content = text.read();

#lines = []

#for i in text:
#	lines += [i]

text.close();


#traitement

res = "";

lines = content.split("\n"); #extraction ligne par ligne

previous = ""

#print(lines)

try:
	n=0;
	for line in lines:
		colonne = line.split();
		if(len(colonne)!=0):

		  #si ligne non vide
			# print(len(line))
			if(line[0] != ""):

			#si pas ligne de commentaire
			
			#extraction du mot et de son entity nomme

				# print(colonne)

			  #print(colonne[9].split("."))

				if(colonne[1] != "O"):

					en = colonne[1]
					en = convert.convEnToEtiq(en)

			  #verfier que l'entity est une sous entity

					if(previous == "B"):

						en = "I-" + en

						previous = "B"

				  #La premiere entity

					else:
						if(colonne[0] != ""):
							en = "B-" + en

							previous = "B"

					# print(en);

				else:
					if(colonne[1] == "O"):
						en = colonne[1]

						previous =""
					else:
						en = ""
						previous=""
			else:
				n = n+1
				print(n)

			res += colonne[0] + "\t" + en + "\n";

			# print(res)

		else :
			print("couc")
			res += "\n"

except Exception as e:

    print(str(e))
	



#ecriture dans fichier de sortie

outputFile = open(output, "w");

# print(res)

outputFile.write(res);

outputFile.close();