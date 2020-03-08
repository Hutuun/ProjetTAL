def convEnToEtiq(ne):

	if(ne == "ORGANIZATION"):

		return "ORG"

	if(ne == "LOCATION"):

		return "LOC"

	if(ne == "PERSON"):

		return "PERS"

	if(ne == "O"):

		return "O"
	if(ne == ""):
		return ""
	else:

		return "MISC"