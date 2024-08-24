from PyQt6 import QtWidgets, uic, QtCore, QtGui
from dice import roll, afterRoll
import os


class Ui_Dialog(QtWidgets.QDialog):
    """UI functions of Digital Dice"""

    def __init__(self) -> None:
        super(Ui_Dialog, self).__init__()

        uic.loadUi(os.path.join("GUI", "main.ui"), self)
        self.setWindowTitle("Digital Dice")

        self.numbers = [1, 2, 3, 4, 5, 6]

        self.player1Roll.clicked.connect(lambda: self.dice_roll(1))
        self.player2Roll.clicked.connect(lambda: self.dice_roll(2))
        self.player3Roll.clicked.connect(lambda: self.dice_roll(3))
        self.player4Roll.clicked.connect(lambda: self.dice_roll(4))

    def dice_roll(self, player):

        result = roll(self.numbers)
        print(result)
        after_roll_result = afterRoll(result)
        match player:
            case 1:
                self.listWidget.addItem(after_roll_result)
                self.listWidget.scrollToBottom()

            case 2:
                self.listWidget_2.addItem(after_roll_result)
                self.listWidget_2.scrollToBottom()

            case 3:
                self.listWidget_3.addItem(after_roll_result)
                self.listWidget_3.scrollToBottom()

            case 4:
                self.listWidget_4.addItem(after_roll_result)
                self.listWidget_4.scrollToBottom()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Dialog()
    window.show()
    app.exec()
