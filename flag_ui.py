#!/usr/bin/python3

# flag_ui.py
# Gerben Timmerman & Stan Snijders

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from country import *
from flag_color import *
import sys

class ColorFlag(QtGui.QWidget):
	"""Class waar de constructor, Interface van Country in staan """
	
	
	def __init__(self):
		""" Constructor """
		super(ColorFlag, self).__init__()
		self.initUI()
	
	def initUI(self):
		""" User Interface """
		
		# Plaats en grootte van venster
		self.setGeometry(300,300,600,150)
		self.setWindowTitle('Vlag bepaler')
		self.show()
		
		label1 = QtGui.QLabel("Land:", self)
		label1.move(10,30)
		label1.show()
		
		label2 = QtGui.QLabel("Kleur flag:", self)
		label2.move(10,90)
		label2.show()
		
		# Landen Comboboxen tekenen in venster
		self.comboboxland = QtGui.QComboBox(self)
		self.comboboxland.setGeometry(55,30,250,40)
		self.comboboxland.show()
			
		# Ieder land toevoegen aan combobox
		countrylijst = getCountrylist()
		for countries in countrylijst:
			self.comboboxland.addItem(countries.country)
		self.comboboxland.currentIndexChanged.connect(self.updateUI)
		
		# QFrame waar de kleur in staat
		self.frame = QtGui.QFrame(self)
		self.frame.setGeometry(85,80,250,40)
		self.kleurobject = QtGui.QColor(0,0,0)
		self.frame.setStyleSheet("QFrame {background-color: %s}" % self.kleurobject.name())
		self.show()
		
		
	def updateUI(self):
		""" Kleur van flag aanpassen """
		nieuwland = self.comboboxland.currentText()
		countrylijst = getCountrylist()
		for landen in countrylijst:
			if (landen.country == nieuwland):
				self.frame.setStyleSheet("QFrame { background-color: %s }" % landen.vlag())
		

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	flag = ColorFlag()
	sys.exit(app.exec_())
