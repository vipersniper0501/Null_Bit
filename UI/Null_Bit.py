# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/Null_Bit.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1070, 773)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1071, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 128))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tabWidget = QtWidgets.QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.CryptographicTab = QtWidgets.QWidget()
        self.CryptographicTab.setObjectName("CryptographicTab")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.CryptographicTab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(-1, -1, 1051, 551))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(5, 10, 10, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.Mode_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Mode_Selection.setMinimumSize(QtCore.QSize(100, 0))
        self.Mode_Selection.setObjectName("Mode_Selection")
        self.Mode_Selection.addItem("")
        self.Mode_Selection.addItem("")
        self.horizontalLayout.addWidget(self.Mode_Selection)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.Type_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.Type_Selection.setMinimumSize(QtCore.QSize(225, 0))
        self.Type_Selection.setObjectName("Type_Selection")
        self.Type_Selection.addItem("")
        self.Type_Selection.addItem("")
        self.Type_Selection.addItem("")
        self.horizontalLayout.addWidget(self.Type_Selection)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.Title1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Title1.setObjectName("Title1")
        self.verticalLayout_4.addWidget(self.Title1)
        self.Input_Box = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.Input_Box.setObjectName("Input_Box")
        self.verticalLayout_4.addWidget(self.Input_Box)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Crypto_Load_Input = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Crypto_Load_Input.setObjectName("Crypto_Load_Input")
        self.horizontalLayout_7.addWidget(self.Crypto_Load_Input)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Title2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Title2.setObjectName("Title2")
        self.verticalLayout_2.addWidget(self.Title2)
        self.Output_Box = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_2)
        self.Output_Box.setReadOnly(True)
        self.Output_Box.setObjectName("Output_Box")
        self.verticalLayout_2.addWidget(self.Output_Box)
        self.Save_Output_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Save_Output_Button.setObjectName("Save_Output_Button")
        self.verticalLayout_2.addWidget(self.Save_Output_Button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Key_Label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.Key_Label.setObjectName("Key_Label")
        self.verticalLayout_3.addWidget(self.Key_Label)
        self.Key_Box = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Key_Box.sizePolicy().hasHeightForWidth())
        self.Key_Box.setSizePolicy(sizePolicy)
        self.Key_Box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Key_Box.setObjectName("Key_Box")
        self.verticalLayout_3.addWidget(self.Key_Box)
        self.Load_Key_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Load_Key_Button.setObjectName("Load_Key_Button")
        self.verticalLayout_3.addWidget(self.Load_Key_Button)
        self.Save_Key_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.Save_Key_Button.setObjectName("Save_Key_Button")
        self.verticalLayout_3.addWidget(self.Save_Key_Button)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem3)
        self.tabWidget.addTab(self.CryptographicTab, "")
        self.SteganographicTab = QtWidgets.QWidget()
        self.SteganographicTab.setObjectName("SteganographicTab")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.SteganographicTab)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 1041, 551))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_5.setContentsMargins(5, 10, 10, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.Stego_Mode_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Stego_Mode_Selection.setMinimumSize(QtCore.QSize(100, 0))
        self.Stego_Mode_Selection.setObjectName("Stego_Mode_Selection")
        self.Stego_Mode_Selection.addItem("")
        self.Stego_Mode_Selection.addItem("")
        self.horizontalLayout_4.addWidget(self.Stego_Mode_Selection)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.Stego_Type_Selection = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.Stego_Type_Selection.setMinimumSize(QtCore.QSize(225, 0))
        self.Stego_Type_Selection.setObjectName("Stego_Type_Selection")
        self.Stego_Type_Selection.addItem("")
        self.horizontalLayout_4.addWidget(self.Stego_Type_Selection)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Stego_Input_Title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Stego_Input_Title.setObjectName("Stego_Input_Title")
        self.verticalLayout_6.addWidget(self.Stego_Input_Title)
        self.Stego_Input_Box = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget_3)
        self.Stego_Input_Box.setEnabled(True)
        self.Stego_Input_Box.setObjectName("Stego_Input_Box")
        self.verticalLayout_6.addWidget(self.Stego_Input_Box)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.Stego_Load_Input = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Stego_Load_Input.setObjectName("Stego_Load_Input")
        self.horizontalLayout_8.addWidget(self.Stego_Load_Input)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Stego_Filepath_Title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Stego_Filepath_Title.setObjectName("Stego_Filepath_Title")
        self.verticalLayout_7.addWidget(self.Stego_Filepath_Title)
        self.Stego_Filepath = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stego_Filepath.sizePolicy().hasHeightForWidth())
        self.Stego_Filepath.setSizePolicy(sizePolicy)
        self.Stego_Filepath.setClearButtonEnabled(False)
        self.Stego_Filepath.setObjectName("Stego_Filepath")
        self.verticalLayout_7.addWidget(self.Stego_Filepath)
        self.Stego_Browse_Filepath_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Stego_Browse_Filepath_Button.setObjectName("Stego_Browse_Filepath_Button")
        self.verticalLayout_7.addWidget(self.Stego_Browse_Filepath_Button)
        self.Stego_Picture = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stego_Picture.sizePolicy().hasHeightForWidth())
        self.Stego_Picture.setSizePolicy(sizePolicy)
        self.Stego_Picture.setMinimumSize(QtCore.QSize(475, 167))
        self.Stego_Picture.setText("")
        self.Stego_Picture.setAlignment(QtCore.Qt.AlignCenter)
        self.Stego_Picture.setObjectName("Stego_Picture")
        self.verticalLayout_7.addWidget(self.Stego_Picture)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Stego_Output_Title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Stego_Output_Title.setObjectName("Stego_Output_Title")
        self.verticalLayout_8.addWidget(self.Stego_Output_Title)
        self.Stego_Output_Box = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Stego_Output_Box.sizePolicy().hasHeightForWidth())
        self.Stego_Output_Box.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Stego_Output_Box.setFont(font)
        self.Stego_Output_Box.setStyleSheet("background: white")
        self.Stego_Output_Box.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Stego_Output_Box.setLineWidth(1)
        self.Stego_Output_Box.setText("")
        self.Stego_Output_Box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Stego_Output_Box.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.Stego_Output_Box.setObjectName("Stego_Output_Box")
        self.verticalLayout_8.addWidget(self.Stego_Output_Box)
        self.Stego_Save_Output_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Stego_Save_Output_Button.setObjectName("Stego_Save_Output_Button")
        self.verticalLayout_8.addWidget(self.Stego_Save_Output_Button)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.Stego_Key_Title = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.Stego_Key_Title.setObjectName("Stego_Key_Title")
        self.verticalLayout_9.addWidget(self.Stego_Key_Title)
        self.Stego_Key_Box = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.Stego_Key_Box.setObjectName("Stego_Key_Box")
        self.verticalLayout_9.addWidget(self.Stego_Key_Box)
        self.Stego_Load_Key_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Stego_Load_Key_Button.setObjectName("Stego_Load_Key_Button")
        self.verticalLayout_9.addWidget(self.Stego_Load_Key_Button)
        self.Stego_Save_Key_Button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.Stego_Save_Key_Button.setObjectName("Stego_Save_Key_Button")
        self.verticalLayout_9.addWidget(self.Stego_Save_Key_Button)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem9 = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem9)
        self.tabWidget.addTab(self.SteganographicTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Execute = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Execute.setMinimumSize(QtCore.QSize(100, 20))
        self.Execute.setObjectName("Execute")
        self.horizontalLayout_3.addWidget(self.Execute)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.Clear_Button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Clear_Button.setMinimumSize(QtCore.QSize(100, 20))
        self.Clear_Button.setObjectName("Clear_Button")
        self.horizontalLayout_3.addWidget(self.Clear_Button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Null Bit"))
        self.label.setText(_translate("MainWindow", "Null Bit Encryption/Decryption"))
        self.label_2.setText(_translate("MainWindow", "Mode:"))
        self.Mode_Selection.setItemText(0, _translate("MainWindow", "Encrypt"))
        self.Mode_Selection.setItemText(1, _translate("MainWindow", "Decrypt"))
        self.label_3.setText(_translate("MainWindow", "Encryption Type"))
        self.Type_Selection.setItemText(0, _translate("MainWindow", "XOR Cipher"))
        self.Type_Selection.setItemText(1, _translate("MainWindow", "Columnar Transposition Cipher"))
        self.Type_Selection.setItemText(2, _translate("MainWindow", "Vigenere Cipher"))
        self.Title1.setText(_translate("MainWindow", "TextLabel"))
        self.Crypto_Load_Input.setText(_translate("MainWindow", "Load Input From File"))
        self.Title2.setText(_translate("MainWindow", "TextLabel"))
        self.Save_Output_Button.setText(_translate("MainWindow", "Save _ Output To File"))
        self.Key_Label.setText(_translate("MainWindow", "TextLabel"))
        self.Load_Key_Button.setText(_translate("MainWindow", "Load Key From File"))
        self.Save_Key_Button.setText(_translate("MainWindow", "Save Key To File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CryptographicTab), _translate("MainWindow", "Cryptographic Encryption"))
        self.label_4.setText(_translate("MainWindow", "Mode:"))
        self.Stego_Mode_Selection.setItemText(0, _translate("MainWindow", "Encrypt"))
        self.Stego_Mode_Selection.setItemText(1, _translate("MainWindow", "Decrypt"))
        self.label_5.setText(_translate("MainWindow", "Encryption Type"))
        self.Stego_Type_Selection.setItemText(0, _translate("MainWindow", "Hide in Image"))
        self.Stego_Input_Title.setText(_translate("MainWindow", "Message to Encode:"))
        self.Stego_Load_Input.setText(_translate("MainWindow", "Load Input Message From File"))
        self.Stego_Filepath_Title.setText(_translate("MainWindow", "Filepath Of File To Hide Message In:"))
        self.Stego_Browse_Filepath_Button.setText(_translate("MainWindow", "Browse Files"))
        self.Stego_Output_Title.setText(_translate("MainWindow", "TextLabel"))
        self.Stego_Save_Output_Button.setText(_translate("MainWindow", "Save Output"))
        self.Stego_Key_Title.setText(_translate("MainWindow", "[Mode] Key"))
        self.Stego_Load_Key_Button.setText(_translate("MainWindow", "Load Key From File"))
        self.Stego_Save_Key_Button.setText(_translate("MainWindow", "Save Key To File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SteganographicTab), _translate("MainWindow", "Steganographic Encryption"))
        self.Execute.setText(_translate("MainWindow", "Run"))
        self.Clear_Button.setText(_translate("MainWindow", "Clear"))
