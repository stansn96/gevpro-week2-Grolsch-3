#!/usr/bin/python3

# Gerben Timmerman


class Country():
	def __init__(self,country):
		self.country = country
				
	def __str__(self):
		countrynaam = ('Hello from {0}'.format(self.country))
		return countrynaam
		


def main():
	lijstlanden = []
	ob1, ob2 = "The Netherlands", "Germany"
	lijstlanden.append(ob1)
	lijstlanden.append(ob2)
	for landen in lijstlanden:
		groet = Country(landen)
		print(groet)
		
if __name__ == '__main__':
	main()
