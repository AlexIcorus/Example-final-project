import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Employee.form_employees_popup_ui import Ui_frm_employee_popup


class EmployeeFormPopup(QMainWindow):
    def __init__(self):

        super().__init__()
        self.ui = Ui_frm_employee_popup()
        self.ui.setupUi(self)




            
   