#!/usr/bin/python
# -*- coding: utf-8 -*-

###########
# Programme permettant d'harmoniser la sortie du POS Tagger avec la référence
# Usage : python alignPOSTaggerOutputWithReference.py nom_fichier.pos.universal.reference.firstcolumn nom_fichier.stanford.universal.pos.firstcolumn nom_fichier.pos.universal.reference nom_fichier.stanford.universal.pos
###########

import sys
from difflib import ndiff
from os.path import basename
FILE=[]
LINE=[]
if len(sys.argv) < 2: 
    print "Usage:"
    print sys.argv
    print "./Extract_Tain.py Corpus_1 ..."
    exit(1)
else :
  for fichier in sys.argv:
    FILE.append (open(fichier, 'r')) 
  FILE[0].close()
  FILE.pop(0)  

txt = [None] * len(FILE) 

for i in range(len(FILE)):
  txt[i]=FILE[i].readlines() 
for i in range(len(FILE)): 
  if (i!=0) :
    min_size=min(len(txt[i]),len(txt[i-1]),min_size)
  else :
    min_size=len(txt[0])


Out_File = [None] * ((len(FILE)/2)+1)
for i in range(len(Out_File)):
  Out_File[i]=open(basename(sys.argv[i+(len(FILE)/2)])+".Filter", 'w')

Indice = [0] * ((len(FILE)/2))
Indice_Old = [0] * ((len(FILE)/2))
K=0 

for i in range(len(txt[0])):
    for j in range((len(txt)/2)-1):
         test=0
         Indice[0]=i
         Decalage = max(len(txt[0]),len(txt[j+1]))-min(len(txt[0]),len(txt[j+1]))	/ 2				
         for k in range(max(0,i-Decalage), min(i+Decalage,len(txt[j+1]))):
            if txt[0][i] in txt[j+1][k] and len(txt[0][i])==len(txt[j+1][k]):              
              Indice[j+1] = k
              test=1
              break 
         if test==0:
           break
    if test==1:
      for l in range(len(Out_File)-1):#for l in range(len(Out_File)-1):                          
        
        #Out_File[l+1].write(txt[l+(len(FILE)/2)][Indice[l]])
        if l==0:
          print "if",l,Indice,i, test 
          Out_File[l].write(txt[l][i])        

          Out_File[l+1].write(txt[l+(len(FILE)/2)][Indice[l]])                        

        else: 
          print "else",l,Indice,i, test 
          Out_File[l+1].write(txt[l+(len(FILE)/2)][Indice[l]])

    else : continue
for i in range(len(FILE)):
  FILE[i].close()

for i in range(len(Out_File)):
  Out_File[i].close()







     










