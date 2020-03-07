import sys
import os

def convEnToEtiq(ne):

	if(ne == "ORGANIZATION"):

		return "ORG"

	if(ne == "LOCATION"):

		return "LOC"

	if(ne == "PERSON"):

		return "PERS"

	if(ne == "O"):

		return "O"

	else:

		return "MISC"
