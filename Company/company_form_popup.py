import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Company.frm_popup_company_ui import Ui_frm_popup_company


class companyFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_company()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)

        


