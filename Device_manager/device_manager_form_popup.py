import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Device_manager.frm_popup_device_manager_ui import Ui_frm_popup_device_manager


class DeviceManagerFormPopUp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_popup_device_manager()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame)