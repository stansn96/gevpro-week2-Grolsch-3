#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders
# flag_color.py

from PyQt4 import QtCore, QtGui
from random import randrange

class FlagColor(QtGui.QColor):
	"""Class waarin de kleur wordt bepaald """
	
	def __init__(self, land):
		""" Constructor """
		super(FlagColor, self).__init__()
		
	def initUI(self):
		self.land = land
		self.kleur = self.Kleur()
		
	def Kleur(self):
		self.setGreen(randrange(256))
		self.setRed(randrange(256))
		self.setBlue(randrange(256))
		
		return self


def main():
	app = QtGui.QApplication(sys.argv)
	color = FlagColor()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
