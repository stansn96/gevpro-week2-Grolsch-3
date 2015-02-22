#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders

from PyQt4 import QtCore, QtGui
from flag_color import *

class Country():
	
	def __init__(self,country):
		self.country = country
				
	def __str__(self):
		countrynaam = self.country
		
	def flagcolor(self):
		
		
def countryread():
	
	countrylijst = []
	bestand = open("countries_list.txt","r")
	for line in bestand:
		countrylijst.append(line)
	return countrylijst

def main():
	lijstlanden = countryread()
	for landen in lijstlanden:
		result = Country(landen)
		print(result)
		
if __name__ == '__main__':
	main()
