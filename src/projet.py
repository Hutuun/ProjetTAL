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
import nltk

print("Debut du programme")

print("Etape 1")

source = open("..\data\POSTags_PTB_Universal_Linux.txt","r")
entree = open("..\data\pos_reference.txt.lima","r")

sortie = "..\data\pos_reference.txt.univ"

fctConv.convertisseur(source,entree,sortie)

print("Etape 1 finie")

print("Etape 2")

entree = open("..\data\pos_reference.txt.univ","r")

sortie = "..\data\pos_test.txt"

fctRet.retablissement(entree,sortie)

print("Etape 2 finie")

print("Etape 3")

entree = open("..\data\ne_reference.txt.conll","r")

sortie = "..\data\ne_test.txt"

fctRet.retablissement(entree,sortie)

print("Etape 3 finie")

print("Fin du programme")