# Form implementation generated from reading ui file 'c:\Project\new_exim_device\Supplier\frm_popup_supplier.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_frm_popup_supplier(object):
    def setupUi(self, frm_popup_supplier):
        frm_popup_supplier.setObjectName("frm_popup_supplier")
        frm_popup_supplier.resize(1122, 660)
        self.gridLayout = QtWidgets.QGridLayout(frm_popup_supplier)
        self.gridLayout.setContentsMargins(-1, 11, -1, 11)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=frm_popup_supplier)
        self.frame.setStyleSheet("color: rgb(255, 213, 126);\n"
"background-color: rgb(202, 202, 202);\n"
"background-color: rgb(76, 76, 76);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.lbl_ID = QtWidgets.QLabel(parent=self.frame)
        self.lbl_ID.setGeometry(QtCore.QRect(1150, 50, 61, 31))
        self.lbl_ID.setStyleSheet("color: rgb(68, 80, 105);")
        self.lbl_ID.setText("")
        self.lbl_ID.setObjectName("lbl_ID")
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setGeometry(QtCore.QRect(690, 0, 372, 75))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.txt_search = QtWidgets.QLineEdit(parent=self.widget)
        self.txt_search.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";\n"
"color: rgb(0, 0, 0);")
        self.txt_search.setObjectName("txt_search")
        self.horizontalLayout.addWidget(self.txt_search)
        self.btn_search = QtWidgets.QPushButton(parent=self.widget)
        self.btn_search.setStyleSheet("background-color: rgb(255, 213, 126);\n"
"color: rgb(0, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Project\\new_exim_device\\Supplier\\../../../Users/AlexP/PycharmProjects/pythonProject/PythonPOS/icon/search-alt-regular-60.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QtCore.QSize(40, 40))
        self.btn_search.setObjectName("btn_search")
        self.horizontalLayout.addWidget(self.btn_search)
        self.txt_address = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_address.setGeometry(QtCore.QRect(240, 110, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.txt_address.setFont(font)
        self.txt_address.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_address.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.txt_address.setText("")
        self.txt_address.setDragEnabled(False)
        self.txt_address.setPlaceholderText("")
        self.txt_address.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_address.setObjectName("txt_address")
        self.label_18 = QtWidgets.QLabel(parent=self.frame)
        self.label_18.setGeometry(QtCore.QRect(20, 110, 161, 41))
        self.label_18.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_18.setObjectName("label_18")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(520, 420, 541, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_insert = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_insert.setEnabled(True)
        self.btn_insert.setStyleSheet("background-color: rgb(0, 127, 108);\n"
"color: rgb(255, 255, 255);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_insert.setIconSize(QtCore.QSize(20, 20))
        self.btn_insert.setObjectName("btn_insert")
        self.horizontalLayout_2.addWidget(self.btn_insert)
        self.btn_edit = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_edit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 127);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_edit.setIconSize(QtCore.QSize(25, 25))
        self.btn_edit.setObjectName("btn_edit")
        self.horizontalLayout_2.addWidget(self.btn_edit)
        self.btn_clear = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_clear.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_clear.setIconSize(QtCore.QSize(25, 25))
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.btn_cancel = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        self.btn_cancel.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 18pt \"Phetsarath OT\";")
        self.btn_cancel.setIconSize(QtCore.QSize(25, 25))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.lbl_did_ = QtWidgets.QLabel(parent=self.frame)
        self.lbl_did_.setGeometry(QtCore.QRect(1110, 100, 81, 41))
        self.lbl_did_.setStyleSheet("color: rgb(1, 114, 127);\n"
"color: rgb(255, 0, 0);")
        self.lbl_did_.setText("")
        self.lbl_did_.setObjectName("lbl_did_")
        self.label_22 = QtWidgets.QLabel(parent=self.frame)
        self.label_22.setGeometry(QtCore.QRect(20, 60, 221, 41))
        self.label_22.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_22.setObjectName("label_22")
        self.txt_supplier = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_supplier.setGeometry(QtCore.QRect(240, 60, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.txt_supplier.setFont(font)
        self.txt_supplier.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_supplier.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.txt_supplier.setText("")
        self.txt_supplier.setDragEnabled(False)
        self.txt_supplier.setPlaceholderText("")
        self.txt_supplier.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_supplier.setObjectName("txt_supplier")
        self.txt_remark = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_remark.setGeometry(QtCore.QRect(240, 310, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.txt_remark.setFont(font)
        self.txt_remark.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_remark.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.txt_remark.setText("")
        self.txt_remark.setDragEnabled(False)
        self.txt_remark.setPlaceholderText("")
        self.txt_remark.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_remark.setObjectName("txt_remark")
        self.label_19 = QtWidgets.QLabel(parent=self.frame)
        self.label_19.setGeometry(QtCore.QRect(20, 310, 161, 41))
        self.label_19.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_19.setObjectName("label_19")
        self.txt_fax = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_fax.setGeometry(QtCore.QRect(240, 210, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.txt_fax.setFont(font)
        self.txt_fax.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_fax.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.txt_fax.setText("")
        self.txt_fax.setDragEnabled(False)
        self.txt_fax.setPlaceholderText("")
        self.txt_fax.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_fax.setObjectName("txt_fax")
        self.label_20 = QtWidgets.QLabel(parent=self.frame)
        self.label_20.setGeometry(QtCore.QRect(20, 210, 161, 41))
        self.label_20.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.frame)
        self.label_21.setGeometry(QtCore.QRect(20, 160, 161, 41))
        self.label_21.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_21.setObjectName("label_21")
        self.txt_phone = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_phone.setGeometry(QtCore.QRect(240, 160, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.txt_phone.setFont(font)
        self.txt_phone.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_phone.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.txt_phone.setText("")
        self.txt_phone.setDragEnabled(False)
        self.txt_phone.setPlaceholderText("")
        self.txt_phone.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_phone.setObjectName("txt_phone")
        self.label_23 = QtWidgets.QLabel(parent=self.frame)
        self.label_23.setGeometry(QtCore.QRect(20, 260, 161, 41))
        self.label_23.setStyleSheet("font: 18pt \"Phetsarath OT\";\n"
"color: rgb(255, 213, 126);\n"
"")
        self.label_23.setObjectName("label_23")
        self.txt_email = QtWidgets.QLineEdit(parent=self.frame)
        self.txt_email.setGeometry(QtCore.QRect(240, 260, 371, 41))
        font = QtGui.QFont()
        font.setFamily("Phetsarath OT")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferAntialias)
        self.txt_email.setFont(font)
        self.txt_email.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.txt_email.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Phetsarath OT\";")
        self.txt_email.setText("")
        self.txt_email.setDragEnabled(False)
        self.txt_email.setPlaceholderText("")
        self.txt_email.setCursorMoveStyle(QtCore.Qt.CursorMoveStyle.LogicalMoveStyle)
        self.txt_email.setObjectName("txt_email")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 2)

        self.retranslateUi(frm_popup_supplier)
        QtCore.QMetaObject.connectSlotsByName(frm_popup_supplier)

    def retranslateUi(self, frm_popup_supplier):
        _translate = QtCore.QCoreApplication.translate
        frm_popup_supplier.setWindowTitle(_translate("frm_popup_supplier", "Form Supplier"))
        self.label_18.setText(_translate("frm_popup_supplier", "Address"))
        self.btn_insert.setText(_translate("frm_popup_supplier", " ເພີ່ມຂໍ້ມູນ"))
        self.btn_edit.setText(_translate("frm_popup_supplier", "ແກ້ໄຂ"))
        self.btn_clear.setText(_translate("frm_popup_supplier", "ລ້າງ"))
        self.btn_cancel.setText(_translate("frm_popup_supplier", "ຍົກເລີກ"))
        self.label_22.setText(_translate("frm_popup_supplier", "Supplier"))
        self.label_19.setText(_translate("frm_popup_supplier", "Description"))
        self.label_20.setText(_translate("frm_popup_supplier", "Fax"))
        self.label_21.setText(_translate("frm_popup_supplier", "Phone"))
        self.label_23.setText(_translate("frm_popup_supplier", "Email"))
