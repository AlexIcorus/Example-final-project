import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Device_info.device_form_controller_ui import Ui_frm_Device
from Device_info.device_controller import DeviceController
from Device_info.device_form_popup import DeviceFormPopUp
from History.device_history_controller import DeviceHistoryController
from Device_manager.device_form_manager_controller import DeviceManageController


class FrmDeviceController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_Device()
        self.deviceformpopup = DeviceFormPopUp()
        self.ui.setupUi(self)
        self.devicecontroller = DeviceController()
        self.devicehistorycontroller = DeviceHistoryController()
        self.devicemanagercontroller = DeviceManageController()
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
        self.getBrandStatus()
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.deviceformpopup.ui.btn_insert
        self.btn_edit_popup = self.deviceformpopup.ui.btn_edit
        self.btn_cancel_popup = self.deviceformpopup.ui.btn_cancel
        self.btn_clear_popup = self.deviceformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_device_id = self.ui.lbl_did
        self.txt_serial_number = self.deviceformpopup.ui.txt_serial_number
        self.txt_mac_address = self.deviceformpopup.ui.txt_mac_address
        self.lbl_id_popup = self.deviceformpopup.ui.lbl_did_
        self.txt_remark = self.deviceformpopup.ui.txt_remark
        self.cmb_brand = self.deviceformpopup.ui.cmb_brand_name
        self.cmb_status = self.deviceformpopup.ui.cmb_status
        self.txt_username = self.deviceformpopup.ui.txt_username
        self.txt_device_name = self.deviceformpopup.ui.txt_device_name
        self.cmb_device_location = self.deviceformpopup.ui.cmb_location
        self.lbl_manage_id = self.ui.lbl_devicemange_id
    
        self.cmb_device_model = self.deviceformpopup.ui.cmb_Model

        self.cmb_used_by = self.deviceformpopup.ui.cmb_used_by
        self.cmb_category = self.deviceformpopup.ui.cmb_category
        self.txt_search = self.deviceformpopup.ui.txt_search
        self.lbl_title = self.ui.lbl_title  
        self.lbl_user = self.ui.lbl_user
        self.btn_search = self.ui.btn_search
        self.txt_search_main = self.ui.txt_search
        self.lbl_21 = self.deviceformpopup.ui.label_21
        self.vld_brand_name = self.deviceformpopup.ui.vld_brand_name
        self.vld_device_model = self.deviceformpopup.ui.vld_device_model
        self.vld_device_name = self.deviceformpopup.ui.vld_device_name
        self.vld_serial_number = self.deviceformpopup.ui.vld_serial_number
        self.vld_serial_number_same = self.deviceformpopup.ui.vld_serial_number_same
        self.vld_mac_address = self.deviceformpopup.ui.vld_mac_address
        self.vld_mac_address_same = self.deviceformpopup.ui.vld_mac_address_same
        self.vld_category = self.deviceformpopup.ui.vld_category
      




  
       
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
        self.btn_search.clicked.connect(self.searchData)
        self.txt_search_main.returnPressed.connect(self.searchData)
     
        self.hideEditButton()

    def clearPopUp(self):
        self.getBrandStatus()
        self.txt_search.clear()
        self.txt_remark.clear()
        self.txt_device_name.clear()
        self.cmb_device_model.setFocus()
        self.txt_serial_number.clear()
        self.txt_mac_address.clear()

    def closePopUp(self):
        self.deviceformpopup.close()
        print("hii")
        return
        self.clearPopUp()


    def setupTable(self):
        self.tbshow.setColumnCount(13)
        self.tbshow.setColumnHidden(0, True)
        # self.cmb_used_by.setHidden(True)
        # self.lbl_21.setHidden(True)
       
        self.tbshow.setColumnHidden(11, True)
        
     
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
     
        column_widths = [50, 200, 200, 200, 100, 150, 70, 80, 100, 100, 100,100]
      
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        for i in range(13):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)

        self.tbshow.setColumnWidth(1, 150)
        self.tbshow.setColumnWidth(2, 200)
        self.tbshow.setColumnWidth(3, 200)
        self.tbshow.setColumnWidth(4, 150)
        self.tbshow.setColumnWidth(5, 150)
        self.tbshow.setColumnWidth(6, 150)
        self.tbshow.setColumnWidth(7, 200)
        self.tbshow.setColumnWidth(8, 200)
        self.tbshow.setColumnWidth(9, 200)
        self.tbshow.setColumnWidth(10, 200)
        self.tbshow.setColumnWidth(11, 200)
        self.tbshow.setColumnWidth(12, 200)
  

        
    def setUsername(self,user):
        self.txt_username.clear()
        self.txt_username.setText(user[0]['username'])
        self.lbl_user.setText('User: ( '+ user[0]['name']+' )')
        self.txt_username.setHidden(True)

    def loadAndShowData(self):

        try:
            result = self.devicecontroller.selectDeviceData()  # Ensure this method exists and fetches data
            self.showData(result)
           
            print(result)
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to load data: {e}")
    
    def showData(self, result):
        font = QFont()
        font.setPointSize(10)  # Set font size to 10px
        
        if result:
            self.tbshow.setRowCount(len(result))
            for row, info in enumerate(result):
                # Check if `used_by` is `NULL` or an empty string
                used_id = info.get("user_id", "0")
                used_by = info.get("used_by", "")
                if used_id != '0' :
                    used_by_display = "No User Use" 
                else:
                    used_by_display = used_by
                info_list = [
                    info.get("device_id", ""),
                    info.get("brand_name", ""),
                    info.get("device_name", ""),
                    info.get("device_model", ""),
                    info.get("serial_number", ""),
                    info.get("mac_address", ""),
                    info.get("status_name", ""), 
                    info.get("category_name", ""),   
                    info.get("device_remark", ""),
                    info.get("device_location_name", ""),                     
                    info.get("username", ""),   
                    info.get("created_by", ""),  
                    used_by_display,  # Display "No" if `used_by` is `NULL` or "null", otherwise the actual value
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    cell_item.setFont(font)
                    self.tbshow.setItem(row, column, cell_item)
        else:
            self.tbshow.setRowCount(0)



    def setAfterLogin(self,user):
        self.setUser()
        print('This is AlexTheDark World')
        
    
    def setUser(self):
        self.txt_username.setText('AlexTheDark')
        print('Aloha')
        
    
   

    def hideEditButton(self):
        self.btn_edit.setHidden(True)
        self.btn_delete.setHidden(True)
        self.lbl_device_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)
        self.vld_brand_name.setHidden(True)
        self.vld_device_model.setHidden(True)
        self.vld_mac_address.setHidden(True)
        self.vld_mac_address_same.setHidden(True)
        self.vld_serial_number.setHidden(True)
        self.vld_serial_number_same.setHidden(True)
        self.vld_category.setHidden(True)
        self.vld_device_name.setHidden(True)

    
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
        self.cmb_device_model.setFocus()

    def selectRecord(self):
        try:
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
                device_id = self.tbshow.item(select_row, 0).text().strip()
                brand_name = self.tbshow.item(select_row, 1).text().strip()
                device_name = self.tbshow.item(select_row, 2).text().strip()
                device_model = self.tbshow.item(select_row, 3).text().strip()
                serial_number = self.tbshow.item(select_row, 4).text().strip()
                mac_address = self.tbshow.item(select_row, 5).text().strip()
                status_name = self.tbshow.item(select_row, 6).text().strip()
                category_name = self.tbshow.item(select_row, 8).text().strip()
                remark = self.tbshow.item(select_row, 9).text().strip()
                device_location = self.tbshow.item(select_row, 10).text().strip()
                username = self.tbshow.item(select_row, 11).text().strip()
                used_by = self.tbshow.item(select_row, 12).text().strip()

                # Update the labels and combo boxes with the selected row data
                self.lbl_device_id.setText(device_id)
                self.lbl_id_popup.setText(device_id)

                # Set the combo boxes based on the selected row data using setCurrentText
                self.cmb_brand.setCurrentText(brand_name)
                self.cmb_device_model.setCurrentText(device_model)
                self.txt_serial_number.setText(serial_number)
                self.txt_mac_address.setText(mac_address)
                self.cmb_status.setCurrentText(status_name)
                self.cmb_category.setCurrentText(category_name)
                self.cmb_device_location.setCurrentText(device_location)
                self.txt_device_name.setText(device_name)
                
                self.cmb_used_by.setCurrentText(used_by)
                self.txt_remark.setText(remark)

                self.showEditButton()

            else:
                self.clearSelectionSettings()
                QMessageBox.information(self, "Warning", "Please select a device to view information.",
                                        QMessageBox.StandardButton.Ok)

    
        except KeyError as e:
            print(f'KeyError in select: {e}')
        except ValueError as e:
            print(f'ValueError in select: {e}')
        except Exception as e:
            print(f'Error in select: {e}')



    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_device_id.clear()
        self.lbl_id_popup.clear()

    

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()
            

        

    def getBrandStatus(self):
        try:
        #Brand
            result_brand = self.devicecontroller.getBrand()
            # print('Retrieved data:', result_brand)

            self.cmb_brand.clear()
            self.cmb_brand.addItem('No select')
            self.brandData = [] 

            for item in result_brand:
                brand_name = item.get('brand_name', '')
                brand_id = item.get('brand_id', '')

                if brand_name:
                    self.cmb_brand.addItem(brand_name)
                    self.brandData.append({'brand_id': brand_id, 'brand_name': brand_name})  

        #Device Model
            result_device_model= self.devicecontroller.getDeviceModel()
            self.cmb_device_model.clear()
            deviceData = [""]
            for item in result_device_model:
                for k, v in item.items():
                    if v != "":
                        deviceData.append(' '+v)

            if len(deviceData) > 1:
                self.cmb_device_model.addItems(deviceData)

        #Status
            result_status = self.devicecontroller.getStatus()
            # print('Retrieved data:', result_status)

            self.cmb_status.clear()
            self.cmb_status.addItem('No select')
            self.statusData = [] 

            for item in result_status:
                status_name = item.get('status_name', '')
                status_id = item.get('status_id', '')

                if status_name:
                    # self.cmb_status.addItem(status_name)
                    self.cmb_status.addItem(status_name)
                    self.statusData.append({'status_id': status_id, 'status_name': status_name}) 

        
        #User
            result_user = self.devicecontroller.getUser()
            # print('Retrieved data:', result_status)

            self.userData = [] 

            for item in result_user:
                username = item.get('username', '')
                user_id = item.get('id', '')

                if username:
                    self.userData.append({'id': user_id, 'username': username}) 
        
        
        # category
            result_category= self.devicecontroller.getCategory()

            self.cmb_category.clear()
            self.cmb_category.addItem('No select')
            self.categoryData = [] 
           

            for item in result_category:
                category_name = item.get('category_name', '')
                category_id = item.get('category_id', '')

                if category_name:
                   
                    self.cmb_category.addItem(category_name)
                    self.categoryData.append({'category_id': category_id, 'category_name': category_name})  
            # category_id = self.categoryData[0]["category_id"]
            # self.cmb_category.addItem(str(category_id))
        

        # location 
            result_location= self.devicecontroller.getDeviceLocation()
            
            self.cmb_device_location.clear()
            self.cmb_device_location.addItem('No select')
            self.deviceLocationData = [] 

            for item in result_location:
                location = item.get('device_location_name', '')
                device_location_id = item.get('device_location_id', '')

                if location:
                    
                    self.cmb_device_location.addItem(location)
                    self.deviceLocationData.append({'device_location_id': device_location_id, 'device_location_name': location})  

        # used by
            result_used_by= self.devicecontroller.getUseBy()
            
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

    def add_info(self):
        try:
            device_info = self.getDeviceInfo()

            if device_info is None:
                raise ValueError("No device info returned")


            
            if not device_info["brand_id"] and "No Select":
                QMessageBox.warning(self, "Validation Error", "Brand name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                self.cmb_device_model.setFocus()
                return
            
            if not device_info["status_id"]and "No Select":
                QMessageBox.warning(self, "Validation Error", "Status name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                self.cmb_device_model.setFocus()
                return
            

            if not device_info["device_location_id"]and "No Select":
                QMessageBox.warning(self, "Validation Error", "Device Location must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                self.cmb_device_model.setFocus()
                return
            
            if not device_info["category_id"]and "No Select":
                QMessageBox.warning(self, "Validation Error", "Category name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormDevice()
                self.cmb_device_model.setFocus()    
                return

      
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
                # Check if all IDs are valid
                  
                
                    self.devicecontroller.add_info(
                        brand_id=device_info["brand_id"],
                        device_name = device_info["device_name"],
                        status_id=device_info["status_id"],
                        device_model=device_info["device_model"],
                        mac_address=device_info["mac_address"],
                        serial_number=device_info["serial_number"],
                        user_id=device_info["user_id"],
                        category_id=device_info["category_id"],
                        device_location_id=device_info["device_location_id"],
                        created_by = device_info["created_by"],
                        used_by_id = device_info["used_by_id"],
                        remark =device_info["remark"]

                    )
                    

                    self.devicehistorycontroller.addDeviceInfo(
                       
                        device_name = device_info["device_name"],
                        status_id=device_info["status_id"],
                        serial_number=device_info["serial_number"],
                        device_location_id=device_info["device_location_id"],
                        created_by = device_info["created_by"],
          

                    )
                    # print('Info added successfully.')
                    self.loadAndShowData()
                    self.closePopUp()
                    QMessageBox.information(self,"Success", "Info added successfully.",
                                            QMessageBox.StandardButton.Ok)
        

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')

    def searchData(self):
        try:
            font = QFont()
            font.setPointSize(10)
            device_info = self.getDeviceInfo()
            result = self.devicecontroller.searchData(select_data=device_info["search_data"])
            if device_info["search_data"]=="":
                self.loadAndShowData()
            else:
                if result:
                    self.tbshow.setRowCount(len(result))
                    for row, info in enumerate(result):
                        info_list = [
                            info.get("device_id",""),
                            info.get("brand_name", ""),
                            info.get("device_name", ""),
                            info.get("device_model", ""),
                            info.get("serial_number", ""),
                            info.get("mac_address", ""),
                            info.get("status_name", ""),
                        
                            info.get("category_name", ""),
                            info.get("device_remark", ""),
                            info.get("device_location_name", ""),
                            info.get("created_by", ""),
                            info.get("created_by", ""),
                            info.get("used_by", "")
                        ]

                        for column, item in enumerate(info_list):
                            cell_item = QTableWidgetItem(str(item))
                            cell_item.setFont(font)
                            self.tbshow.setItem(row, column, cell_item)

                else:
                    self.tbshow.setRowCount(0)
                    QMessageBox.information(self, "No Data Found", "No data found in Database")
                    
                    self.loadAndShowData()


        except Exception as e:
            print(e)
                                                                   
              
                     
     

    def updateData(self):
        try:
            device_info = self.getDeviceInfo()
            if device_info is None:
                raise ValueError("No device info returned")

            
            if not device_info["brand_id"] and "No Select":
                QMessageBox.warning(self, "Validation Error", "Brand name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                self.cmb_device_model.setFocus()
                return
            
            if not device_info["status_id"]and "No Select":
                QMessageBox.warning(self, "Validation Error", "Status name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                self.cmb_device_model.setFocus()
                return
            
            
            if not device_info["device_location_id"]and "No Select":
                QMessageBox.warning(self, "Validation Error", "Device Location must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                self.cmb_device_model.setFocus()
                return
            

            
            if not device_info["category_id"]and "No Select":
                QMessageBox.warning(self, "Validation Error", "Category name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                self.cmb_device_model.setFocus()    
                return
            
            

            # Ensure the brand_id is available before proceeding with the update
            if not device_info["device_id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
            # Perform the update operation
                update_result = self.devicecontroller.updateData(
                    device_id=device_info["device_id"],
                    brand_id=device_info["brand_id"],
                    device_name=device_info["device_name"],
                    status_id=device_info["status_id"],
                    device_model=device_info["device_model"],
                    serial_number=device_info["serial_number"],
                    mac_address=device_info["mac_address"],
                 
                    user_id=device_info["user_id"],
                    category_id=device_info["category_id"],
                    device_location_id=device_info["device_location_id"],
                    used_by_id=device_info["used_by_id"],
                    remark=device_info["remark"]
                )
                self.devicemanagercontroller.updateFromDeviceInfo(
                    status_id=device_info["status_id"],
                    device_id=device_info["device_id"],
                    device_location_id=device_info["device_location_id"],
                    used_by_id=device_info["used_by_id"],
                    
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
                delete_result = self.devicecontroller.deleteData(device_id=device_info["device_id"])

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
        
        username = self.txt_username.text().strip()
        device_id = self.lbl_device_id.text().strip()
        brand_name = self.cmb_brand.currentText().strip()
        device_model = self.cmb_device_model.currentText().strip()
        serial_number = self.txt_serial_number.text().strip()
        mac_address = self.txt_mac_address.text().strip()
        status_name = self.cmb_status.currentText().strip()

        category_name = self.cmb_category.currentText().strip()
        device_location = self.cmb_device_location.currentText().strip()
        used_by = self.cmb_used_by.currentText().strip()
        remark = self.txt_remark.text().strip()
        search_data = self.txt_search_main.text().strip()
        device_name = self.txt_device_name.text().strip()
        created_by = self.lbl_user.text().strip()

        brand_id = None
        status_id = None
       
        category_id = None
        user_id = None
        device_location_id = None
        used_by_id = None

        for brand in self.brandData:
            if brand['brand_name'] == brand_name:
                brand_id = brand['brand_id']
                break

        for user in self.userData:
            if user['username'] == username:
                user_id = user['id']
                break

        for status in self.statusData:
            if status['status_name'] == status_name:
                status_id = status['status_id']
                break 

        for category in self.categoryData:
            if category['category_name'] == category_name:
                category_id = category['category_id']
                break 

        for location in self.deviceLocationData:
            if location['device_location_name'] == device_location:
                device_location_id = location['device_location_id']
                break

        for usedby in self.usedByData:
            if usedby['by_user'] == used_by:
                used_by_id = usedby['emp_id']
                break

        device_info = {
            "brand_id": brand_id,
            "device_name": device_name,
            "status_id": status_id,
            "device_id": device_id,
            "device_model": device_model,
            "serial_number": serial_number,
            "mac_address": mac_address,
      
            "user_id": user_id,
            "category_id": category_id,
            "device_location_id": device_location_id,
            "used_by_id": used_by_id,
            "remark": remark,
            "search_data": search_data,
            "created_by": created_by
        }

        # print('Device Data:', device_info)  # Debug line
        return device_info