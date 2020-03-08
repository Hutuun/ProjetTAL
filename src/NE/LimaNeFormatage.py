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

				lineColumn = line.split("\t");


				if(len(lineColumn[9].split(".")) > 1):

					en = lineColumn[9].split(".")[1].split("|")[0];

				else:

					en = "O";

			  

				res += lineColumn[1] + "\t" + en + "\n";

			#print(res)

			'''else:

				res += "\n";'''

except Exception as e:

    print(str(e))



#ecriture dans fichier de sortie

fout = open("../../data/est.txt.ne.lima", "w+");

fout.write(res);

fout.close();