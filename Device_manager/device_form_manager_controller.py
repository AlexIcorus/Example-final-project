import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Device_manager.device_manager_form_controller_ui import Ui_frm_Device
from Device_manager.device_manager_controller import DeviceManageController
from Device_manager.device_manager_form_popup import DeviceManagerFormPopUp
from History.device_history_controller import DeviceHistoryController
from Device_info.device_form_controller import DeviceController




class FrmDeviceManageController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_Device()
        self.deviceformpopup = DeviceManagerFormPopUp()
        self.devicehistorycontroller = DeviceHistoryController()
        self.ui.setupUi(self)
        self.devicemanagercontroller = DeviceManageController()
        self.devicecontroller = DeviceController()
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
        self.getdeviceStatus()
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.deviceformpopup.ui.btn_insert
        self.btn_edit_popup = self.deviceformpopup.ui.btn_edit
        self.btn_cancel_popup = self.deviceformpopup.ui.btn_cancel
        self.btn_clear_popup = self.deviceformpopup.ui.btn_clear
        self.btn_search_device_name = self.deviceformpopup.ui.btn_search_device_name
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_device_id = self.ui.lbl_did
        self.lbl_id_popup = self.deviceformpopup.ui.lbl_did_
        self.txt_remark = self.deviceformpopup.ui.txt_remark
        self.cmb_device_name = self.deviceformpopup.ui.cmb_device_name
        self.cmb_status = self.deviceformpopup.ui.cmb_status
        self.txt_username = self.deviceformpopup.ui.txt_username
        self.cmb_device_location = self.deviceformpopup.ui.cmb_location
        self.lbl_serial_number = self.deviceformpopup.ui.lbl_serial_number
        self.cmb_used_by = self.deviceformpopup.ui.cmb_used_by
        self.lbl_username = self.ui.lbl_user
        self.lbl_title = self.ui.lbl_title  
        self.lbl_remark = self.deviceformpopup.ui.label_18

        
       
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
        self.cmb_device_name.currentIndexChanged.connect(self.getDeviceID)
        self.btn_delete.clicked.connect(self.delete_info)
        self.getSameData()

        self.hideEditButton()

    def clearPopUp(self):
        self.getdeviceStatus()
        self.lbl_serial_number.clear()
        self.txt_remark.clear()
     


    def closePopUp(self):
        self.deviceformpopup.close()
        print("hii")
        return
        self.clearPopUp()


    def setupTable(self):
        self.tbshow.setColumnCount(7)
        self.tbshow.setColumnHidden(0, True)
        self.lbl_remark.setHidden(True)
        self.txt_remark.setHidden(True)
        
     
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
     
        column_widths = [50, 200, 200, 200, 100, 150, 70]
      
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        for i in range(7):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)

        self.tbshow.setColumnWidth(1, 150)
        self.tbshow.setColumnWidth(2, 200)
        self.tbshow.setColumnWidth(3, 200)
        self.tbshow.setColumnWidth(4, 150)
        self.tbshow.setColumnWidth(5, 290)
        self.tbshow.setColumnWidth(6, 220)

       
    def setUsername(self,user):
        self.txt_username.setText(user[0]['username'])
        self.lbl_username.setText('User: ( '+ user[0]['name']+' )')
        self.txt_username.setHidden(True)

    def loadAndShowData(self):

        try:
            result = self.devicemanagercontroller.selectDeviceData()  # Ensure this method exists and fetches data
            self.showData(result)
            print(result)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
    
    def showData(self, result):
        
        font = QFont()
        font.setPointSize(10)  # Set font size to 8px
        if result:
            self.tbshow.setRowCount(len(result))
            for row, info in enumerate(result):
                info_list = [
                    info.get("id", ""),
                    info.get("device_name", ""),
                    info.get("serial_number", ""),
                    info.get("status_name", ""), 
                    info.get("device_location_name", ""),                     
                    info.get("used_by",""), 
                    info.get("device_remark", ""),        
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
        self.lbl_device_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def openInsertPopUpFormDevice(self):
        self.deviceformpopup.show()
        self.deviceformpopup.activateWindow()
        self.txt_username.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)

    def openEditPopUpFormDevice(self):
        self.deviceformpopup.show()
        self.deviceformpopup.activateWindow()
        self.btn_edit_popup.setHidden(False)
        self.btn_insert_popup.setHidden(True)
      

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
            device_manager_id = self.tbshow.item(select_row, 0).text().strip()
            device_name = self.tbshow.item(select_row, 1).text().strip()
            serial_number = self.tbshow.item(select_row, 2).text().strip()
            status_name = self.tbshow.item(select_row, 3).text().strip()
            device_location = self.tbshow.item(select_row, 4).text().strip()
            used_by = self.tbshow.item(select_row, 5).text().strip() 
            remark = self.tbshow.item(select_row, 6).text().strip()
            # Update the labels and combo boxes with the selected row data
            self.lbl_device_id.setText(device_manager_id)
            self.lbl_id_popup.setText(device_manager_id)
            
            # Set the combo boxes based on the selected row data using setCurrentText
            self.cmb_device_name.setCurrentText(device_name)
            self.lbl_serial_number.setText(serial_number)
            self.cmb_status.setCurrentText(status_name)
            self.cmb_device_location.setCurrentText(device_location)
            self.cmb_used_by.setCurrentText(used_by)
            self.txt_remark.setText(remark)

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a device to view information.",
                                    QMessageBox.StandardButton.Ok)




    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_device_id.clear()
        self.lbl_id_popup.clear()

    

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()
            

        

    def getdeviceStatus(self):
        
        #device
            result_device = self.devicemanagercontroller.getDevice()
            print('Retrieved data:', result_device)

            self.cmb_device_name.clear()
            self.cmb_device_name.addItem('No select')
            self.deviceData = [] 

            for item in result_device:
                device_name = item.get('device_name', '')
                device_id = item.get('device_id', '')
                used_by_id = item.get('used_by', '')
                status_id = item.get('status_id')
                device_location_id = item.get('device_location_id')

                if device_name:
                    self.cmb_device_name.addItem(device_name)
                    self.deviceData.append({'device_id': device_id, 'device_name': device_name,'used_by':used_by_id,'status_id':status_id,'device_location_id':device_location_id})  

        # location 
            result_location= self.devicemanagercontroller.getDeviceLocation()
            
            self.cmb_device_location.clear()
            self.cmb_device_location.addItem('No select')
            self.deviceLocationData = [] 

            for item in result_location:
                location = item.get('device_location_name', '')
                device_location_id = item.get('device_location_id', '')

                if location:
                    
                    self.cmb_device_location.addItem(location)
                    self.deviceLocationData.append({'device_location_id': device_location_id, 'device_location_name': location})

    

    def UpdateUsedBy(self):
        try:
        # used by
            result_used_by= self.devicemanagercontroller.getUseBy()
            
            self.cmb_used_by.clear()
            self.cmb_used_by.addItem('No select')
            self.usedByData = [] 

            for item in result_used_by:
                used_by = item.get('by_user', '')
                used_by_id = item.get('emp_id', '')

                if used_by:
                    
                    self.cmb_used_by.addItem(used_by)
                    self.usedByData.append({'emp_id': used_by_id, 'by_user': used_by})  
        except Exception as e:
            print('Exception occurred:', e)


    def UpdateStatus(self):
        try:
        # used by
            result_status= self.devicemanagercontroller.getStatus()
            
            self.cmb_status.clear()
            self.cmb_status.addItem('No select')
            self.statusData = [] 

            for item in result_status:
                status_name = item.get('status_name', '')
                status_id = item.get('status_id', '')

                if status_name:
                    
                    self.cmb_status.addItem(status_name)
                    self.statusData.append({'status_id': status_id, 'status_name': status_name})  
        except Exception as e:
            print('Exception occurred:', e)


    def getSameData(self):
        try:
          
            result_check = self.devicemanagercontroller.selectDeviceData()
            self.checkSameData = [] 
            

            for item in result_check:
                name = item.get('device_name', '')
                if name :
                    self.checkSameData.append({'device_name': name})

        except Exception as e:
            print('Exception occurred:', e)

    def add_info(self):
        try:
            device_info = self.getDeviceInfo()

            if device_info is None:
                raise ValueError("No device info returned")

            if not device_info.get("device_id") or device_info["device_id"] == "No Select":
                QMessageBox.warning(self, "Validation Error", "Device name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return

            if not device_info.get("status_id") or device_info["status_id"] == "No Select":
                QMessageBox.warning(self, "Validation Error", "Status name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return

            if not device_info.get("device_location_id") or device_info["device_location_id"] == "No Select":
                QMessageBox.warning(self, "Validation Error", "Device Location must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return

            if not device_info.get("used_by_id") or device_info["used_by_id"] == "No Select":
                QMessageBox.warning(self, "Validation Error", "Use by must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                # Check for duplicate device
                duplicate_found = False
                for device in self.checkSameData:
                    if device['device_name'] == device_info["device_name"]:
                        QMessageBox.warning(self, "Validation Error", "Device is in progress",
                                            QMessageBox.StandardButton.Ok)
                        self.openInsertPopUpFormDevice()
                        duplicate_found = True
                        break  # Exit the loop if a duplicate is found

                # If no duplicate is found, proceed to add the device info
                if not duplicate_found:
                    # Encode text data if necessary
                    device_name = device_info["device_name"].encode('utf-8').decode('utf-8')
                    serial_number = device_info["serial_number"].encode('utf-8').decode('utf-8')

                    self.devicemanagercontroller.add_info(
                        device_id=device_info["device_id"],
                        used_by_id=device_info["used_by_id"],
                        status_id=device_info["status_id"],
                        device_location_id=device_info["device_location_id"]
                    )

                    self.devicehistorycontroller.addDeviceManage(
                        device_name=device_name,
                        serial_number=serial_number,
                        used_by=device_info["used_by"],
                        status_id=device_info["status_id"],
                        device_location_id=device_info["device_location_id"],
                        created_by=device_info["created_by"]
                    )

                    self.devicecontroller.updateUseby(
                        device_id=device_info["device_id"],
                        used_by_id=device_info["used_by_id"]
                    )

                    print('Info added successfully.')
                    self.loadAndShowData()
                    self.closePopUp()
                    QMessageBox.information(self, "Success", "Info added successfully.",
                                            QMessageBox.StandardButton.Ok)

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')



    def updateData(self):
        try:
            device_info = self.getDeviceInfo()
            if device_info is None:
                raise ValueError("No device info returned")

        
            
            

        
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
            # Perform the update operation
                update_result = self.devicemanagercontroller.updateData(
                    status_id=device_info["status_id"],
                    device_manager_id=device_info["device_manager_id"],
                    device_location_id=device_info["device_location_id"],
                    used_by_id=device_info["used_by_id"],
                    
                )
                
                self.devicehistorycontroller.addDeviceManage(
                        device_name=device_info["device_name"],
                        serial_number=device_info["serial_number"],
                        used_by = device_info["used_by"],
                        status_id=device_info["status_id"],
                        device_location_id=device_info["device_location_id"],
                        created_by = device_info["created_by"])
                 
                self.devicecontroller.updateUseby(
                        device_id=device_info["device_id"],
                        used_by_id=device_info["used_by_id"]
                        )

                if update_result:
                    
                    QMessageBox.information(self, "Warning",
                                            f"Fail to update the information: {update_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "Device information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in device information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            device_info = self.getDeviceInfo()

            if not device_info["device_id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.devicemanagercontroller.deleteData(device_manager_id=device_info["device_manager_id"])

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
            
    def getDeviceInfo(self):
        # Assume you have a way to get the current username
        
        device_manager_id = self.lbl_device_id.text().strip()
        device_name = self.cmb_device_name.currentText().strip()
        serial_number = self.lbl_serial_number.text().strip()
        status_name = self.cmb_status.currentText().strip()
        device_location = self.cmb_device_location.currentText().strip()
        used_by = self.cmb_used_by.currentText().strip()
        remark = self.txt_remark.text().strip()
        created_by = self.lbl_username.text().strip()

        

        device_id = None
        status_id = None
        device_location_id = None
        used_by_id = None
        device_model_id = None

        for device in self.deviceData:
            if device['device_name'] == device_name:
                device_id = device['device_id']
                break


        for location in self.deviceLocationData:
            if location['device_location_name'] == device_location:
                device_location_id = location['device_location_id']
                break

        for usedby in self.usedByData:
            if usedby['by_user'] == used_by:
                used_by_id = usedby['emp_id']
                break

        for status in self.statusData:
            if status['status_name'] == status_name:
                status_id = status['status_id']
                break

        device_info = {
            "device_name": device_name,
            "serial_number": serial_number,
            "device_id": device_id,
            "device_manager_id": device_manager_id,
            "status_id": status_id,
            "device_model_id": device_model_id,
            "device_location_id": device_location_id,
            "used_by_id": used_by_id,
            "used_by": used_by,
            "remark": remark,
            "created_by": created_by
        }

        print('Device Data:', device_info)  # Debug line
        return device_info
    
    def getDeviceID(self):
        try:
            current_index = self.cmb_device_name.currentIndex()
            if self.cmb_device_name.currentText() != 'No select' and current_index >= 0:
                used_by_id = self.deviceData[current_index - 1]['used_by']
                device_id = self.deviceData[current_index - 1]['device_id']
                status_id = self.deviceData[current_index - 1]['status_id']
                device_location_id = self.deviceData[current_index - 1]['device_location_id']
                
                print("used_by", used_by_id)
                print("status_id", status_id)
                   
                # Call getDepartment with the company_id argument
                result_device = self.devicemanagercontroller.SetFormByDeviceId(used_by_id=str(used_by_id))
                result_serial_number = self.devicemanagercontroller.SetLabelSerialNumber(device_id = str(device_id))
                result_status = self.devicemanagercontroller.SetStatus(status_id = str(status_id))
                result_device_location = self.devicemanagercontroller.SetDeviceLocation(device_location_id = str(device_location_id))
                # Department
                # self.cmb_used_by.blockSignals(True) 
                self.cmb_used_by.clear()
                self.cmb_used_by.addItem('No select')
                self.usedByData = []
                self.statusData = []
                self.UpdateUsedBy()
                self.UpdateStatus()

                # Used by
                for item in result_device:
                    used_by_name = item.get('used_by_name', '')
                    used_by_id = item.get('emp_id', '')

                    if used_by_name:
                        self.cmb_used_by.addItem(used_by_name)
                        self.usedByData.append({'used_by_id': used_by_id, 'used_by_name': used_by_name})

                self.cmb_used_by.setCurrentText(used_by_name)
                

                for item in result_serial_number:
                    serial_number = item.get('serial_number', '')
                    if serial_number:
                        self.lbl_serial_number.setText(' ' +serial_number)
                    
                for item in result_status:
                    status_name = item.get('status_name', '')
                    status_id = item.get('status_id', '')

                    if status_name:
                        self.cmb_status.addItem(status_name)
                        self.statusData.append({'status_id': status_id, 'status_name': status_name})

                self.cmb_status.setCurrentText(status_name)


                for item in result_device_location:
                    device_location_name = item.get('device_location_name', '')
                    device_location_id = item.get('device_location_id', '')

                    if device_location_name:
                        self.cmb_status.addItem(device_location_name)
                        self.deviceLocationData.append({'device_location_id': device_location_id, 'device_location_name': device_location_name})

                self.cmb_device_location.setCurrentText(device_location_name)
                
                
            else:
                print("Error: No Deivice selected")
                self.cmb_used_by.clear()
                self.cmb_used_by.addItem('No select')
                self.UpdateStatus()
                self.UpdateUsedBy()
        except Exception as e:
            print(f"Error: {e}")





