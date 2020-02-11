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
import nltk

source = open("../data/POSTags_PTB_Universal_Linux.txt","r")
entree = open("../data/pos_reference.txt.lima","w")

fctConv.convertisseur(source,entree)