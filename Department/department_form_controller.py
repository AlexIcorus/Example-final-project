import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox, QHeaderView, QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Department.department_form_controller_ui import Ui_frm_company
from Department.department_controller import departmentController
from Department.department_form_popup import departmentFormPopUp


class FrmDepartmentController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_company()
        self.departmentformpopup = departmentFormPopUp()
        self.ui.setupUi(self)
        self.devicecontroller = departmentController()
        
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.departmentformpopup.ui.btn_insert
        self.btn_edit_popup = self.departmentformpopup.ui.btn_edit
        self.btn_cancel_popup = self.departmentformpopup.ui.btn_cancel
        self.btn_clear_popup = self.departmentformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_department_id = self.ui.lbl_did
        self.lbl_id_popup = self.departmentformpopup.ui.lbl_did_
        self.txt_department_name = self.departmentformpopup.ui.txt_department_name
        self.txt_remark = self.departmentformpopup.ui.txt_remark
        self.txt_search = self.departmentformpopup.ui.txt_search
             
    def initSignal(self):
        self.btn_insert.clicked.connect(self.openInsertPopUpFormDevice)
        self.btn_insert.clicked.connect(self.clearPopUp)
        self.btn_edit.clicked.connect(self.openEditPopUpFormDevice)
        self.btn_cancel_popup.clicked.connect(self.closePopUp)
        self.btn_clear_popup.clicked.connect(self.clearPopUp)
        self.btn_refresh.clicked.connect(self.loadAndShowData)
        self.btn_insert_popup.clicked.connect(self.add_info)
        self.btn_edit_popup.clicked.connect(self.updateData)
        self.txt_remark.returnPressed.connect(self.updateData)
        self.btn_edit_popup.clicked.connect(self.loadAndShowData)
        self.tbshow.itemSelectionChanged.connect(self.selectRecord)
        self.tbshow.itemSelectionChanged.connect(self.checkSelection)
        self.btn_delete.clicked.connect(self.delete_info)
        self.hideEditButton()

    def clearPopUp(self):
        self.txt_search.clear()
        self.txt_remark.clear()
        self.txt_department_name.clear()
        self.txt_department_name.setFocus()

    def closePopUp(self):
        self.departmentformpopup.close()
        self.clearPopUp()

    def setupTable(self):
        self.tbshow.setColumnCount(3)
        self.tbshow.setColumnHidden(0, True)
        
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        column_widths = [50, 200, 200]
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        for i in range(3):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)

        self.tbshow.setColumnWidth(0, 150)
        self.tbshow.setColumnWidth(1, 300)
        self.tbshow.setColumnWidth(2, 300)

    def loadAndShowData(self):
        try:
            result = self.devicecontroller.selectDepartmentData()  # Ensure this method exists and fetches data
            self.showData(result)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
    
    def showData(self, result):
        font = QFont()
        font.setPointSize(10)
        if result:
            self.tbshow.setRowCount(len(result))
            for row, info in enumerate(result):
                info_list = [
                    info.get("id", ""),
                    info.get("name_en", ""),
                    info.get("description", ""),
                ]
                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    cell_item.setFont(font)
                    self.tbshow.setItem(row, column, cell_item)
        else:
            self.tbshow.setRowCount(0)

    def hideEditButton(self):
        self.btn_edit.setHidden(True)
        self.btn_delete.setHidden(True)
        self.lbl_department_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def openInsertPopUpFormDevice(self):
        self.departmentformpopup.show()
        self.departmentformpopup.activateWindow()
        self.txt_department_name.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)

    def openEditPopUpFormDevice(self):
        self.departmentformpopup.show()
        self.departmentformpopup.activateWindow()
        self.btn_edit_popup.setHidden(False)
        self.btn_insert_popup.setHidden(True)
        self.txt_department_name.setFocus()

    def selectRecord(self):
        self.tbshow.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        self.tbshow.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: blue;
                color: white;
            }
        """)

        select_row = self.tbshow.currentRow()
        if select_row != -1:
            department_id = self.tbshow.item(select_row, 0).text().strip()
            department_name = self.tbshow.item(select_row, 1).text().strip()
            description = self.tbshow.item(select_row, 2).text().strip()
        
            self.lbl_department_id.setText(department_id)
            self.lbl_id_popup.setText(department_id)
            self.txt_department_name.setText(department_name)
            self.txt_remark.setText(description)

            self.showEditButton()
        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a device to view information.",
                                    QMessageBox.StandardButton.Ok)

    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_department_id.clear()
        self.lbl_id_popup.clear()

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()

    def add_info(self):
        try:
            device_info = self.getDepartmentInfo()
            
            if device_info is None:
                raise ValueError("No device info returned")

            
            if not device_info["department_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Department name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
                self.devicecontroller.add_info(
                    department_name=device_info["department_name"], 
                    description=device_info["description"]
                )
                self.loadAndShowData()
                self.closePopUp()
                QMessageBox.information(self, "Success", "Info added successfully.",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.openInsertPopUpFormDevice()
        
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError in add_info: {e}",
                                QMessageBox.StandardButton.Ok)
        except ValueError as e:
            QMessageBox.critical(self, "Error", f"ValueError in add_info: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in add_info: {e}",
                                QMessageBox.StandardButton.Ok)


    def updateData(self):
        try:
            device_info = self.getDepartmentInfo()
            if device_info is None:
                raise ValueError("No device info returned")

            
            if not device_info["department_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Department name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                return
                
            
            if not device_info["department_id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to update.", 
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to Update it?", 
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                update_result = self.devicecontroller.updateData(
                    department_id=device_info["department_id"],
                    department_name=device_info["department_name"],
                    description=device_info["description"]
                )

                if update_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to update the information: {update_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "Department information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()
            else:
                # Set focus back on the departmentFormPopUp form
                self.openEditPopUpFormDevice()
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in device information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            device_info = self.getDepartmentInfo()
            if not device_info["department_id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.devicecontroller.deleteData(department_id=device_info["department_id"])

                if delete_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to delete the information: {delete_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "Device information deleted successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()
        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in device information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in delete_info: {e}",
                                QMessageBox.StandardButton.Ok)

    def getDepartmentInfo(self):
        department_id = self.lbl_department_id.text().strip()
        department_name = self.txt_department_name.text().strip()
        description = self.txt_remark.text().strip()

        device_info = {
            "department_id": department_id,   
            "department_name": department_name,
            "description": description
        }
        
        return device_info
