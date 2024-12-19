import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Brand.brand_form_controller_ui import Ui_frm_brand
from Brand.brand_controller import BrandController
from Brand.brand_form_popup import BrandFormPopUp


class FrmBrandController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_brand()
        self.brandformpopup = BrandFormPopUp()
        self.ui.setupUi(self)
        self.devicecontroller = BrandController()
        
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
      
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.brandformpopup.ui.btn_insert
        self.btn_edit_popup = self.brandformpopup.ui.btn_edit
        self.btn_cancel_popup = self.brandformpopup.ui.btn_cancel
        self.btn_clear_popup = self.brandformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_brand_id = self.ui.lbl_did
        self.lbl_id_popup = self.brandformpopup.ui.lbl_did_
        self.txt_brand_name = self.brandformpopup.ui.txt_brand_name
        self.txt_remark = self.brandformpopup.ui.txt_remark
        self.txt_search = self.brandformpopup.ui.txt_search
       
    def initSignal(self):
        self.btn_insert.clicked.connect(self.openInsertPopUpFormDevice)
        self.btn_insert.clicked.connect(self.clearPopUp)
        self.txt_brand_name.returnPressed.connect(self.setFocusRemark)
        self.btn_edit.clicked.connect(self.openEditPopUpFormDevice)
        self.btn_edit.clicked.connect(self.txt_brand_name.setFocus)
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
        self.txt_brand_name.clear()
        self.txt_brand_name.setFocus()

    def closePopUp(self):
        self.brandformpopup.close()
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
            result = self.devicecontroller.selectBrandData()  # Ensure this method exists and fetches data
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
                    info.get("brand_id", ""),
                    info.get("brand_name", ""),
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
        self.lbl_brand_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def openInsertPopUpFormDevice(self):
        self.brandformpopup.show()
        self.brandformpopup.activateWindow()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)
        
    def setFocusRemark(self):
        self.txt_remark.setFocus()
    def openEditPopUpFormDevice(self):
       
        self.brandformpopup.activateWindow()
        self.brandformpopup.show()
        self.txt_brand_name.setFocus()
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
            brand_id = self.tbshow.item(select_row, 0).text().strip()
            brand_name = self.tbshow.item(select_row, 1).text().strip()
            description = self.tbshow.item(select_row, 2).text().strip()
        

            # Update the labels and combo boxes with the selected row data
            self.lbl_brand_id.setText(brand_id)
            self.lbl_id_popup.setText(brand_id)
            self.txt_brand_name.setText(brand_name)
            self.txt_remark.setText(description)

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a device to view information.",
                                    QMessageBox.StandardButton.Ok)


    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_brand_id.clear()
        self.lbl_id_popup.clear()

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()


    def add_info(self):
        try:
            device_info= self.getBrandInfo()
            if device_info is None:
                raise ValueError("No device info returned")

            
            # if not device_info["brand_name"].strip():
            #     QMessageBox.warning(self, "Validation Error", "Brand name must not be empty.",
            #                         QMessageBox.StandardButton.Ok)
            #     self.openInsertPopUpFormDevice()
            #     self.txt_brand_name.setFocus()
            #     return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                
                add_result = self.devicecontroller.add_info(
                        brand_name=device_info["brand_name"], 
                        description =device_info["description"]
                    )

                if add_result:
                    QMessageBox.critical(self, "Warning",
                                        f"Fail to update the information: {add_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "brand information add successfully.",
                                        QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()
            else:
                self.openInsertPopUpFormDevice()
                self.txt_brand_name.setFocus()
          

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')
        except UnicodeEncodeError as e:
            QMessageBox.critical(self, "Encoding Error", f"Failed to encode characters: {e}")
            return


    def updateData(self):
        try:
            device_info = self.getBrandInfo()
            brand_name = device_info["brand_name"].encode('utf-8', 'replace').decode('utf-8')
            description = device_info["description"].encode('utf-8', 'replace').decode('utf-8')
            if device_info is None:
                raise ValueError("No device info returned")

            
            if not device_info["brand_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Brand name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormDevice()
                self.txt_brand_name.setFocus()
                return

            # Ensure the brand_id is available before proceeding with the update
            if not device_info["brand_id"]:
                QMessageBox.warning(self, "Warning", "Please select a brand to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.information(self, "Warning", "Are you sure you want to Update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:

                update_result = self.devicecontroller.updateData(
                brand_id=device_info["brand_id"],
                brand_name=brand_name,
                description=description
            )
                if update_result:
                
                    QMessageBox.critical(self, "Warning",
                                        f"Fail to update the information: {update_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "brand information updated successfully.",
                                        QMessageBox.StandardButton.Ok)
                    self.closePopUp()
            else:
                self.openEditPopUpFormDevice()
                self.txt_brand_name.setFocus()


           

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in brand information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            device_info = self.getBrandInfo()

            if not device_info["brand_id"]:
                QMessageBox.warning(self, "Warning", "Please select a brand to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.devicecontroller.deleteData(brand_id=device_info["brand_id"])

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

    def getBrandInfo(self):
        brand_id = self.lbl_brand_id.text().strip()
        brand_name = self.txt_brand_name.text()
        description = self.txt_remark.text().strip()
        print('device_info',brand_name)

        device_info = {
            "brand_id": brand_id,   
            "brand_name": brand_name,
            "description": description
  
        }

        print('Brand Data Here :', device_info)  # Debug line
        return device_info



    
    