# Form implementation generated from reading ui file 'c:\Project\new_exim_device\Menu\form_menu.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Frm_MainWindow(object):
    def setupUi(self, Frm_MainWindow):
        Frm_MainWindow.setObjectName("Frm_MainWindow")
        Frm_MainWindow.resize(1302, 795)
        self.centralwidget = QtWidgets.QWidget(parent=Frm_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_menu = QtWidgets.QWidget(parent=self.centralwidget)
        self.main_menu.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(30, 146, 255);")
        self.main_menu.setObjectName("main_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.main_menu)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 11)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mdiArea = QtWidgets.QMdiArea(parent=self.main_menu)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout_3.addWidget(self.mdiArea)
        self.gridLayout.addWidget(self.main_menu, 0, 0, 1, 1)
        Frm_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Frm_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1302, 34))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menuManagement = QtWidgets.QMenu(parent=self.menubar)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menuManagement.setFont(font)
        self.menuManagement.setObjectName("menuManagement")
        self.menuSetting = QtWidgets.QMenu(parent=self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        self.menuReport = QtWidgets.QMenu(parent=self.menubar)
        self.menuReport.setObjectName("menuReport")
        Frm_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Frm_MainWindow)
        self.statusbar.setObjectName("statusbar")
        Frm_MainWindow.setStatusBar(self.statusbar)
        self.itm_Employees = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Employees.setObjectName("itm_Employees")
        self.itm_Users = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Users.setObjectName("itm_Users")
        self.itm_Position = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Position.setObjectName("itm_Position")
        self.itm_Roles = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Roles.setObjectName("itm_Roles")
        self.itm_Permission = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Permission.setObjectName("itm_Permission")
        self.itm_Department = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Department.setObjectName("itm_Department")
        self.itm_Company = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Company.setObjectName("itm_Company")
        self.itm_Device = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Device.setObjectName("itm_Device")
        self.itm_Suppliers = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Suppliers.setObjectName("itm_Suppliers")
        self.itm_Brand = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Brand.setObjectName("itm_Brand")
        self.itm_Categories = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Categories.setObjectName("itm_Categories")
        self.itm_Device_Location = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Device_Location.setObjectName("itm_Device_Location")
        self.itm_Device_Status = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Device_Status.setObjectName("itm_Device_Status")
        self.itm_Logout = QtGui.QAction(parent=Frm_MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.itm_Logout.setFont(font)
        self.itm_Logout.setObjectName("itm_Logout")
        self.itm_ExitFullScreen = QtGui.QAction(parent=Frm_MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.itm_ExitFullScreen.setFont(font)
        self.itm_ExitFullScreen.setObjectName("itm_ExitFullScreen")
        self.itm_Device_Management = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Device_Management.setObjectName("itm_Device_Management")
        self.itm_Report_Device = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_Report_Device.setObjectName("itm_Report_Device")
        self.itm_history = QtGui.QAction(parent=Frm_MainWindow)
        self.itm_history.setObjectName("itm_history")
        self.menuManagement.addSeparator()
        self.menuManagement.addAction(self.itm_Employees)
        self.menuManagement.addAction(self.itm_Users)
        self.menuManagement.addAction(self.itm_Position)
        self.menuManagement.addAction(self.itm_Permission)
        self.menuManagement.addAction(self.itm_Department)
        self.menuManagement.addAction(self.itm_Company)
        self.menuManagement.addSeparator()
        self.menuManagement.addAction(self.itm_Device)
        self.menuManagement.addAction(self.itm_Suppliers)
        self.menuManagement.addAction(self.itm_Brand)
        self.menuManagement.addAction(self.itm_Categories)
        self.menuManagement.addAction(self.itm_Device_Location)
        self.menuManagement.addAction(self.itm_Device_Status)
        self.menuManagement.addAction(self.itm_Device_Management)
        self.menuSetting.addAction(self.itm_Logout)
        self.menuSetting.addAction(self.itm_ExitFullScreen)
        self.menuReport.addAction(self.itm_Report_Device)
        self.menuReport.addAction(self.itm_history)
        self.menubar.addAction(self.menuManagement.menuAction())
        self.menubar.addAction(self.menuReport.menuAction())
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(Frm_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Frm_MainWindow)

    def retranslateUi(self, Frm_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Frm_MainWindow.setWindowTitle(_translate("Frm_MainWindow", "MainWindow"))
        self.menuManagement.setTitle(_translate("Frm_MainWindow", "Management"))
        self.menuSetting.setTitle(_translate("Frm_MainWindow", "Setting"))
        self.menuReport.setTitle(_translate("Frm_MainWindow", "Report"))
        self.itm_Employees.setText(_translate("Frm_MainWindow", "Employees Info"))
        self.itm_Users.setText(_translate("Frm_MainWindow", "Users Info"))
        self.itm_Position.setText(_translate("Frm_MainWindow", "Positions Info"))
        self.itm_Roles.setText(_translate("Frm_MainWindow", "Manage Roles"))
        self.itm_Permission.setText(_translate("Frm_MainWindow", "Manage Permissions"))
        self.itm_Department.setText(_translate("Frm_MainWindow", "Department Info"))
        self.itm_Company.setText(_translate("Frm_MainWindow", "Companies Info"))
        self.itm_Device.setText(_translate("Frm_MainWindow", "Devices Info"))
        self.itm_Suppliers.setText(_translate("Frm_MainWindow", "Suppliers Info"))
        self.itm_Brand.setText(_translate("Frm_MainWindow", "Brand Info"))
        self.itm_Categories.setText(_translate("Frm_MainWindow", "Device Categories "))
        self.itm_Device_Location.setText(_translate("Frm_MainWindow", "Device Location "))
        self.itm_Device_Status.setText(_translate("Frm_MainWindow", "Device Status "))
        self.itm_Logout.setText(_translate("Frm_MainWindow", "Logout"))
        self.itm_ExitFullScreen.setText(_translate("Frm_MainWindow", "exit FullScreen"))
        self.itm_Device_Management.setText(_translate("Frm_MainWindow", "Device Management"))
        self.itm_Report_Device.setText(_translate("Frm_MainWindow", "Device Report"))
        self.itm_history.setText(_translate("Frm_MainWindow", "History"))
