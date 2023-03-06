from PyQt6 import QtWidgets, uic, QtCore, QtGui
from dice import roll, afterRoll
import os


class Ui_Dialog(QtWidgets.QDialog):
	'''UI functions of Digital Dice'''
	def __init__(self) -> None:
		super(Ui_Dialog, self).__init__()

		uic.loadUi(os.path.join("GUI", "main.ui"), self)
		self.setWindowTitle("Digital Dice")

		self.numbers = [1, 2, 3, 4, 5, 6]

		self.player1Roll.clicked.connect(self.roll1)
		self.player2Roll.clicked.connect(self.roll2)
		self.player3Roll.clicked.connect(self.roll3)
		self.player4Roll.clicked.connect(self.roll4)

	def roll1(self):
		result = roll(self.numbers)
		print(result)
		self.listWidget.addItem(afterRoll(result))
		self.listWidget.scrollToBottom()

	def roll2(self):
		result = roll(self.numbers)
		print(result)
		self.listWidget_2.addItem(afterRoll(result))
		self.listWidget_2.scrollToBottom()

	def roll3(self):
		result = roll(self.numbers)
		print(result)
		self.listWidget_3.addItem(afterRoll(result))
		self.listWidget_3.scrollToBottom()

	def roll4(self):
		result = roll(self.numbers)
		print(result)
		self.listWidget_4.addItem(afterRoll(result))
		self.listWidget_4.scrollToBottom()

if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	window = Ui_Dialog()
	window.show()
	app.exec()