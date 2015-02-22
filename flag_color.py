#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders
# flag_color.py

from PyQt4 import QtCore, QtGui

class FlagColor(QtGui.QColor):
	"""Class waarin de kleur wordt bepaald """
	
	def __init__(self, land):
		""" Constructor """
		super(FlagColor, self).__init__()
		
	def initUI(self):
		self.land = land
		self.kleur = self.Kleur()
		
	def Kleur(self):
		green = randrange(256)
		red = randrange(256)
		blue = randrange(256)
		
		return self


def main():
	app = QtGui.QApplication(sys.argv)
	color = FlagColor()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
