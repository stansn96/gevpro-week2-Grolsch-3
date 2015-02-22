#!/usr/bin/python3

# Gerben Timmerman en Stan Snijders
# flag_color.py

from PyQt4 import QtCore, QtGui

class FlagColor():
	"""Class waarin de kleur wordt bepaald """
	
	def __init__(self):
		""" Constructor """
		super(QtGui.QColor, self).__init__()
		self.kleur()
		
	def kleur(self):
		green = randrange(0,257)
		red = randrange(0,257)
		blue = randrange(0,257)
		self.setGreen(green)
		self.setRed(red)
		self.setBlue(blue)


def main():
	app = QtGui.QApplication(sys.argv)
	color = FlagColor()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
