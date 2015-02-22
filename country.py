#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders


class Country():
	def __init__(self,country):
		self.country = country
				
	def __str__(self):
		countrynaam = ('Hello from {0}'.format(self.country))
		return countrynaam
		
def countryread():
	
	countrylijst = []
	bestand = open("countries_list.txt","r")
	for line in bestand:
		countrylijst.append(line)
	return countrylijst

def main():
	lijstlanden = countryread()
	for landen in lijstlanden:
		groet = Country(landen)
		print(groet)
		
if __name__ == '__main__':
	main()
