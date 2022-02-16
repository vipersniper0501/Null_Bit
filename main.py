import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtCore import Qt

from UI.Null_Bit import Ui_MainWindow

class NullBitMainWindow(QMainWindow, Ui_MainWindow):
    """
    Manages Null Bit's GUI
    """

    def __init__(self, parent=None):
        super(NullBitMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1072, 780)
        self.NullBit_Assign_Functions()


    def EncryptXOR(self):
        pass

    def DecryptXOR(self):
        pass

    def Run(self):
        currentType = self.Type_Selection.currentText()
        if (self.Mode_Selection.currentText() == "Encrypt"):
            if (currentType == "XOR Cipher"):
                self.EncryptXOR()
        else:
            if (currentType == "XOR Cipher"):
                self.DecryptXOR()

    def Change_Mode(self):
        currentType = self.Type_Selection.currentText()

        if (self.Mode_Selection.currentText() == "Encrypt"):
            if (currentType == "XOR Cipher"):
                self.Load_Key_Button.setDisabled(True)
            self.Title1.setText("Encrypt Text (Input):")
            self.Title2.setText("Encoded Text (Output):")
            self.Key_Label.setText("Encryption Key:")
        else:
            self.Title1.setText("Decrypt Text (Input):")
            self.Title2.setText("Decoded Text (Output):")
            self.Key_Label.setText("Decryption Key:")
            if currentType == "XOR Cipher":
                self.Load_Key_Button.setDisabled(False)

    def Clear_All(self):
        """
        Resets Input, Output, and Key boxes
        """

    def NullBit_Assign_Functions(self):
        """
        Assigns functions to ui buttons along with running startup code.
        """

        self.Change_Mode()


        self.Execute.clicked.connect(self.Run)
        self.Mode_Selection.currentIndexChanged.connect(self.Change_Mode)
        self.Clear_Button.clicked.connect(self.Clear_All)






if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = NullBitMainWindow()
    main.show()
    sys.exit(app.exec_())
