# ProjetTAL

Afin de lancer le projet, il est necessaire d'installer toutes les librairies ci-dessous : 



pandas

sklearn

numpy 

glob

os

matplotlib

Pour générer les fichier à partir des fichiers .txt de référence il faut faire :

- Aller dans le dossier data

- Pour lima: analyzeText -l eng -p main ne_test.txt > ne_test.txt.lima

- Pour stanford : java -mx600m -cp stanford-ner-2018-10-16/stanford-ner.jar:lib/* edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier stanford-ner-2018-10-16/classifiers/english.all.3class.distsim.crf.ser.gz -textFile ne_test.txt > ne_test.txt.ne.stanford.wrongformat 



Dans l'invité de commande, rendez vous dans le dossier src apres avoir genere tous les fichiers à traiter et les avoir nommes correctement (Les noms sont importants).

Excutez ensuite la ligne suivante (Attention, il est obligatoire d'utiliser python 3.7):



python projet.py 



Vous aurez un ensemble d'affichage correspondant à la progression dans l'execution.

Une fois ceci fait, deplacez vous jusque dans le dossier data

Entrez ensuite les lignes de commande suivantes et vous obtiendrez les resultats (Attention, il est obligatoire d'utiliser python 2.7):



python evaluate.py eference.txt.conll est.txt.ne.lima.conll



python evaluate.py eference.txt.conll.final.nltk est.txt.ne.nltk.bis.conll.final



python evaluate.py eference.txt.conll.final est.txt.ne.stanford.conll.final



python evaluate.py pos_reference.txt.univ.stanford pos_test.txt.pos.stanford.univ



python evaluate.py pos_reference.txt.univ pos_test.txt.pos.nltk.univ
