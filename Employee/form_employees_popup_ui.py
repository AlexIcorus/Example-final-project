# Form implementation generated from reading ui file 'c:\Project\new_exim_device\Employee\form_employees_popup.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_employee_popup(object):
    def setupUi(self, frm_employee_popup):
        frm_employee_popup.setObjectName("frm_employee_popup")
        frm_employee_popup.resize(1455, 717)
        self.centralwidget = QtWidgets.QWidget(parent=frm_employee_popup)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, -1, -1, 7)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_main = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_main.setStyleSheet("color: rgb(255, 213, 126);\n"
"background-color: rgb(40, 40, 40);")
        self.frame_main.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_main.setObjectName("frame_main")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_main)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget = QtWidgets.QWidget(parent=self.frame_main)
        self.widget.setObjectName("widget")
        self.label_13 = QtWidgets.QLabel(parent=self.widget)
        self.label_13.setGeometry(QtCore.QRect(20, 500, 211, 41))
        self.label_13.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_13.setObjectName("label_13")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 480, 807, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QtWidgets.QWidget(parent=self.verticalLayoutWidget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.rb_Male = QtWidgets.QRadioButton(parent=self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.rb_Male.setFont(font)
        self.rb_Male.setStyleSheet("font: 12pt \"Phetsarath OT\";")
        self.rb_Male.setObjectName("rb_Male")
        self.horizontalLayout_2.addWidget(self.rb_Male)
        self.rb_Female = QtWidgets.QRadioButton(parent=self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        self.rb_Female.setFont(font)
        self.rb_Female.setIconSize(QtCore.QSize(20, 20))
        self.rb_Female.setObjectName("rb_Female")
        self.horizontalLayout_2.addWidget(self.rb_Female)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(50)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_insert = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_insert.setStyleSheet("background-color: rgb(0, 127, 108);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_insert.setIconSize(QtCore.QSize(20, 20))
        self.btn_insert.setObjectName("btn_insert")
        self.horizontalLayout_3.addWidget(self.btn_insert)
        self.btn_edit = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_edit.setStyleSheet("background-color: rgb(0, 127, 108);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_edit.setIconSize(QtCore.QSize(25, 25))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout_3.addWidget(self.btn_edit)
        self.btn_clear_form = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_clear_form.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_clear_form.setIconSize(QtCore.QSize(25, 25))
        self.btn_clear_form.setObjectName("btn_clear_form")
        self.horizontalLayout_3.addWidget(self.btn_clear_form)
        self.btn_cancel = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.btn_cancel.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_3.addWidget(self.btn_cancel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.lbl_id_popup = QtWidgets.QLabel(parent=self.widget)
        self.lbl_id_popup.setGeometry(QtCore.QRect(1120, 420, 55, 16))
        self.lbl_id_popup.setStyleSheet("color: rgb(255, 255, 255);")
        self.lbl_id_popup.setObjectName("lbl_id_popup")
        self.widget_Form = QtWidgets.QWidget(parent=self.widget)
        self.widget_Form.setGeometry(QtCore.QRect(20, 20, 813, 471))
        self.widget_Form.setStyleSheet("")
        self.widget_Form.setObjectName("widget_Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setContentsMargins(0, 7, 0, 1)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget_4)
        self.label.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txt_emp_code = QtWidgets.QLineEdit(parent=self.widget_4)
        self.txt_emp_code.setEnabled(True)
        self.txt_emp_code.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.txt_emp_code.setText("")
        self.txt_emp_code.setObjectName("txt_emp_code")
        self.horizontalLayout.addWidget(self.txt_emp_code)
        self.verticalLayout.addWidget(self.widget_4)
        self.widgets_vld_name = QtWidgets.QWidget(parent=self.widget_Form)
        self.widgets_vld_name.setObjectName("widgets_vld_name")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widgets_vld_name)
        self.horizontalLayout_9.setContentsMargins(180, 0, 310, 0)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.vld_emp_code = QtWidgets.QLabel(parent=self.widgets_vld_name)
        self.vld_emp_code.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_emp_code.setObjectName("vld_emp_code")
        self.horizontalLayout_9.addWidget(self.vld_emp_code)
        self.verticalLayout.addWidget(self.widgets_vld_name)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 7, 0, 1)
        self.horizontalLayout_4.setSpacing(40)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_2.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.txt_name = QtWidgets.QLineEdit(parent=self.widget_5)
        self.txt_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";\n"
"color: rgb(0, 0, 0);")
        self.txt_name.setText("")
        self.txt_name.setObjectName("txt_name")
        self.horizontalLayout_4.addWidget(self.txt_name)
        self.btn_search_name = QtWidgets.QPushButton(parent=self.widget_5)
        self.btn_search_name.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_search_name.setStyleSheet("background-color: rgb(255, 213, 126);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_search_name.setText("")
        self.btn_search_name.setIconSize(QtCore.QSize(40, 40))
        self.btn_search_name.setObjectName("btn_search_name")
        self.horizontalLayout_4.addWidget(self.btn_search_name)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setContentsMargins(180, 0, 270, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.vld_name = QtWidgets.QLabel(parent=self.widget_10)
        self.vld_name.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_name.setObjectName("vld_name")
        self.horizontalLayout_10.addWidget(self.vld_name)
        self.verticalLayout.addWidget(self.widget_10)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_5.setContentsMargins(0, 7, 0, 1)
        self.horizontalLayout_5.setSpacing(45)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_9.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_5.addWidget(self.label_9)
        self.txt_surname = QtWidgets.QLineEdit(parent=self.widget_6)
        self.txt_surname.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt;\n"
"color: rgb(0, 0, 0);")
        self.txt_surname.setText("")
        self.txt_surname.setObjectName("txt_surname")
        self.horizontalLayout_5.addWidget(self.txt_surname)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_11 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_13.setContentsMargins(180, 0, 270, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.vld_last_name = QtWidgets.QLabel(parent=self.widget_11)
        self.vld_last_name.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_last_name.setObjectName("vld_last_name")
        self.horizontalLayout_13.addWidget(self.vld_last_name)
        self.verticalLayout.addWidget(self.widget_11)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 1)
        self.horizontalLayout_6.setSpacing(95)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_7)
        self.label_3.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.txt_phone = QtWidgets.QLineEdit(parent=self.widget_7)
        self.txt_phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt ;\n"
"color: rgb(0, 0, 0);")
        self.txt_phone.setText("")
        self.txt_phone.setObjectName("txt_phone")
        self.horizontalLayout_6.addWidget(self.txt_phone)
        self.verticalLayout.addWidget(self.widget_7)
        self.widget_12 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_12.setObjectName("widget_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_12)
        self.horizontalLayout_14.setContentsMargins(200, 0, 270, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.vld_last_name_5 = QtWidgets.QLabel(parent=self.widget_12)
        self.vld_last_name_5.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_last_name_5.setText("")
        self.vld_last_name_5.setObjectName("vld_last_name_5")
        self.horizontalLayout_14.addWidget(self.vld_last_name_5)
        self.verticalLayout.addWidget(self.widget_12)
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_7.setContentsMargins(0, 7, 0, 1)
        self.horizontalLayout_7.setSpacing(110)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_8)
        self.label_4.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.txt_email = QtWidgets.QLineEdit(parent=self.widget_8)
        self.txt_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt ;\n"
"color: rgb(0, 0, 0);")
        self.txt_email.setText("")
        self.txt_email.setObjectName("txt_email")
        self.horizontalLayout_7.addWidget(self.txt_email)
        self.verticalLayout.addWidget(self.widget_8)
        self.widget_13 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_15.setContentsMargins(200, 0, 270, 0)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.vld_last_name_6 = QtWidgets.QLabel(parent=self.widget_13)
        self.vld_last_name_6.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_last_name_6.setText("")
        self.vld_last_name_6.setObjectName("vld_last_name_6")
        self.horizontalLayout_15.addWidget(self.vld_last_name_6)
        self.verticalLayout.addWidget(self.widget_13)
        self.widget_9 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_8.setContentsMargins(0, 7, 0, 1)
        self.horizontalLayout_8.setSpacing(70)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_9)
        self.label_5.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.txt_address = QtWidgets.QLineEdit(parent=self.widget_9)
        self.txt_address.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt;\n"
"color: rgb(0, 0, 0);")
        self.txt_address.setText("")
        self.txt_address.setObjectName("txt_address")
        self.horizontalLayout_8.addWidget(self.txt_address)
        self.verticalLayout.addWidget(self.widget_9)
        self.widget_14 = QtWidgets.QWidget(parent=self.widget_Form)
        self.widget_14.setObjectName("widget_14")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.widget_14)
        self.horizontalLayout_16.setContentsMargins(200, 0, 270, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.vld_last_name_7 = QtWidgets.QLabel(parent=self.widget_14)
        self.vld_last_name_7.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_last_name_7.setText("")
        self.vld_last_name_7.setObjectName("vld_last_name_7")
        self.horizontalLayout_16.addWidget(self.vld_last_name_7)
        self.verticalLayout.addWidget(self.widget_14)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 3)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 3)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 3)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 3)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 3)
        self.verticalLayout.setStretch(11, 1)
        self.widget_17 = QtWidgets.QWidget(parent=self.widget)
        self.widget_17.setGeometry(QtCore.QRect(880, 30, 517, 239))
        self.widget_17.setObjectName("widget_17")
        self.formLayout = QtWidgets.QFormLayout(self.widget_17)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(0)
        self.formLayout.setObjectName("formLayout")
        self.widget_16 = QtWidgets.QWidget(parent=self.widget_17)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(10)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_11 = QtWidgets.QLabel(parent=self.widget_16)
        self.label_11.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_19.addWidget(self.label_11)
        self.cmb_company = QtWidgets.QComboBox(parent=self.widget_16)
        self.cmb_company.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.cmb_company.setObjectName("cmb_company")
        self.horizontalLayout_19.addWidget(self.cmb_company)
        self.widget_22 = QtWidgets.QWidget(parent=self.widget_16)
        self.widget_22.setMinimumSize(QtCore.QSize(50, 0))
        self.widget_22.setMaximumSize(QtCore.QSize(50, 50))
        self.widget_22.setObjectName("widget_22")
        self.horizontalLayout_19.addWidget(self.widget_22)
        self.horizontalLayout_19.setStretch(0, 2)
        self.horizontalLayout_19.setStretch(1, 4)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.widget_16)
        self.widget_21 = QtWidgets.QWidget(parent=self.widget_17)
        self.widget_21.setObjectName("widget_21")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.widget_21)
        self.horizontalLayout_23.setContentsMargins(180, 0, 0, 10)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.vld_company = QtWidgets.QLabel(parent=self.widget_21)
        self.vld_company.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_company.setObjectName("vld_company")
        self.horizontalLayout_23.addWidget(self.vld_company)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_21)
        self.widget_15 = QtWidgets.QWidget(parent=self.widget_17)
        self.widget_15.setObjectName("widget_15")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.widget_15)
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_15)
        self.label_10.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.cmb_department = QtWidgets.QComboBox(parent=self.widget_15)
        self.cmb_department.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.cmb_department.setObjectName("cmb_department")
        self.horizontalLayout_18.addWidget(self.cmb_department)
        self.btn_search_department = QtWidgets.QPushButton(parent=self.widget_15)
        self.btn_search_department.setMaximumSize(QtCore.QSize(50, 40))
        self.btn_search_department.setStyleSheet("background-color: rgb(255, 213, 126);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_search_department.setText("")
        self.btn_search_department.setIconSize(QtCore.QSize(40, 40))
        self.btn_search_department.setObjectName("btn_search_department")
        self.horizontalLayout_18.addWidget(self.btn_search_department)
        self.horizontalLayout_18.setStretch(0, 2)
        self.horizontalLayout_18.setStretch(1, 4)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.widget_15)
        self.widget_20 = QtWidgets.QWidget(parent=self.widget_17)
        self.widget_20.setObjectName("widget_20")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.widget_20)
        self.horizontalLayout_22.setContentsMargins(180, 0, 0, 10)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.vld_department = QtWidgets.QLabel(parent=self.widget_20)
        self.vld_department.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_department.setObjectName("vld_department")
        self.horizontalLayout_22.addWidget(self.vld_department)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_20)
        self.widget_18 = QtWidgets.QWidget(parent=self.widget_17)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_20.setContentsMargins(180, 0, 0, 10)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.vld_position = QtWidgets.QLabel(parent=self.widget_18)
        self.vld_position.setStyleSheet("background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 0, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.vld_position.setObjectName("vld_position")
        self.horizontalLayout_20.addWidget(self.vld_position)
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.ItemRole.LabelRole, self.widget_18)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_17)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setSpacing(10)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_7.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_17.addWidget(self.label_7)
        self.cmb_position = QtWidgets.QComboBox(parent=self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cmb_position.setFont(font)
        self.cmb_position.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.cmb_position.setObjectName("cmb_position")
        self.horizontalLayout_17.addWidget(self.cmb_position)
        self.btn_search_position = QtWidgets.QPushButton(parent=self.widget_3)
        self.btn_search_position.setMaximumSize(QtCore.QSize(50, 40))
        self.btn_search_position.setStyleSheet("background-color: rgb(255, 213, 126);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_search_position.setText("")
        self.btn_search_position.setIconSize(QtCore.QSize(40, 40))
        self.btn_search_position.setObjectName("btn_search_position")
        self.horizontalLayout_17.addWidget(self.btn_search_position)
        self.horizontalLayout_17.setStretch(0, 2)
        self.horizontalLayout_17.setStretch(1, 4)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.widget_3)
        self.widget_19 = QtWidgets.QWidget(parent=self.widget)
        self.widget_19.setGeometry(QtCore.QRect(1200, 400, 247, 46))
        self.widget_19.setObjectName("widget_19")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.widget_19)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.gridLayout_3.addWidget(self.widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_main, 0, 0, 1, 1)
        frm_employee_popup.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=frm_employee_popup)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1455, 26))
        self.menubar.setObjectName("menubar")
        frm_employee_popup.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=frm_employee_popup)
        self.statusbar.setObjectName("statusbar")
        frm_employee_popup.setStatusBar(self.statusbar)

        self.retranslateUi(frm_employee_popup)
        QtCore.QMetaObject.connectSlotsByName(frm_employee_popup)

    def retranslateUi(self, frm_employee_popup):
        _translate = QtCore.QCoreApplication.translate
        frm_employee_popup.setWindowTitle(_translate("frm_employee_popup", "Employee Form"))
        self.label_13.setText(_translate("frm_employee_popup", "Gender"))
        self.rb_Male.setText(_translate("frm_employee_popup", "Male"))
        self.rb_Female.setText(_translate("frm_employee_popup", "Female"))
        self.btn_insert.setText(_translate("frm_employee_popup", "ບັນທຶກ"))
        self.btn_edit.setText(_translate("frm_employee_popup", "ເເກ້ໄຂຂໍ້ມູນ"))
        self.btn_clear_form.setText(_translate("frm_employee_popup", "ລ້າງ"))
        self.btn_cancel.setText(_translate("frm_employee_popup", "ຍົກເລີກ"))
        self.lbl_id_popup.setText(_translate("frm_employee_popup", "TextLabel"))
        self.label.setText(_translate("frm_employee_popup", "Emp_code"))
        self.vld_emp_code.setText(_translate("frm_employee_popup", " * Please enter your employee code"))
        self.label_2.setText(_translate("frm_employee_popup", "First Name:"))
        self.vld_name.setText(_translate("frm_employee_popup", " * Please enter your firstname"))
        self.label_9.setText(_translate("frm_employee_popup", "Last Name"))
        self.vld_last_name.setText(_translate("frm_employee_popup", " * Please enter your lastname"))
        self.label_3.setText(_translate("frm_employee_popup", "Phone:"))
        self.label_4.setText(_translate("frm_employee_popup", "Email:"))
        self.label_5.setText(_translate("frm_employee_popup", "Address:"))
        self.label_11.setText(_translate("frm_employee_popup", "Company"))
        self.vld_company.setText(_translate("frm_employee_popup", " * Please select company position"))
        self.label_10.setText(_translate("frm_employee_popup", "Department"))
        self.vld_department.setText(_translate("frm_employee_popup", " * Please select department"))
        self.vld_position.setText(_translate("frm_employee_popup", " * Please select employee position"))
        self.label_7.setText(_translate("frm_employee_popup", "Position"))