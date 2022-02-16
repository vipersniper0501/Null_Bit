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

    def Change_Mode(self):
        pass

    def Clear_All(self):
        pass

    def NullBit_Assign_Functions(self):
        pass



if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    app = QApplication(sys.argv)
    main = NullBitMainWindow()
    main.show()
    sys.exit(app.exec_())
