import os
import sys
from PyQt6 import QtWidgets, uic

from dice import roll, afterRoll


class DigitalDice(QtWidgets.QDialog):
    """UI functions of Digital Dice"""

    def __init__(self) -> None:
        super().__init__()

        uic.loadUi(os.path.join("GUI", "main.ui"), self)
        self.setWindowTitle("Digital Dice")

        self.numbers = [1, 2, 3, 4, 5, 6]

        self.list_widgets = (
            self.listWidget,
            self.listWidget_2,
            self.listWidget_3,
            self.listWidget_4,
        )

        self.player_1_roll.clicked.connect(lambda: self.dice_roll(1))
        self.player_2_roll.clicked.connect(lambda: self.dice_roll(2))
        self.player_3_roll.clicked.connect(lambda: self.dice_roll(3))
        self.player_4_roll.clicked.connect(lambda: self.dice_roll(4))

    def dice_roll(self, player):

        result = roll(self.numbers)
        print(result)
        after_roll_result = afterRoll(result)

        self.list_widgets[player - 1].addItem(after_roll_result)
        self.list_widgets[player - 1].scrollToBottom()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    window = DigitalDice()
    window.show()
    app.exec()
