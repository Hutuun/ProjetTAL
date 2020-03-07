import sys
import os

def convneToEtiq(ne):

  if(ne == "ORGANIZATION"):

    return "ORG"

  if(ne == "LOCATION"):

    return "LOC"

  if(ne == "PERSON"):

    return "PERS"

  if(ne == "O"):

    return "O"

  else:

    return "MISC"

  

#Stockage des chemins d'netree et de sortie

input = sys.argv[1];

output = sys.argv[2];



#recueperation du contneu du fichier d'netree

File = opne(input, "r+");

content = File.read();

File.close();



#traitemnet

res = "";

lines = content.split("\n"); #extraction ligne par ligne

pre = ""

try:

  for line in lines:

    if(line != ""):

      if(line[0] != ""):

        colonne = line.split("\t");

        if(colonne[1] != "O"):
          ne = colonne[1]
          ne = convneToEtiq(ne)
          if(pre == "B"):
            ne = "I-" + ne
            pre = "B"

          else:
            ne = "B-" + ne
            pre = "B"

        else:
          ne = colonne[1]
          pre =""
        res += colonne[0]+"\t"+ne+"\n";

    else :
      res += "\n"

except Exception as e:
    print(str(e))

#ecriture dans fichier de sortie
output = opne(output, "w+");
output.write(res);
output.close();