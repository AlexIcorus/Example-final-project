import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Device_location.device_location_form_controller_ui import Ui_frm_device_location
from Device_location.device_location_controller import deviceLocationController
from Device_location.device_location_form_popup import devicelocationFormPopUp


class FrmDeviceLocationController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_device_location()
        self.device_locationformpopup = devicelocationFormPopUp()
        self.ui.setupUi(self)
        self.devicecontroller =deviceLocationController()
        
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
      
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.device_locationformpopup.ui.btn_insert
        self.btn_edit_popup = self.device_locationformpopup.ui.btn_edit
        self.btn_cancel_popup = self.device_locationformpopup.ui.btn_cancel
        self.btn_clear_popup = self.device_locationformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_device_location_id = self.ui.lbl_did
        self.lbl_id_popup = self.device_locationformpopup.ui.lbl_did_
        self.txt_device_location_name = self.device_locationformpopup.ui.txt_device_location
        self.txt_remark = self.device_locationformpopup.ui.txt_remark
        self.txt_search = self.device_locationformpopup.ui.txt_search
        self.txt_address = self.device_locationformpopup.ui.txt_address
       
    def initSignal(self):
        self.btn_insert.clicked.connect(self.openInsertPopUpFormDevice)
        self.btn_insert.clicked.connect(self.clearPopUp)
        self.btn_edit.clicked.connect(self.openEditPopUpFormDevice)
        self.btn_cancel_popup.clicked.connect(self.closePopUp)
        self.btn_clear_popup.clicked.connect(self.clearPopUp)
        self.btn_refresh.clicked.connect(self.loadAndShowData)
        self.btn_insert_popup.clicked.connect(self.add_info)
        self.btn_edit_popup.clicked.connect(self.updateData)
        self.btn_edit_popup.clicked.connect(self.loadAndShowData)
        self.tbshow.itemSelectionChanged.connect(self.selectRecord)
        self.tbshow.itemSelectionChanged.connect(self.checkSelection)
        self.btn_delete.clicked.connect(self.delete_info)
        self.hideEditButton()

    def clearPopUp(self):
        self.txt_search.clear()
        self.txt_remark.clear()
        self.txt_address.clear()
        self.txt_device_location_name.clear()
        self.txt_device_location_name.setFocus()

    def closePopUp(self):
        self.device_locationformpopup.close()
        self.clearPopUp()


    def setupTable(self):
        self.tbshow.setColumnCount(4)
        self.tbshow.setColumnHidden(0, True)
        
     
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
     
        column_widths = [50, 200, 200,200]
      
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        for i in range(3):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)

        self.tbshow.setColumnWidth(0, 150)
        self.tbshow.setColumnWidth(1, 300)
        self.tbshow.setColumnWidth(2, 300)
        self.tbshow.setColumnWidth(3, 300)


       
    
    

    def loadAndShowData(self):

        try:
            result = self.devicecontroller.selectDeviceLocationData()  # Ensure this method exists and fetches data
            self.showData(result)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
    
    def showData(self, result):
        
        font = QFont()
        font.setPointSize(10)  # Set font size to 8px
        if result:
            self.tbshow.setRowCount(len(result))
            for row, info in enumerate(result):
                info_list = [
                    info.get("device_location_id", ""),
                    info.get("device_location_name", ""),
                    info.get("address", ""),
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
        self.lbl_device_location_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def openInsertPopUpFormDevice(self):
        self.device_locationformpopup.show()
        self.device_locationformpopup.activateWindow()
        self.txt_device_location_name.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)

    def openEditPopUpFormDevice(self):
        self.device_locationformpopup.show()
        self.device_locationformpopup.activateWindow()
        self.btn_edit_popup.setHidden(False)
        self.btn_insert_popup.setHidden(True)
        self.txt_device_location_name.setFocus()

    def selectRecord(self):
        self.tbshow.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        
        # Set stylesheet for selected row (optional, for visual feedback)
        self.tbshow.setStyleSheet("""
            QTableWidget::item:selected {
                background-color: blue;
                color: white;
            }
        """)

        select_row = self.tbshow.currentRow()
        if select_row != -1:
            # Retrieve the values from the selected row
            device_location_id = self.tbshow.item(select_row, 0).text().strip()
            device_location_name = self.tbshow.item(select_row, 1).text().strip()
            address = self.tbshow.item(select_row, 2).text().strip()
            description = self.tbshow.item(select_row, 3).text().strip()
        

            # Update the labels and combo boxes with the selected row data
            self.lbl_device_location_id.setText(device_location_id)
            self.lbl_id_popup.setText(device_location_id)
            self.txt_device_location_name.setText(device_location_name)
            self.txt_address.setText(address)
            self.txt_remark.setText(description)

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a device to view information.",
                                    QMessageBox.StandardButton.Ok)


    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_device_location_id.clear()
        self.lbl_id_popup.clear()

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()


    def add_info(self):
        try:
            device_info = self.getDeviceLocationInfo()
            
            if device_info is None:
                raise ValueError("No device info returned")

            
            if not device_info["device_location_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Device Location name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return
            
            if not device_info["address"].strip():
                QMessageBox.warning(self, "Validation Error", "Address must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
                if device_info is None:
                    raise ValueError("No device info returned")

                print(f'Device info Here: {device_info}')  # Debug line

                # Check if all IDs are valid
                if not device_info["device_location_id"] :
                    self.devicecontroller.add_info(
                        device_location_name=device_info["device_location_name"], 
                        address=device_info["address"], 
                        description =device_info["description"]

                    )
                    print('Info added successfully.')
                    self.loadAndShowData()
                    self.closePopUp()
                    QMessageBox.information(self,"Success", "Info added successfully.",
                                            QMessageBox.StandardButton.Ok)
                else:
    
                    QMessageBox.warning(self,"Warning" , "Please Checking Your Form",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.openInsertPopUpFormDevice()

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')






    def updateData(self):
        
        try:
            device_info = self.getDeviceLocationInfo()
            if device_info is None:
                raise ValueError("No device info returned")

            
            if not device_info["device_location_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Device Location name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                return
            
            if not device_info["address"].strip():
                QMessageBox.warning(self, "Validation Error", "Address must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                return

            # Ensure the brand_id is available before proceeding with the update
            if not device_info["device_location_id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                # Perform the update operation
                update_result = self.devicecontroller.updateData(
                    device_location_id=device_info["device_location_id"],
                    device_location_name=device_info["device_location_name"],
                    address=device_info["address"], 
                    description=device_info["description"]
                )

                if update_result:
                    
                    QMessageBox.information(self, "Warning",
                                            f"Fail to update the information: {update_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "device_location information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
            else:
                self.openEditPopUpFormDevice()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in device information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            device_info = self.getDeviceLocationInfo()

            if not device_info["device_location_id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.devicecontroller.deleteData(device_location_id=device_info["device_location_id"])

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

    def getDeviceLocationInfo(self):
        device_location_id = self.lbl_device_location_id.text().strip()
        device_location_name = self.txt_device_location_name.text().strip()
        address = self.txt_address.text().strip()
        description = self.txt_remark.text().strip()


        device_info = {
            "device_location_id": device_location_id,   
            "device_location_name": device_location_name,
            "address": address,
            "description": description
  
        }

        print('Device Data:', device_info)  # Debug line
        return device_info



    
    