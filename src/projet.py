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

source = open("../data/pos_reference.txt.lima","r")
sortie = open("../data/pos_reference.txt.univ","w")

fctConv.convertisseur(source,sortie)