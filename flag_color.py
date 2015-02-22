#!/usr/bin/python3

<<<<<<< HEAD
# Gerben Timmerman
# flag_color.py

from PyQt4 import QtCore, QtGui
from random import randrange
=======
# Gerben Timmerman en Stan Snijders
# flag_color.py

from PyQt4 import QtCore, QtGui
>>>>>>> 25dbb6922f7f2c0da58e7e4a61ccf52eb44e0ca1

class FlagColor(QtGui.QColor):
	"""Class waarin de kleur wordt bepaald """
	
	def __init__(self, land):
		""" Constructor """
		super(FlagColor, self).__init__()
		self.kleur()
		
	def initUI(self):
		self.land = land
		self.kleur = self.Kleur()
		
	def Kleur(self):
		self.setGreen(randrange(256))
		self.setRed(randrange(256)
		self.setBlue(randrange(256)
		
		return self


def main():
	app = QtGui.QApplication(sys.argv)
	color = FlagColor()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
