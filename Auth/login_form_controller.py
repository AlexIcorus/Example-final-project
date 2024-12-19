import sys
import bcrypt


from PyQt6.QtWidgets import QMainWindow, QLineEdit, QApplication, QPushButton, QFrame, QMessageBox,QPlainTextEdit
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QIntValidator,QCloseEvent

from Auth.frm_login_ui import Ui_FormLogin
from Register.register_form_controller import RegisterFormController
from Auth.login_controller import LoginController
from Menu.menu_form_controller import MenuFormController
from Device_info.device_form_controller import FrmDeviceController
from Device_manager.device_form_manager_controller import FrmDeviceManageController


class LoginFormController(QMainWindow):
    def __init__(self):
        
        super().__init__()
        self.windowRegister = RegisterFormController()
        self.loginController = LoginController()
        self.menuFormController = MenuFormController()
        self.devicemanagercontroller = FrmDeviceManageController()    

       

        self.ui = Ui_FormLogin()
        self.setObjectName("FormLogin")
        self.resize(400, 300)
        self.ui.setupUi(self)
        
        # Connect UI elements to class variables
        self.txt_username = self.ui.txt_username
        self.txt_username.setFocus()
        self.txt_password = self.ui.txt_password
        self.txt_password.setEchoMode(QLineEdit.EchoMode.Password) 
    
    
        self.txt_username.setText('pou')
        self.txt_password.setText('password')

        
        self.btn_login = self.ui.btn_login
        self.btn_register = self.ui.btn_register
        self.reg_btn_close = self.windowRegister.ui.btn_close
        self.itm_logout = self.menuFormController.ui.itm_Logout
        

        
     
        
        # Initialize signal-slot connections
        self.initSignalSlot()

    def initSignalSlot(self):
        self.btn_login.clicked.connect(self.login)
        self.txt_password.returnPressed.connect(self.login)
        self.btn_register.clicked.connect(self.register)
        self.reg_btn_close.clicked.connect(self.registerClose)
        self.itm_logout.triggered.connect(self.menuClose)
        self.txt_username.returnPressed.connect(self.focusPassword)
        self.itm_logout.triggered.connect(self.checkMenuLogout)
        # self.txt_password.returnPressed.
        # Connect the returnPressed signal to the login function
        

    def getUserInfo(self):
        # Function to retrieve user information from the form
        username = self.txt_username.text().strip()
        password = self.txt_password.text().strip()
        

        user_info = {
            "username": username,
            "password": password,
        }
        
        return user_info
    
    def focusPassword(self):
        self.txt_password.setFocus()
        
    def menuClose(self):
        self.show()
        self.menuFormController.close()
        
        
    def register(self):
        self.windowRegister.show()
        self.close()
    
    def registerClose(self):
        self.show()
        self.windowRegister.close()

    def login(self):
        try:
            # Function to handle login
            user_info = self.getUserInfo()
            
            if user_info["username"] and user_info["password"]:
                user_data_after_login = self.loginController.selectData(user_info["username"])
                
                if len(user_data_after_login) <= 0:
                    QMessageBox.information(self, "Warning", "User not found",
                                            QMessageBox.StandardButton.Ok)
                    return
                
                userPassword = user_info["password"]
    
                # Encoding user password 
                userBytes = userPassword.encode('utf-8') 
               
                # Checking password 
                result = bcrypt.checkpw(userBytes, user_data_after_login[0]["password"].encode('utf-8')) 
               
                if result:
                    # print(result)
                    # QMessageBox.information(self, "Warning", "Login Succesful",
                    #                         QMessageBox.StandardButton.Ok)
                    self.close()
                    
                    self.menuFormController.setUserAfterLogin(user_data_after_login)
                   
                    self.menuFormController.showMaximized()
                    self.txt_password.clear()
                else:
                    QMessageBox.information(self, "Warning", "Incorrect password",
                                            QMessageBox.StandardButton.Ok)
            else:
                QMessageBox.information(self, "Warning", "Username and password must be provided",
                                        QMessageBox.StandardButton.Ok)
        except Exception as e:
            print(e)
    
    def checkPassword(self):
        self.data = self.loginController.selectData()

    def MenucloseEvent(self):
        selected_option = QMessageBox.information(self, "Warning", "Are you sure you want to exit this app?",
                                                  QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

        if selected_option == QMessageBox.StandardButton.Yes:
            self.menuFormController.closePopUpForm()
            self.afterCloseEvent()
           
       

    def afterCloseEvent(self):
        self.show()
        self.devicemanagercontroller.lbl_username.clear()
        self.menuFormController.mdiArea.closeAllSubWindows()
        # Add any additional cleanup actions here

    def checkMenuLogout(self):
        try:
            if self.menuFormController.afterCloseEvent():
                self.MenucloseEvent()
            else:
                pass
        except Exception as e:
            print(f"Logout check error: {e}")

