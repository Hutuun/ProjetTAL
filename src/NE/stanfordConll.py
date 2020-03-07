import sys
import os
import re
import limaConll as convert

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

  word_tagSplited = word_tag.split("\t")

  if(len(word_tagSplited) == 2):
    if(word_tagSplited[1] != "O"):
      en = convert.convEnToEtiq(word_tagSplited[1])
      if(previous == "B"):
        en = "I-" + en
        previous = "B"
      else:
        en = "B-" + en
        previous = "B"
      print(en);

    else:

      en = word_tagSplited[1]

      previous =""

    fout.write(word_tagSplited[0] + "\t" + en + "\n");

fout.close();