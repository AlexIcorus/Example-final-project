import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from History.device_history_form_controller_ui import Ui_frm_Device_history
from History.device_history_controller import DeviceHistoryController



class FrmDeviceHistoryController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_Device_history()
        self.ui.setupUi(self)
        self.devicecontroller = DeviceHistoryController()
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
      
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_id = self.ui.lbl_did
        self.lbl_title = self.ui.lbl_title  
        self.lbl_user = self.ui.lbl_user
        self.btn_search = self.ui.btn_search
        self.txt_search_main = self.ui.txt_search
       
  
       
    def initSignal(self):
        self.btn_refresh.clicked.connect(self.loadAndShowData)
        self.tbshow.itemSelectionChanged.connect(self.selectRecord)
        self.tbshow.itemSelectionChanged.connect(self.checkSelection)
        self.btn_delete.clicked.connect(self.delete_info)
        self.btn_search.clicked.connect(self.searchData)
        self.txt_search_main.returnPressed.connect(self.searchData)
     
        self.hideEditButton()


    def setupTable(self):
        self.tbshow.setColumnCount(10)
        self.tbshow.setColumnHidden(0, True)
       
        self.tbshow.setColumnHidden(9, True)
        
     
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
     
        column_widths = [50, 200, 200, 200, 100, 150, 70, 80, 100, 100]
      
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        for i in range(11):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)

        self.tbshow.setColumnWidth(1, 150)
        self.tbshow.setColumnWidth(2, 200)
        self.tbshow.setColumnWidth(3, 150)
        self.tbshow.setColumnWidth(4, 150)
        self.tbshow.setColumnWidth(5, 150)
        self.tbshow.setColumnWidth(6, 200)
        self.tbshow.setColumnWidth(7, 200)
        self.tbshow.setColumnWidth(8, 200)
        self.tbshow.setColumnWidth(9, 250)
      

        
    def setUsername(self,user):
        self.lbl_user.setText('User: ( '+ user[0]['name']+' )')

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
        font.setPointSize(10)  # Set font size to 8px
        if result:
            self.tbshow.setRowCount(len(result))
            for row, info in enumerate(result):
                info_list = [
                    info.get("id", ""),
                    info.get("device_name", ""),
                    info.get("serial_number", ""),
                    info.get("status_name", ""), 
                    info.get("created_at", ""),
                    info.get("device_location_name", ""),      
                    info.get("device_created_date", ""),
                    info.get("created_by", ""),
                    info.get("used_by",""),         
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    cell_item.setFont(font)
                    self.tbshow.setItem(row, column, cell_item)
        else:
            self.tbshow.setRowCount(0)
   

    def hideEditButton(self):
  
        self.btn_delete.setHidden(True)
        self.lbl_id.setHidden(True)
  

    
    def showEditButton(self):

        self.btn_delete.setHidden(False)

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
            id = self.tbshow.item(select_row, 0).text().strip()

            # Update the labels and combo boxes with the selected row data
            self.lbl_id.setText(id)

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a device to view information.",
                                    QMessageBox.StandardButton.Ok)




    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_id.clear()


    

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()

    

    def searchData(self):
        try:
            font = QFont()
            font.setPointSize(10)
            History_info = self.getDeviceInfo()
            result = self.devicecontroller.searchData(select_data=History_info["search_data"])
            if History_info["search_data"]=="":
                self.loadAndShowData()
            else:
                if result:
                    self.tbshow.setRowCount(len(result))
                    for row, info in enumerate(result):
                        info_list = [
                            info.get("id",""),
                            info.get("device_name", ""),
                            info.get("serial_number", ""),                        
                            info.get("status_name", ""),
                            info.get("created_at", ""),
                            info.get("device_location_name", ""),
                            info.get("device_created_at", ""),
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
                                                                   


    def delete_info(self):
        try:
            History_info = self.getDeviceInfo()

            if not History_info["id"]:
                QMessageBox.warning(self, "Warning", "Please select a device to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.devicecontroller.deleteData(history_id=History_info["id"])

                if delete_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to delete the information: {delete_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "Device information deleted successfully.",
                                            QMessageBox.StandardButton.Ok)
              
                    self.loadAndShowData()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in device information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in delete_info: {e}",
                                QMessageBox.StandardButton.Ok)

    def getDeviceInfo(self):
        # Assume you have a way to get the current username
        
        search_data = self.txt_search_main.text().strip()
        history_id = self.lbl_id.text().strip()

        History_info = {
            "search_data": search_data,
            "id": history_id
        }

        print('Device Data:', History_info)  # Debug line
        return History_info




