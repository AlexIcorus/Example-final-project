# Import necessary modules
import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QFrame, QMessageBox, QTableWidgetItem
from PyQt6.QtCore import pyqtSlot

from PyQt6.QtGui import QIntValidator


from Auth.login_form_controller import LoginFormController







if __name__ == '__main__':

    
    app = QApplication(sys.argv)
    window = LoginFormController()
    window.show()
    sys.exit(app.exec())
    


































               










