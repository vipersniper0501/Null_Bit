import sys
import os
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from UI.Null_Bit import Ui_MainWindow
from login import LoginWindow
from XOR import XOR_Cipher
from COLUMNAR import Columnar_Cipher
from VIGENERE import Vigenere_Cipher
from STEGANOGRAPHY import Stego_Image


class NullBitMainWindow(QMainWindow, Ui_MainWindow):
    """
    Manages Null Bit's GUI
    """

    changingTab = False
    
    def __init__(self, parent=None):
        super(NullBitMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1072, 780)
        self.startingUp = True
        self.disableChangeModeWarning = False
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
                msg.setText("Duplicate letters in key is not allowed.\n"
                            f"Duplicate Letter: {dupLetter}")
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
                msg.setText("Duplicate letters in key is not allowed.\n"
                            f"Duplicate Letter: {dupLetter}")
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

        cipher = Vigenere_Cipher()
        key = self.Key_Box.text()
        msg = self.Input_Box.toPlainText()

        if key != "":
            cipher.encrypt(msg, key)
            self.Output_Box.setPlainText(cipher.cipher_text)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Missing Key")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()


    def DecryptVigenere(self):
        """
        Decrypts Vigenere ciphertext provided in the Input Box using the
        provided Key, and outputs the decrypted text into the Output Box.
        """

        cipher = Vigenere_Cipher()
        key = self.Key_Box.text()
        msg = self.Input_Box.toPlainText()

        if key != "":
            cipher.decrypt(msg, key)
            self.Output_Box.setPlainText(cipher.cipher_text)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Missing Key")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()


    def StegoEncodeImage(self):
        """
        Encodes message into a *.png image file with the provided image, message,
        and key.
        """

        stego = Stego_Image()
        filepath = self.Stego_Filepath.text()
        key = self.Stego_Key_Box.text()
        msg = self.Stego_Input_Box.toPlainText()

        def double_QSize(s1):
            """
            Only used for doubling QSize values.
            """
            r = s1
            r += s1
            return r

        if filepath.endswith('.png'):
            if key != "":
                stego.encode(filepath, msg, key)
                self.Stego_Output_Box.setText(stego.encoded_filepath)
                self.Stego_Picture.setPixmap(
                    QPixmap(stego.encoded_filepath).scaled(
                        double_QSize(self.Stego_Output_Box.size()),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Missing Key")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("File is not of type *.png")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()


    def StegoDecodeImage(self):
        """
        Decodes message from a *.png image file with the provided image, message,
        and key.
        """
        stego = Stego_Image()
        filepath = self.Stego_Filepath.text()
        key = self.Stego_Key_Box.text()

        if filepath.endswith('.png'):
            if key != "":
                result = stego.decode(filepath, key)
                
                if result == 0:
                    self.Stego_Output_Box.setText(stego.cipher_text)
                else:
                    msg = QMessageBox()
                    msg.setWindowTitle("Error")
                    msg.setText("Your key did not match.")
                    msg.setIcon(QMessageBox.Warning)
                    _ = msg.exec_()
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("Missing Key")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("File is not of type *.png")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()



    def LoadPNGFile(self):
        """
        Loads png file.
        """
        def double_QSize(s1):
            """
            Only used for doubling QSize values.
            """
            r = s1
            r += s1
            return r

        fname, _ = QFileDialog.getOpenFileNames(self,
                                                "Select File to"
                                                " load input from",
                                                "./",
                                                "PNG (*.png)")
        if len(fname) != 0:
            fname = str(fname[0])
        else:
            return
        if fname != '' and os.path.isfile(fname):
            if fname.lower().endswith(".png"):
                self.Stego_Filepath.setText(fname)
                self.Stego_Picture.setPixmap(
                    QPixmap(fname).scaled(
                        double_QSize(self.Stego_Output_Box.size()),
                        Qt.KeepAspectRatio,
                        Qt.SmoothTransformation
                    )
                )
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("File is not of type *.png")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()

    def LoadInputFromFile(self):
        """
        Loads Input text from a text file.
        """

        fname, _ = QFileDialog.getOpenFileNames(self,
                                                "Select File to"
                                                " load input from",
                                                "./",
                                                "Text (*.txt)")
        if len(fname) != 0:
            fname = str(fname[0])
        else:
            return
        if fname != '' and os.path.isfile(fname):
            if fname.endswith(".txt"):
                with open(fname, "r") as f:
                    self.Input_Box.setPlainText(f.read()[7:])
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("File is not of type *.txt")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()


    def SaveOutputToFile(self):
        """
        Saves the output to selected file. Will overwrite existing
        contents of file so use with caution.
        """

        fname, _ = QFileDialog.getSaveFileName(self, "File to save output to", "./", "Text (*.txt)")
        if fname != '':
            if fname.endswith(".txt"):
                with open(fname, "w") as f:
                    L = ["Output:", self.Output_Box.toPlainText()]
                    f.writelines(L)
            else:
                with open(fname + ".txt", "w") as f:
                    L = ["Output:", self.Output_Box.toPlainText()]
                    f.writelines(L)


    def SaveKeyToFile(self):
        """
        Saves the key in Key Box to selected file. Will overwrite
        existing contents of file so use with caution.
        """

        if self.tabWidget.currentIndex() == 0:
            L = ["Key:", self.Key_Box.text()]
        else:
            L = ["Key:", self.Stego_Key_Box.text()]
        fname, _ = QFileDialog.getSaveFileName(self,
                                               "Select File to save key to",
                                               "./",
                                               "Key (*.key)")
        if fname != '':
            if fname.endswith(".key"):
                with open(fname, "w") as f:
                    f.writelines(L)
            else:
                with open(fname + ".key", "w") as f:
                    f.writelines(L)


    def LoadKeyFromFile(self):
        """
        Loads key from a file and puts it in the key box.
        """

        fname, _ = QFileDialog.getOpenFileNames(self,
                                                "Select File to"
                                                " extract key from",
                                                "./",
                                                "Key (*.key)")
        if len(fname) != 0:
            fname = str(fname[0])
        else:
            return
        if fname != '' and os.path.isfile(fname):
            if fname.endswith(".key"):
                with open(fname, "r") as f:
                    if self.tabWidget.currentIndex() == 0:
                        self.Key_Box.setText(f.read()[4:])
                    else:
                        self.Stego_Key_Box.setText(f.read()[4:])
            else:
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText("File is not of type *.key")
                msg.setIcon(QMessageBox.Warning)
                _ = msg.exec_()


    def Run(self):
        """
        Identify the current type and mode and run the associated cipher
        program.
        """

        if self.tabWidget.currentIndex() == 0:
            currentType = self.Type_Selection.currentText()
            if self.Mode_Selection.currentText() == "Encrypt":
                if currentType == "XOR Cipher":
                    self.EncryptXOR()
                elif currentType == "Columnar Transposition Cipher":
                    self.EncryptColumnar()
                elif currentType == "Vigenere Cipher":
                    self.EncryptVigenere()
            else:
                if currentType == "XOR Cipher":
                    self.DecryptXOR()
                elif currentType == "Columnar Transposition Cipher":
                    self.DecryptColumnar()
                elif currentType == "Vigenere Cipher":
                    self.DecryptVigenere()
        else:
            currentType = self.Stego_Type_Selection.currentText()
            if self.Stego_Mode_Selection.currentText() == "Encrypt":
                if currentType == "Hide in Image":
                    self.StegoEncodeImage()
            else:
                if currentType == "Hide in Image":
                    self.StegoDecodeImage()


    def DisableChangeModeWarning(self, btn):
        """
        Disables the warning that appears everytime you try and change
        encryption modes.
        """

        if btn.text() == 'Disable this message':
            self.disableChangeModeWarning = True
            self.Change_Mode()


    def ChangeModeWarningPopup(self):
        """
        Displays Popup warning that input and output boxes will be cleared.
        """

        msg = QMessageBox()
        msg.setWindowTitle("Warning")
        msg.setText("Warning: When changing mode or tab, all input and output"
                    " boxes will be cleared. Are you sure you want "
                    "to continue?")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.addButton('Disable this message', QMessageBox.ApplyRole)
        msg.buttonClicked.connect(self.DisableChangeModeWarning)
        return msg.exec_()


    def Change_Tab(self):
        warning = QMessageBox.Ok
        if not self.changingTab:
            if not self.disableChangeModeWarning:
                warning = self.ChangeModeWarningPopup()

            if warning == QMessageBox.Ok or self.disableChangeModeWarning:
                if not self.disableChangeModeWarning:
                    self.disableChangeModeWarning = True
                    self.Change_Mode()
                    self.disableChangeModeWarning = False
                else:
                    self.Change_Mode()
            else:
                self.changingTab = True
                self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() == 0 if 1 else 0)
                self.changingTab = False
                # if not self.disableChangeModeWarning:
                self.disableChangeModeWarning = True
                self.Change_Mode()
                self.disableChangeModeWarning = False
                # else:
                    # self.Change_Mode()

    def Change_Mode(self):
        """
        Changes text labels to reflect the current mode
        """

        # Default to Okay
        warning = QMessageBox.Ok

        if not self.startingUp:
            # if disable change mode warnign is false
            if not self.disableChangeModeWarning:
                warning = self.ChangeModeWarningPopup()

        if self.startingUp or warning == QMessageBox.Ok or self.disableChangeModeWarning:

            self.Clear_All()

            # Automatically take output information and put it in input box if
            # Output_Box is not empty.
            #  if self.Output_Box.toPlainText() != "":
                #  self.Input_Box.setPlainText(self.Output_Box.toPlainText())

            if self.tabWidget.currentIndex() == 0:
                currentType = self.Type_Selection.currentText()


                SecurePalette = QPalette()
                SecurePalette.setColor(QPalette.WindowText, Qt.darkGreen)

                UnsecurePalette = QPalette()
                UnsecurePalette.setColor(QPalette.WindowText, Qt.red)

                if self.Mode_Selection.currentText() == "Encrypt":
                    if currentType == "XOR Cipher":
                        self.Key_Box.setDisabled(True)
                        self.Load_Key_Button.setDisabled(True)
                    else:
                        self.Key_Box.setDisabled(False)
                        self.Load_Key_Button.setDisabled(False)
                    self.Title1.setText("Plain Text (Input):")
                    self.Title1.setPalette(UnsecurePalette)

                    self.Title2.setText("Encoded Text (Output):")
                    self.Title2.setPalette(SecurePalette)

                    self.Key_Label.setText("Encryption Key:")
                    self.Save_Output_Button.setText("Save Encrypted Output To File")
                else:
                    self.Title1.setText("Cipher Text (Input):")
                    self.Title1.setPalette(SecurePalette)

                    self.Title2.setText("Decoded Text (Output):")
                    self.Title2.setPalette(UnsecurePalette)

                    self.Key_Label.setText("Decryption Key:")
                    self.Save_Output_Button.setText("Save Decrypted Output To File")

                    self.Key_Box.setDisabled(False)
                    self.Load_Key_Button.setDisabled(False)
            else:
                if self.Stego_Mode_Selection.currentText() == "Encrypt":
                    if self.Stego_Type_Selection.currentText() == "Hide in Image":
                        self.Stego_Input_Box.setEnabled(True)
                        self.Stego_Load_Input.setEnabled(True)
                        self.Stego_Save_Output_Button.setEnabled(False)

                    self.Stego_Filepath_Title.setText("Filepath Of Image To "
                                                      "Encode Message In:")
                    self.Stego_Output_Title.setText("Encoded Output Saved To: ")
                    self.Stego_Key_Title.setText("Encryption Key:")
                else:
                    self.Stego_Input_Box.setEnabled(False)
                    self.Stego_Load_Input.setEnabled(False)
                    self.Stego_Save_Output_Button.setEnabled(True)

                    self.Stego_Filepath_Title.setText("Filepath Of Encoded Image:")
                    self.Stego_Output_Title.setText("Decoded Output: ")
                    self.Stego_Key_Title.setText("Decryption Key:")



            if self.startingUp:
                self.startingUp = False


    def Clear_All(self):
        """
        Resets Input, Output, and Key boxes
        """
        self.Input_Box.setPlainText("")
        self.Output_Box.setPlainText("")
        self.Key_Box.setText("")

        self.Stego_Input_Box.setPlainText("")
        self.Stego_Output_Box.setText("")
        self.Stego_Key_Box.setText("")
        self.Stego_Filepath.setText("")
        self.Stego_Picture.clear()


    def Change_Type(self):
        """
        Resets everything due to a new encryption type being used.
        """
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

        self.Save_Key_Button.clicked.connect(self.SaveKeyToFile)
        self.Load_Key_Button.clicked.connect(self.LoadKeyFromFile)
        self.Save_Output_Button.clicked.connect(self.SaveOutputToFile)
        self.Crypto_Load_Input.clicked.connect(self.LoadInputFromFile)

        self.Stego_Mode_Selection.currentIndexChanged.connect(self.Change_Mode)
        self.Stego_Type_Selection.currentIndexChanged.connect(self.Change_Type)

        self.Stego_Browse_Filepath_Button.clicked.connect(self.LoadPNGFile)
        self.Stego_Load_Key_Button.clicked.connect(self.LoadKeyFromFile)
        self.Stego_Save_Key_Button.clicked.connect(self.SaveKeyToFile)
        self.Stego_Load_Input.clicked.connect(self.LoadInputFromFile)
        self.Stego_Save_Output_Button.clicked.connect(self.SaveOutputToFile)
        
        self.tabWidget.currentChanged.connect(self.Change_Tab)


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = NullBitMainWindow()
    login = LoginWindow()
    isValidated = login.exec_()
    if isValidated == 1:
        main.show()
    else:
        sys.exit(1)
    sys.exit(app.exec_())
