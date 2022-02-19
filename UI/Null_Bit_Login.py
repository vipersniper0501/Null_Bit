# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Null_Bit_Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Null_Bit_Login(object):
    def setupUi(self, Null_Bit_Login):
        Null_Bit_Login.setObjectName("Null_Bit_Login")
        Null_Bit_Login.resize(320, 163)
        font = QtGui.QFont()
        font.setPointSize(10)
        Null_Bit_Login.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(Null_Bit_Login)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 321, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Username_Box = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Username_Box.setObjectName("Username_Box")
        self.horizontalLayout.addWidget(self.Username_Box)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Password_Box = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.Password_Box.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password_Box.setObjectName("Password_Box")
        self.horizontalLayout_2.addWidget(self.Password_Box)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Submit_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Submit_Button.setObjectName("Submit_Button")
        self.horizontalLayout_3.addWidget(self.Submit_Button)
        self.Cancel_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Cancel_Button.setObjectName("Cancel_Button")
        self.horizontalLayout_3.addWidget(self.Cancel_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Null_Bit_Login)
        QtCore.QMetaObject.connectSlotsByName(Null_Bit_Login)

    def retranslateUi(self, Null_Bit_Login):
        _translate = QtCore.QCoreApplication.translate
        Null_Bit_Login.setWindowTitle(_translate("Null_Bit_Login", "Null Bit Login"))
        self.label_3.setText(_translate("Null_Bit_Login", "Login:"))
        self.label.setText(_translate("Null_Bit_Login", "Username"))
        self.label_2.setText(_translate("Null_Bit_Login", "Password"))
        self.Submit_Button.setText(_translate("Null_Bit_Login", "Submit"))
        self.Cancel_Button.setText(_translate("Null_Bit_Login", "Cancel"))
