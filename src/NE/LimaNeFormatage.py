import sys

import os


def limaNEformat(input,output):

	text = open(input, "r+");

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

					# print(colonne[1])
					if(colonne[1] != " "):
						res += colonne[1] + "\t" + en + "\n";
					else:
						res += "\n";

				#print(res)


	except Exception as e:

		print(str(e))



	#ecriture dans fichier de sortie

	fout = open(output, "w+");

	fout.write(res);

	fout.close();