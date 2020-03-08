#Import des librairies

import numpy
import sklearn
import glob
import os
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas
import fonctionConvertisseur as fctConv
import fonctionRetabli as fctRet
import fonctionFormatage as fctForm
import fonctionFinalize as fctFin
import fonctionDecoupage as fctDec
import nltk
import NE.LimaNeFormatage as forma
import NE.limaConll as lico
import NE.stanfordConll as stco
import NE.Compte as staformat

print("Debut du programme")




print("Etape 1")

source = open("../data/POSTags_PTB_Universal_Linux.txt","r")
entree = open("../data/pos_reference.txt.lima","r")

sortie = "../data/pos_reference.txt.univ"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 1 finie")





print("Etape 2")

entree = open("../data/pos_reference.txt.univ","r")

sortie = "../data/pos_test.txt"

fctRet.retablissement(entree,sortie)

entree.close()

print("Etape 2 finie")






print("Etape 3")

entree = open("../data/eference.txt.conll","r")

sortie = "../data/est.txt"

fctRet.retablissement2(entree,sortie)

entree.close()

print("Etape 3 finie")






print("Etape 4")

source = open("../data/POSTags_PTB_Universal_Linux.txt","r")
entree = open("../data/pos_test.txt.pos.nltk","r")

sortie = "../data/pos_test.txt.pos.nltk.univ"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 4 finie")





print("Etape 5")

entree = open("../data/pos_test.txt.pos.stanford","r")

sortie = "../data/pos_test.txt.pos.stanford.univ"

fctForm.formatage(entree,sortie)

entree.close()

print("Etape 5 finie")






print("Etape 6")

source = open("../data/POSTags_PTB_Universal_Linux.txt","r")
entree = open("../data/pos_test.txt.pos.stanford.univ","r")

sortie = "../data/pos_test.txt.pos.stanford.univ"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 6 finie")





print("Etape 7")

source = open("../data/pos_reference.txt.univ","r")
entree = open("../data/pos_test.txt.pos.stanford.univ","r")

sortie = "../data/pos_test.txt.pos.stanford.univ2"
sortie2 = "../data/pos_reference.txt.univ2"

#fctFin.finalize(source,entree,sortie,sortie2)

source.close()
entree.close()

print("Etape 7 finie")





print("Etape 8")

source = open("../data/pos_reference.txt.univ","r")
entree = open("../data/pos_test.txt.pos.nltk.univ","r")

sortie = "../data/pos_test.txt.pos.nltk.univ2"
sortie2 = "../data/pos_reference.txt.univ3"

#fctFin.finalize(source,entree,sortie,sortie2)

source.close()
entree.close()

print("Etape 8 finie")



print("Etape 9")

entree = open("../data/pos_reference.txt.univ","r")

sortie = "../data/pos_reference.txt.univ"

fctDec.decoupe(entree,sortie)

entree.close()

print("Etape 9 finie")



print("Etape 10")

entree = open("../data/pos_reference.txt.univ","r")

sortie = "../data/pos_reference.txt.univ.stanford"

fctDec.decoupe2(entree,sortie)

entree.close()

print("Etape 10 finie")




print("Etape 11")

entree = open("../data/pos_test.txt.pos.stanford.univ","r")

sortie = "../data/pos_test.txt.pos.stanford.univ"

fctDec.decoupe6(entree,sortie)

entree.close()

print("Etape 11 finie")




print("Etape 12")

entree = open("../data/pos_reference.txt.univ.stanford","r")

sortie = "../data/pos_reference.txt.univ.stanford"

fctDec.decoupe3(entree,sortie)

entree.close()

print("Etape 12 finie")







entree = "../data/est.txt.lima"

sortie = "../data/est.txt.ne.lima";

forma.limaNEformat(entree,sortie)

entree = sortie;

sortie = "../data/est.txt.ne.lima.conll";

lico.limaCo(entree,sortie)

source = open("../data/ne_test.txt.ne.stanford.wrongformat","r")

temp = staformat.FonctionDecoupagePhrase1(source)

source.close()

entree = "../data/est.txt.ne.stanford";

fout = open(entree,"w")
fout.write(temp)
fout.close()



sortie = "../data/est.txt.ne.stanford.conll"

stco.stanfordCo(entree,sortie)

print("Etape 13")

entree = open("../data/est.txt.ne.nltk","r")

sortie = "../data/est.txt.ne.nltk.conll"

fctDec.decoupe4(entree,sortie)

entree.close()

print("Etape 13 finie")






print("Etape 14")

entree = open("../data/eference.txt.conll","r")

sortie = "../data/eference.txt.conll.final"

fctRet.retablissement3(entree,sortie)

entree.close()

print("Etape 14 finie")






print("Etape 15")

entree = open("../data/est.txt.ne.stanford.conll","r")

sortie = "../data/est.txt.ne.stanford.conll.final"

fctRet.retablissement3(entree,sortie)

entree.close()

print("Etape 15 finie")







print("Etape 16")

source = open("../data/PosTag_CONLL.txt","r")
entree = open("../data/est.txt.ne.nltk.bis","r")

sortie = "../data/est.txt.ne.nltk.bis.conll"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 16 finie")







print("Etape 17")

entree = open("../data/est.txt.ne.nltk.bis.conll","r")

sortie = "../data/est.txt.ne.nltk.bis.conll.final"

fctDec.decoupe5(entree,sortie)

entree.close()

print("Etape 17 finie")









print("Etape 18")

entree = open("../data/eference.txt.conll.final","r")

sortie = "../data/eference.txt.conll.final.nltk"

fctDec.decoupe5(entree,sortie)

entree.close()

print("Etape 18 finie")









print("Etape 19")

entree = open("../data/est.txt.ne.lima.conll","r")

sortie = "../data/est.txt.ne.lima.conll"

fctRet.retablissement4(entree,sortie)

entree.close()

print("Etape 19 finie")















print("Etape 20")

source = open("../data/PosTag_CONLL.txt","r")
entree = open("../data/est.txt.ne.lima.conll","r")

sortie = "../data/est.txt.ne.lima.conll"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 20 finie")

















print("Etape 21")

entree = open("../data/eference.txt.conll.final","r")

sortie = "../data/eference.txt.conll.final.lima"

fctRet.retablissement4(entree,sortie)

entree.close()

print("Etape 21 finie")


print("Fin du programme")