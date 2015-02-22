#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders

from PyQt4 import QtCore, QtGui
from flag_color import *

class Country():
	
	def __init__(self,country,vlag):
		self.country = country
				
	def name(self):
		countrynaam = self.country
		
	def flagcolor(self):
		self.vlag = vlag
		
	def __str__(self):
		return self
		
def countryread():
	
	countrylijst = []
	bestand = open("countries_list.txt","r")
	for line in bestand:
		countrylijst.append(line)
	return countrylijst

def main():
	lijstlanden = countryread()
	for landen in lijstlanden:
		flagcolor = FlagColor(landen)
		result = Country(landen, flagcolor)
		
if __name__ == '__main__':
	main()
