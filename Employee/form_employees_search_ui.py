# Form implementation generated from reading ui file 'c:\Project\new_exim_device\Employee\form_employees_search.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SearchEmployee(object):
    def setupUi(self, SearchEmployee):
        SearchEmployee.setObjectName("SearchEmployee")
        SearchEmployee.resize(597, 261)
        self.centralwidget = QtWidgets.QWidget(parent=SearchEmployee)
        self.centralwidget.setObjectName("centralwidget")
        self.txt_search_popup = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txt_search_popup.setGeometry(QtCore.QRect(110, 40, 391, 51))
        self.txt_search_popup.setStyleSheet("font: 12pt \"Phetsarath OT\";")
        self.txt_search_popup.setObjectName("txt_search_popup")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 120, 411, 71))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_search_name_lastname = QtWidgets.QPushButton(parent=self.widget)
        self.btn_search_name_lastname.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_search_name_lastname.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_search_name_lastname.setBaseSize(QtCore.QSize(0, 0))
        self.btn_search_name_lastname.setStyleSheet("font: 12pt \"Phetsarath OT\";\n"
"background-color: rgb(222, 148, 110);")
        self.btn_search_name_lastname.setObjectName("btn_search_name_lastname")
        self.horizontalLayout.addWidget(self.btn_search_name_lastname)
        self.btn_search_department = QtWidgets.QPushButton(parent=self.widget)
        self.btn_search_department.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_search_department.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_search_department.setBaseSize(QtCore.QSize(0, 0))
        self.btn_search_department.setStyleSheet("font: 12pt \"Phetsarath OT\";\n"
"background-color: rgb(222, 148, 110);")
        self.btn_search_department.setObjectName("btn_search_department")
        self.horizontalLayout.addWidget(self.btn_search_department)
        self.btn_search_position = QtWidgets.QPushButton(parent=self.widget)
        self.btn_search_position.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_search_position.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_search_position.setBaseSize(QtCore.QSize(0, 0))
        self.btn_search_position.setStyleSheet("font: 12pt \"Phetsarath OT\";\n"
"background-color: rgb(222, 148, 110);")
        self.btn_search_position.setObjectName("btn_search_position")
        self.horizontalLayout.addWidget(self.btn_search_position)
        self.btn_search_cancel = QtWidgets.QPushButton(parent=self.widget)
        self.btn_search_cancel.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_search_cancel.setSizeIncrement(QtCore.QSize(0, 0))
        self.btn_search_cancel.setBaseSize(QtCore.QSize(0, 0))
        self.btn_search_cancel.setStyleSheet("font: 12pt \"Phetsarath OT\";\n"
"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.btn_search_cancel.setObjectName("btn_search_cancel")
        self.horizontalLayout.addWidget(self.btn_search_cancel)
        SearchEmployee.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SearchEmployee)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 597, 26))
        self.menubar.setObjectName("menubar")
        SearchEmployee.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SearchEmployee)
        self.statusbar.setObjectName("statusbar")
        SearchEmployee.setStatusBar(self.statusbar)

        self.retranslateUi(SearchEmployee)
        QtCore.QMetaObject.connectSlotsByName(SearchEmployee)

    def retranslateUi(self, SearchEmployee):
        _translate = QtCore.QCoreApplication.translate
        SearchEmployee.setWindowTitle(_translate("SearchEmployee", "Search Form"))
        self.btn_search_name_lastname.setText(_translate("SearchEmployee", "ຄົ້ນຫາ1"))
        self.btn_search_department.setText(_translate("SearchEmployee", "ຄົ້ນຫາ2"))
        self.btn_search_position.setText(_translate("SearchEmployee", "ຄົ້ນຫາ3"))
        self.btn_search_cancel.setText(_translate("SearchEmployee", "ຍົກເລີກ"))
