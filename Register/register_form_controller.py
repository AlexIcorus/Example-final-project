import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton,QVBoxLayout,QLabel, QFrame, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIntValidator

from Register.form_register_ui import Ui_FormRegister
from Register.register_controller import RegisterController

class RegisterFormController(QWidget):
    def __init__(self):
        super().__init__()
    
        self.ui = Ui_FormRegister()
        self.controller = RegisterController()
        self.setObjectName("FormRegsiter")
        self.resize(400, 300)
        self.ui.setupUi(self)
        
         # Connect UI elements to class variables
        self.txt_name = self.ui.txt_name
        self.txt_username = self.ui.txt_username
        self.txt_password = self.ui.txt_password
        
        self.txt_name.setText('Pou')
        self.txt_username.setText('pou')
        self.txt_password.setText('password')
        
        self.btn_register = self.ui.btn_register
        
        # self.buttons_list = self.ui.findChildren(QPushButton)
        
        # Initialize signal-slot connections
        self.initSignalSlot()

    def initSignalSlot(self):
        self.btn_register.clicked.connect(self.register)
        
    
  
        
    def getFormatUserInfo(self):
        # Function to retrieve student information from the form
        name = self.txt_name.toPlainText().strip()
        username = self.txt_username.toPlainText().strip()
        password = self.txt_password.toPlainText().strip()

        user_info = {
            "name": name,
            "username": username,
            "password": password,
           
        }
        
        return user_info
    
    def register(self):
        
        user_info=self.getFormatUserInfo()
        
        status =  self.controller.addUser(user_info["name"],user_info["username"],user_info["password"])
        
        if status:
           QMessageBox.information(self, "ສຳເລັດ", "Register Successfully",
                                        QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.information(self, "Warning", "ບໍ່ສຳເລັດ",
                                        QMessageBox.StandardButton.Ok)
        
        self.clearForm()
        
        
        
    def clearForm(self):
        self.txt_name.clear()
        self.txt_username.clear()
        self.txt_password.clear()
        
        self.txt_name.setFocus()
        
  

