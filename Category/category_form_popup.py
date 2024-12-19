import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Category.frm_popup_category_ui import Ui_frm_popup_category


class categoryFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_category()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)

        


