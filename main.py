import sys
import random
from PyQt5 import QtWidgets , QtGui , QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from NumberGuessing import Ui_MainWindowNumberGuessing

class UiNumberGuessingForm(QMainWindow):
    counter = 0
    const = 0

    def __init__(self):
        QMainWindow.__init__(self)

        self.uinumberguessingform = Ui_MainWindowNumberGuessing()
        self.uinumberguessingform.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.uinumberguessingform.help_btn.clicked.connect(self.help)
        self.btnchecked()
        self.btnreset()

        self.show()


    def mousePressEvent(self, evt):
        self.oldpos = evt.globalPos()


    def mouseMoveEvent(self, evt) :
        delta = QPoint(evt.globalPos() - self.oldpos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldpos = evt.globalPos()

    def btnchecked(self):
        self.uinumberguessingform.check.clicked.connect(self.checked)

    def btnreset(self):
        self.uinumberguessingform.reset.clicked.connect(self.reset)

    def random(self):
        if self.const == 0:
            self.start = int(self.uinumberguessingform.start.text())
            self.stop = int(self.uinumberguessingform.stop.text())
            self.randomnumber = random.randint(self.start, self.stop)

            self.const += 1


    def checked(self):

        self.chances = int(self.uinumberguessingform.chances.text())
        if self.const == 0:
            self.start = int(self.uinumberguessingform.start.text())
            self.stop = int(self.uinumberguessingform.stop.text())
            self.randomnumber = random.randint(self.start, self.stop)

            self.const += 1

        self.counter += 1

        self.guessnumber = int(self.uinumberguessingform.yourguess.text())

        print(self.randomnumber)

        if self.counter <= self.chances:


            if self.guessnumber > self.randomnumber:
                self.uinumberguessingform.Suggestioandresult.setText("Go Down")

            elif self.guessnumber < self.randomnumber:
                self.uinumberguessingform.Suggestioandresult.setText("Go Up")

            elif self.guessnumber == self.randomnumber:
                self.uinumberguessingform.Suggestioandresult.setText("You Did it Well done !")

        elif self.counter > self.chances:
            self.uinumberguessingform.Suggestioandresult.setText(f"You lost, you losser ")

    def reset(self):

        self.const -= 1
        self.uinumberguessingform.chances.setText("")
        self.uinumberguessingform.start.setText("")
        self.uinumberguessingform.stop.setText("")
        self.uinumberguessingform.yourguess.setText("")
        self.uinumberguessingform.Suggestioandresult.setText("Suggestion and Result")
        self.counter = 0

    def help(self):

            message_box = QtWidgets.QMessageBox()

            message_box.setWindowTitle("Developer information")
            message_box.setWindowIcon(QtGui.QIcon('royal_lionn.ico'))
            message_box.setIcon(QMessageBox.Information)

            message_box.setText("Developer : Amin Jafari\n"
                                "---------------------------------\n"
                                "Gmail : Aminjjjeffrey@gmail.com\n")
            message_box.exec_()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = UiNumberGuessingForm()
    sys.exit(app.exec_())
