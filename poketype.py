#poketype.py
import re
import sets
import webbrowser, sys
import string
import lxml.html
import httplib
import urlparse
from lxml import etree

typedict = {
	'normal':0,'fighting':1,'flying':2,'poison':3,'ground':4,'rock':5,'bug':6,'ghost':7,'steel':8,'fire':9,'water':10,'grass':11,'electric':12,'psychic':13,'ice':14,'dragon':15,'dark':16,'fairy':17,
	0:'normal', 1:'fighting', 2:'flying', 3:'poison', 4:'ground', 5:'rock', 6:'bug', 7:'ghost', 8:'steel', 9:'fire', 10:'water', 11:'grass', 12:'electric', 13:'psychic', 14:'ice', 15:'dragon', 16:'dark', 17:'fairy'}

weakto = {
	'normal': ['fighting'],
	'fighting': ['flying','psychic'],
	'flying': ['electric','ice','rock'],
	'poison': ['bug','ground','psychic'],
	'ground': ['ice','grass','water'],
	'rock': ['fighting','grass','ground','steel','water'],
	'bug': ['fire','flying','rock'],
	'ghost': ['dark','ghost'],
	'steel': ['fighting','fire','ground'],
	'fire': ['ground','rock','water'],
	'water': ['electric','grass'],
	'grass': ['bug','fire','flying','ice','poison'],
	'electric': ['ground'],
	'psychic': ['bug','dark','ghost'],
	'ice': ['fighting','fire','rock','steel'],
	'dragon': ['dragon','fairy','ice'],
	'dark': ['bug','fairy','fighting'],
	'fairy': ['poison','steel']
}

notweakto = {
	'normal': [],
	'fighting': ['bug','dark','rock'],
	'flying': ['bug','fighting','grass'],
	'poison': ['bug','fairy','fighting','grass','poison'],
	'ground': ['poison','rock'],
	'rock': ['fire','flying','normal','poison'],
	'bug': ['fighting','grass','ground'],
	'ghost': ['bug','poison'],
	'steel': ['bug','dragon','fairy','flying','grass','ice','normal','psychic','rock','steel'],
	'fire': ['bug','fairy','fire','grass','ice','steel'],
	'water': ['fire','ice','steel','water'],
	'grass': ['electric','grass','ground','water'],
	'electric': ['electric','flying','steel'],
	'psychic': ['fighting','psychic'],
	'ice': ['ice'],
	'dragon': ['electric','fire','grass','water'],
	'dark': ['dark','ghost'],
	'fairy': ['bug','dark','fighting']
}

immuneto = {
	'normal': ['ghost'],
	'fighting': [],
	'flying': ['ground'],
	'poison': [],
	'ground': ['electric'],
	'rock': [],
	'bug': [],
	'ghost': ['fighting','normal'],
	'steel': ['poison'],
	'fire': [],
	'water': [],
	'grass': [],
	'electric': [],
	'psychic': [],
	'ice': [],
	'dragon': [],
	'dark': ['psychic'],
	'fairy': ['dragon']
}

strongto = {
	'normal': [],
	'fighting': ['dark','ice','normal','rock','steel'],
	'flying': ['bug','fighting','grass'],
	'poison': ['fairy','grass'],
	'ground': ['electric','fire','poison','rock','steel'],
	'rock': ['bug','fire','flying','ice'],
	'bug': ['dark','grass','psychic'],
	'ghost': ['ghost','psychic'],
	'steel': ['fairy','ice','rock'],
	'fire': ['bug','grass','ice','steel'],
	'water': ['fire','ground','rock'],
	'grass': ['ground','rock','water'],
	'electric': ['flying','water'],
	'psychic': ['fighting','poison'],
	'ice': ['dragon','flying','grass','ground'],
	'dragon': ['dragon'],
	'dark': ['ghost','psychic'],
	'fairy': ['dark','dragon','fighting']
}

if sys.argv[1] == "weak":
	t1w = weakto[sys.argv[2]]
	t1s = strongto[sys.argv[2]]
	t1i = immuneto[sys.argv[2]]
	t1d = notweakto[sys.argv[2]]
	if len(sys.argv) >3:
		t2w = weakto[sys.argv[3]]
		t2s = strongto[sys.argv[3]]
		t2i = immuneto[sys.argv[3]]
		t2d = notweakto[sys.argv[3]]

		t1 = set(t1w).difference(set(t2d))
		t2 = set(t2w).difference(set(t1d))
		if not(t1i == []) or not(t2i == []):
			immune = set(t2i).union(set(t1i))
			t1 = set(t1).difference(set(immune))
			t2 = set(t2).difference(set(immune))
			print "Immune to: " + str(immune)
		print "Weak x2: " + str(set(t2).symmetric_difference(set(t1)))
		if not len(set(t2).intersection(set(t1))) == 0:
			print "Weak x4: " + str(set(t2).intersection(set(t1)))
	else:
		if not(t1i == []):
			print "Immune to: " + str(t1i)
		print "Weak x2: " + str(t1w)


	if len(sys.argv) >3:

		t1d = set(t1d).difference(set(t2w))
		t2d = set(t2d).difference(set(t1w))
		if not(t1i == []) or not(t2i == []):
			t1d = set(t1d).difference(set(immune))
			t2d = set(t2d).difference(set(immune))
		print "NVE x1/2: " + str(set(t2d).symmetric_difference(set(t1d)))
		if not len(set(t2).intersection(set(t1))) == 0:
			print "NVE x1/4: " + str(set(t2d).intersection(set(t1d)))
	else:
		print "NVE x1/2: " + str(t1d)


if sys.argv[1] == "strong":
	t1 = strongto[sys.argv[2]]

	if len(sys.argv) >3:
		t2 = strongto[sys.argv[3]]
		print "Strong x2: " + str(set(t2).difference(set(t1))) + "\nStrong x4: " + str(set(t2).intersection(set(t1)))
	else:
		print "Strong x2: " + str(t1)