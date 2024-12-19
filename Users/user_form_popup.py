import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Users.frm_popup_users_ui import Ui_frm_popup_user

class userFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_user()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)

        


