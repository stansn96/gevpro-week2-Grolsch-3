#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders

from PyQt4 import QtCore, QtGui
from flag_color import *

class Country():
	
	def __init__(self, country, vlag):
		self.country = country
				
	def name(self):
		return self.name

		
	def vlag(self):
		return self.vlag
		
	def __str__(self):
		return self

		
def getCountrylist():
	
	countrylijst = []
	bestand = open("countries_list.txt","r")
	for line in bestand:
		landen = line.strip()
		vlag = FlagColor(landen)
		result = Country(landen, vlag)
		countrylijst.append(result)
	return countrylijst

		
if __name__ == '__main__':
	getCountrylist()
