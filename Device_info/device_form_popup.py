import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Device_info.frm_popup_device_ui import Ui_frm_popup_device


class DeviceFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_device()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)

        



    


            
   