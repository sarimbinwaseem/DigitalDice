import os
from PyQt6 import QtWidgets, uic
from dice import roll, afterRoll


class Ui_Dialog(QtWidgets.QDialog):
	"""UI functions of Digital Dice"""

	def __init__(self) -> None:
		super(Ui_Dialog, self).__init__()

		uic.loadUi(os.path.join("GUI", "main.ui"), self)
		self.setWindowTitle("Digital Dice")

		self.numbers = [1, 2, 3, 4, 5, 6]

		self.player1Roll.clicked.connect(lambda: self.main_roll(self.listWidget))
		self.player2Roll.clicked.connect(lambda: self.main_roll(self.listWidget_2))
		self.player3Roll.clicked.connect(lambda: self.main_roll(self.listWidget_3))
		self.player4Roll.clicked.connect(lambda: self.main_roll(self.listWidget_4))

	def main_roll(self, listWidget) -> list:
		"""Rolls and update the list widget with new entry"""

		result = roll(self.numbers)
		print(result)

		listWidget.addItem(afterRoll(result))
		listWidget.scrollToBottom()


if __name__ == "__main__":
	import sys

	app = QtWidgets.QApplication(sys.argv)
	window = Ui_Dialog()
	window.show()
	app.exec()
