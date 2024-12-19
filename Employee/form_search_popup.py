import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Employee.form_employees_search_ui import Ui_SearchEmployee

class EmployeeFormSearchPopup(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.ui = Ui_SearchEmployee()
        self.ui.setupUi(self)

        
        




            
   