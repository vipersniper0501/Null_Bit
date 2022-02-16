import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt

from UI.Null_Bit import Ui_MainWindow
from XOR import XOR_Cipher
from COLUMNAR import Columnar_Cipher
from VIGENERE import Vigenere_Cipher


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
        """
        Encrypts the provided plain text in the Input Box, and generates a key
        to be used at a later time to decrypt the newly encoded text.
        """
        cipher = XOR_Cipher()
        msg = self.Input_Box.toPlainText()

        cipher.encrypt(msg)
        self.Output_Box.setPlainText(str(cipher.cipher_text)[2:-1])
        self.Key_Box.setText(str(cipher.key)[2:-1])

    def DecryptXOR(self):
        """
        Decrypts XOR ciphertext provided in the Input Box using the provided 
        Key, and outputs the decrypted text into the Output Box.
        """
        cipher = XOR_Cipher()
        msg = self.Input_Box.toPlainText()
        key = self.Key_Box.text()

        cipher.decrypt(msg, key)
        self.Output_Box.setPlainText(str(cipher.cipher_text))

    def EncryptColumnar(self):
        """
        Encrypts the provided plain text in the Input Box with the Columnar 
        Transposition Cipher using the provided key.
        """
        cipher = Columnar_Cipher()
        key = self.Key_Box.text()
        msg = self.Input_Box.toPlainText()

        if key != "":
            duplicate_letters = False
            dupLetter = ""
            for i in range(len(key)):
                if key.count(key[i]) > 1:
                    duplicate_letters = True
                    dupLetter = key[i]
                    break
            if not duplicate_letters:
                cipher.encrypt(msg, key)
                self.Output_Box.setPlainText(cipher.cipher_text)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(f"Duplicate letters in key is not allowed.\nDuplicate Letter: {dupLetter}")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Missing Key")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()


    def DecryptColumnar(self):
        """
        Decrypts Columnar ciphertext provided in the Input Box using the
        provided Key, and outputs the decrypted text into the Output Box.
        """
        cipher = Columnar_Cipher()
        key = self.Key_Box.text()
        msg = self.Input_Box.toPlainText()

        if key != "":
            duplicate_letters = False
            dupLetter = ""
            for i in range(len(key)):
                if key.count(key[i]) > 1:
                    duplicate_letters = True
                    dupLetter = key[i]
                    break
            if not duplicate_letters:
                cipher.decrypt(msg, key)
                self.Output_Box.setPlainText(cipher.cipher_text)
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(f"Duplicate letters in key is not allowed.\nDuplicate Letter: {dupLetter}")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Missing Key")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()

    def EncryptVigenere(self):
        """
        Encrypts the provided plain text in the Input Box with the Vigenere 
        Cipher using the provided key.
        """


    def DecryptVigenere(self):
        pass


    def EncryptCaesar(self):
        pass


    def DecryptCaesar(self):
        pass


    def EncryptPigLatin(self):
        pass


    def DecryptPigLatin(self):
        pass


    def Run(self):
        currentType = self.Type_Selection.currentText()
        if (self.Mode_Selection.currentText() == "Encrypt"):
            if (currentType == "XOR Cipher"):
                self.EncryptXOR()
            elif (currentType == "Columnar Transposition Cipher"):
                self.EncryptColumnar()
        else:
            if (currentType == "XOR Cipher"):
                self.DecryptXOR()
            elif (currentType == "Columnar Transposition Cipher"):
                self.DecryptColumnar()

    def Change_Mode(self):
        """
        Changes text labels to reflect the current mode
        """

        currentType = self.Type_Selection.currentText()
        self.Output_Box.setPlainText("")

        if (self.Mode_Selection.currentText() == "Encrypt"):
            if (currentType == "XOR Cipher"):
                self.Key_Box.setReadOnly(True)
                self.Load_Key_Button.setDisabled(True)
            else:
                self.Key_Box.setReadOnly(False)
                self.Load_Key_Button.setDisabled(False)
            self.Title1.setText("Plain Text (Input):")
            self.Title2.setText("Encoded Text (Output):")
            self.Key_Label.setText("Encryption Key:")
            self.Save_Output_Button.setText("Save Encrypted Output To File")
        else:
            self.Title1.setText("Cipher Text (Input):")
            self.Title2.setText("Decoded Text (Output):")
            self.Key_Label.setText("Decryption Key:")
            self.Save_Output_Button.setText("Save Decrypted Output To File")

            self.Key_Box.setReadOnly(False)
            self.Load_Key_Button.setDisabled(False)


    def Clear_All(self):
        """
        Resets Input, Output, and Key boxes
        """
        self.Input_Box.setPlainText("")
        self.Output_Box.setPlainText("")
        self.Key_Box.setText("")


    def Change_Type(self):
        self.Change_Mode()
        self.Clear_All()


    def NullBit_Assign_Functions(self):
        """
        Assigns functions to ui buttons along with running startup code.
        """

        self.Change_Mode()


        self.Execute.clicked.connect(self.Run)
        self.Mode_Selection.currentIndexChanged.connect(self.Change_Mode)
        self.Type_Selection.currentIndexChanged.connect(self.Change_Type)
        self.Clear_Button.clicked.connect(self.Clear_All)






if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = NullBitMainWindow()
    main.show()
    sys.exit(app.exec_())
