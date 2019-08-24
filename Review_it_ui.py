# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Review_it.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(456, 336)
        Dialog.setAutoFillBackground(False)
        self.Heading = QtWidgets.QLabel(Dialog)
        self.Heading.setGeometry(QtCore.QRect(120, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.Review = QtWidgets.QPlainTextEdit(Dialog)
        self.Review.setGeometry(QtCore.QRect(50, 80, 361, 141))
        self.Review.setToolTip("")
        self.Review.setBackgroundVisible(False)
        self.Review.setObjectName("Review")
        self.Button = QtWidgets.QPushButton(Dialog)
        self.Button.setGeometry(QtCore.QRect(180, 240, 75, 23))
        self.Button.setObjectName("Button")
        self.Prediction = QtWidgets.QLabel(Dialog)
        self.Prediction.setGeometry(QtCore.QRect(190, 290, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Prediction.setFont(font)
        self.Prediction.setText("")
        self.Prediction.setObjectName("Prediction")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Review It v0.1"))
        self.Heading.setText(_translate("Dialog", "Welcome to Review it 0.1 !!!"))
        self.Review.setPlaceholderText(_translate("Dialog", "-----------------------------Write Your Review Here----------------------------"))
        self.Button.setText(_translate("Dialog", "Review It !!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

