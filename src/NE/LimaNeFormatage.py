import sys

import os


text = open("../../data/est.txt.lima", "r+");

content = text.read();

text.close();


res = "";

lines = content.split("\n"); #extraction ligne par ligne

try:

	for line in lines:


		if(line != ""):

		  #si ligne non vide

			if(line[0] != "#"):

				colonne = line.split("\t");


				if(len(colonne[9].split(".")) > 1):

					en = colonne[9].split(".")[1].split("|")[0];

				else:

					en = "O";

				print(colonne[1])
				if(colonne[1] != " "):
					res += colonne[1] + "\t" + en + "\n";
				else:
					res += "\n";

			#print(res)

			'''else:

				res += "\n";'''

except Exception as e:

    print(str(e))



#ecriture dans fichier de sortie

fout = open("../../data/est.txt.ne.lima", "w+");

fout.write(res);

fout.close();