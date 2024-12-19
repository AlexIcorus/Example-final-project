import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Department.frm_popup_department_ui import Ui_frm_popup_department


class departmentFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_department()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)

        


