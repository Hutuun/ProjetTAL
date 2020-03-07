import sys
import os
import re
import lima-conll as convert

input = sys.argv[1];

output = sys.argv[2];

text = open(input, "r+");
content = text.read();
text.close()



lines = content.split("\n")

mots = []

for line in lines:

  mots += line.split(" ")

fout = open(output, "w+")

previous = ""

for word_tag in mots:

  print(word_tag)

  word_tagSplit = word_tag.split("\t")



  if(len(word_tagSplit) == 2):

    if(word_tagSplit[1] != "O"):

      en = ldc.convEnToEtiq(word_tagSplit[1])

      #verfier que l'entity est une sous entity

      if(previous == "B"):

        en = "I-" + en

        previous = "B"

      #La premiere entity

      else:

        en = "B-" + en

        previous = "B"

      print(en);

    else:

      en = word_tagSplit[1]

      previous =""

    fout.write(word_tagSplit[0] + "\t" + en + "\n");

fout.close();