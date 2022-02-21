from PyQt5.QtWidgets import QDialog, QMessageBox
from UI.Null_Bit_Login import Ui_Null_Bit_Login



DEFAULT_USERNAME = "SKILLS2022"
DEFAULT_PASSWORD = "AFCEA"



class LoginWindow(QDialog, Ui_Null_Bit_Login):
    """
    Login window for application
    """

    def __init__(self, parent=None):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        #  self.setFixedSize(419, 163)
        self.LoginWindowAssignFunctions()


    def ValidateLogin(self):
        """
        Validates username and password login attempt.
        """

        if self.Username_Box.text() == DEFAULT_USERNAME and self.Password_Box.text() == DEFAULT_PASSWORD:
            self.accept()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Invalid Username or Password. Please try again.")
            msg.setIcon(QMessageBox.Warning)
            _ = msg.exec_()


    def CancelLogin(self):
        """
        Cancels Login attempt
        """
        self.reject()


    def LoginWindowAssignFunctions(self):
        """
        Assigns functions to login window buttons
        """
        self.Submit_Button.clicked.connect(self.ValidateLogin)
        self.Cancel_Button.clicked.connect(self.CancelLogin)
