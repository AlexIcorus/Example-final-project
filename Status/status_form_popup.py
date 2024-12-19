import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Status.frm_popup_status_ui import Ui_frm_popup_status
class statusFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_status()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)