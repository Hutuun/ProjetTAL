#! /usr/bin/perl -s

###########
# Programme permettant d'extraire la première colonne de la sortie d'un POS Tagger sous le format (toke "\n" tag)
# Usage : perl extractUTF8FirstColumnOfPOSTaggerOutput.pl fichierSource fichierCible
###########

open(SOURCE,"<:utf8", "$ARGV[0]") || die ("Impossible d'ouvrir le fichier source $ARGV[0]");
open(CIBLE,">:utf8", "$ARGV[1]") || die ("Impossible d'ouvrir le fichier cible $ARGV[1]");

# Numéro de la premiere ligne
my $i=0;

# print "\n";

while (my $ligne = <SOURCE>)
{
	# print $ligne;
	chomp($ligne);
	# print "\n";
	
	# Copie du contenu de la ligne
	$ligneCopy = $ligne;

	# Tableau contenant la ligne lue composée de deux éléments séparés par le symbole #
	@tokensArray = split(/#/, $ligne);
	
	# Numéro du token et du POS tag
	$numberTPOS = $i+1;
	
	# Premier élément du tableau des tokens
	$tokenFirstElement=@tokensArray[0];
		
	print CIBLE ("$tokenFirstElement");
	print CIBLE ("\n");
	
	$i++;
}

print "Nombre de lignes lues du fichier source = $i\n";

close SOURCE;
close CIBLE;