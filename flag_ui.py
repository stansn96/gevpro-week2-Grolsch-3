#!/usr/bin/python3


# flag_ui.py
# Gerben Timmerman & Stan Snijders

# !!!! We hebben geprobeerd de landen te koppelen aan kleuren, maar kwamen niet uit
# hoe we die waardes moesten vasthouden en weer moesten gebruiken. Daarom hebben we
# een werkend programma afgeleverd die als je een land kiest, 3 random kleuren bij dat
# land laat zien voor de vlag. !!!!


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
		self.setGeometry(300,300,600,250)
		self.setWindowTitle('Vlag bepaler')
		self.show()
		label1 = QtGui.QLabel("Land:", self)
		label1.move(10,30)
		label1.show()
		label2 = QtGui.QLabel("Kleur flag:", self)
		label2.move(10,90)
		label2.show()
		
		# Landen Combobox tekenen in venster
		self.comboboxland = QtGui.QComboBox(self)
		self.comboboxland.setGeometry(55,30,250,40)
		self.comboboxland.show()
		
		# Ieder land toevoegen aan combobox
		countrylijst = getCountrylist()
		for countries in countrylijst:
			self.comboboxland.addItem(countries.country)
		self.comboboxland.currentIndexChanged.connect(self.updateUI)
		
		# QFrames waar de kleuren in staan
		self.frame = QtGui.QFrame(self)
		self.frame.setGeometry(85,80,250,30)
		self.kleurobject1 = QtGui.QColor(randrange(256),randrange(256),randrange(256))
		self.frame.setStyleSheet("QFrame {background-color: %s}" % self.kleurobject1.name())
		self.frame.show()
		
		self.frame2 = QtGui.QFrame(self)
		self.frame2.setGeometry(85,110,250,30)
		self.kleurobject2 = QtGui.QColor(randrange(256),randrange(256),randrange(256))
		self.frame2.setStyleSheet("QFrame {background-color: %s}" % self.kleurobject2.name())
		self.frame2.show()
		
		self.frame3 = QtGui.QFrame(self)
		self.frame3.setGeometry(85,140,250,30)
		self.kleurobject3 = QtGui.QColor(randrange(256),randrange(256),randrange(256))
		self.frame3.setStyleSheet("QFrame {background-color: %s}" % self.kleurobject3.name())
		self.frame3.show()
		
		
	def updateUI(self):
		""" Kleur van flag aanpassen """
		nieuwland = self.comboboxland.currentText()
		countrylijst = getCountrylist()
		self.kleurobject1 = QtGui.QColor(randrange(256),randrange(256),randrange(256))
		self.kleurobject2 = QtGui.QColor(randrange(256),randrange(256),randrange(256))
		self.kleurobject3 = QtGui.QColor(randrange(256),randrange(256),randrange(256))
		self.frame.setStyleSheet("QFrame { background-color: %s }" % self.kleurobject1.name())
		self.frame2.setStyleSheet("QFrame { background-color: %s }" % self.kleurobject2.name())
		self.frame3.setStyleSheet("QFrame { background-color: %s }" % self.kleurobject3.name())
		
		# We wilden ervoor zorgen dat hij de waarde bij iederland vast hield maar dat is ons niet gelukt
		"""for landen in countrylijst:
			if (landen.country == nieuwland):
				self.frame.setStyleSheet("QFrame { background-color: %s }" % self.kleurobject.name())"""

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	flag = ColorFlag()
	sys.exit(app.exec_())
