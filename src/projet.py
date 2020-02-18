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
import nltk

print("Debut du programme")

print("Etape 1")

source = open("..\data\POSTags_PTB_Universal_Linux.txt","r")
entree = open("..\data\pos_reference.txt.lima","r")

sortie = "..\data\pos_reference.txt.univ"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 1 finie")

print("Etape 2")

entree = open("..\data\pos_reference.txt.univ","r")

sortie = "..\data\pos_test.txt"

fctRet.retablissement(entree,sortie)

entree.close()

print("Etape 2 finie")

print("Etape 3")

entree = open("..\data\eference.txt.conll","r")

sortie = "..\data\est.txt"

fctRet.retablissement(entree,sortie)

entree.close()

print("Etape 3 finie")

print("Etape 4")

source = open("..\data\POSTags_PTB_Universal_Linux.txt","r")
entree = open("..\data\pos_reference.txt.nltk","r")

sortie = "..\data\pos_reference.txt.univ.nltk"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 4 finie")

print("Etape 5")

entree = open("..\data\pos_reference.txt.stanford","r")

sortie = "..\data\pos_reference.txt.univ.stanford"

fctForm.formatage(entree,sortie)

entree.close()

print("Etape 5 finie")

print("Etape 6")

source = open("..\data\POSTags_PTB_Universal_Linux.txt","r")
entree = open("..\data\pos_reference.txt.univ.stanford","r")

sortie = "..\data\pos_reference.txt.univ.stanford"

fctConv.convertisseur(source,entree,sortie)

source.close()
entree.close()

print("Etape 6 finie")

print("Fin du programme")