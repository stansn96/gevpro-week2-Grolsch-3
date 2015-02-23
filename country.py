#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders

from PyQt4 import QtCore, QtGui
from flag_color import *

class Country:
	
	def __init__(self, country, vlag):
		self.country = country
		self.vlag = vlag

	def vlag(self):
		return self.vlag
	
	def __str__(self):
		return self

		
def getCountrylist():
	
	countrylijst = []
	bestand = open("countries_list.txt","r")
	for line in bestand:
		land = line.strip()
		vlag = FlagColor(land)
		result = Country(land, vlag)
		countrylijst.append(result)
	return countrylijst
		
if __name__ == '__main__':
	getCountrylist()
