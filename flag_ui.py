#!/usr/bin/python3

# flag_ui.py
# Gerben Timmerman

from PyQt4 import QtCore, QtGui
from country import *
import sys

class ColorFlag(QtGui.QWidget):
	"""Class waar de constructor, Interface van Country in staan """
	
	
	def __init__(self):
		""" Constructor """
		super(ColorFlag, self).__init__()
		self.initUI()
	
		
	def initUI(self):
		""" User Interface """
		
		# Plaats en groote van venster
		self.setGeometry(300,300,600,150)
		self.setWindowTitle('Valuta converter')
		self.show()
		
		# Labels die van, naar weerwegen in het venster
		label1 = QtGui.QLabel("Land:", self)
		label1.move(10,30)
		label1.show()
		
		label2 = QtGui.QLabel("Kleur flag:", self)
		label2.move(10,90)
		label2.show()
		
		# Valuta Comboboxen tekenen in venster
		self.comboboxland = QtGui.QComboBox(self)
		self.comboboxland.setGeometry(55,30,250,30)
		self.comboboxland.show()
		
		
		# Ieder land toevoegen aan combobox
		landen = countryread()
		self.comboboxland.addItems(landen)
		
		
		# QFrame waar de kleur in staat
		self.frame = QtGui.QFrame(self)
		self.kleurobject = QtGui.QColor(0,0,0)
		self.frame.setStyleSheet("QFrame {background-color: %s}" % self.kleurobject.name())
		
		
		#Het aanpassen van de Boxen roep functie updateUI aan
		self.comboboxland.currentIndexChanged.connect(self.updateUI)
		
	def updateUI(self):
		""" Kleur van flag aanpassen """
		self.kleurobject = flag_color.FlagColor.Kleur(self.kleurobject)
		self.frame.setStyleSheet("QFrame {background-color: %s}" % self.kleurobject.name())
		
		
def main():
	app = QtGui.QApplication(sys.argv)
	flag = ColorFlag()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
