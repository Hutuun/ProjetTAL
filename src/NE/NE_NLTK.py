import nltk

from nltk.corpus import state_union

from nltk.tokenize import PunktSentenceTokenizer

from nltk import pos_tag

from nltk.tokenize import word_tokenize

from nltk import RegexpParser

import sys


# Pour installer toute les lib NLTK sudo python -m nltk.downloader -d /usr/local/share/nltk_data all


#Telechargement des packages

nltk.download('punkt');

nltk.download('averaged_perceptron_tagger');

nltk.download('maxent_ne_chunker');

nltk.download('words');


input = sys.argv[1];

output = sys.argv[2]


text = open(input, "r+");

content = text.read();

text.close();



tokenizer = PunktSentenceTokenizer();

tokens = tokenizer.tokenize(content);



mots = []

tagged = []

Entity = []


for sentence in tokens:

  mots += nltk.word_tokenize(sentence)

  tagged = nltk.pos_tag(mots)

  #Named Entity Recognition

  Entity = nltk.ne_chunk(tagged);

print("Entitée nommée:",Entity);

Fout = open(output, "w");

for token in Entity:

  if(type(token[0]) != type("string")):

    print(token)

    for parts in token:

      Fout.write(parts[0] + "\t" + parts[1] + "\t")

    Fout.write("\n");

  else:

    Fout.write(token[0] + "\t" + token[1] + "\n");

Fout.close();