#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders

from PyQt4 import QtCore, QtGui
from flag_color import *

class Country():
	
	def __init__(self,country,vlag):
		self.country = country
		self.vlag = vlag
		
	def vlag(self):
		self.vlag = vlag
		
	def __str__(self):
		return self
		
def getCountrylist():
	
	countrylijst = []
	bestand = open("countries_list.txt","r")
	for line in bestand:
		landen = line.strip()
		flagcolor = FlagColor(landen)
		result = Country(landen, flagcolor)
		countrylijst.append(result)
	return countrylijst

		
if __name__ == '__main__':
	getCountrylist()
