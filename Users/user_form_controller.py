import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Users.user_form_controller_ui import Ui_frm_user
from Users.user_controller import userController
from Users.user_form_popup import userFormPopUp


class FrmuserController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_user()
        self.userformpopup = userFormPopUp()
        self.ui.setupUi(self)
        self.usercontroller = userController()
        
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
      
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.userformpopup.ui.btn_insert
        self.btn_edit_popup = self.userformpopup.ui.btn_edit
        self.btn_cancel_popup = self.userformpopup.ui.btn_cancel
        self.btn_clear_popup = self.userformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_user_id = self.ui.lbl_did
        self.lbl_id_popup = self.userformpopup.ui.lbl_did_
        self.txt_username = self.userformpopup.ui.txt_username
        self.txt_search = self.userformpopup.ui.txt_search
        self.txt_password = self.userformpopup.ui.txt_password
        self.txt_name = self.userformpopup.ui.txt_name
 
       
    def initSignal(self):
        self.btn_insert.clicked.connect(self.openInsertPopUpFormuser)
        self.btn_insert.clicked.connect(self.clearPopUp)
        self.btn_edit.clicked.connect(self.openEditPopUpFormuser)
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
        self.txt_name.clear()
        self.txt_username.clear()
        self.txt_password.clear()
        self.txt_username.setFocus()

    def closePopUp(self):
        self.userformpopup.close()
        self.txt_password.setEnabled(True)
        self.clearPopUp()


    def setupTable(self):
        self.tbshow.setColumnCount(4)
        self.tbshow.setColumnHidden(0, True)
        
     
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
     
        column_widths = [50, 200, 200, 200]
      
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        for i in range(4):
            header.setSectionResizeMode(i, QHeaderView.ResizeMode.Interactive)

        self.tbshow.setColumnWidth(0, 150)
        self.tbshow.setColumnWidth(1, 300)
        self.tbshow.setColumnWidth(2, 100)
        self.tbshow.setColumnWidth(3, 150)
      



       
    
    

    def loadAndShowData(self):

        try:
            result = self.usercontroller.selectuserData()  # Ensure this method exists and fetches data
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
                    info.get("id", ""),
                    info.get("username", ""),
                    info.get("name", ""),
                    info.get("password", "")
                   
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
        self.lbl_user_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def openInsertPopUpFormuser(self):
        self.userformpopup.show()
        self.userformpopup.activateWindow()
        self.txt_username.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)

    def openEditPopUpFormuser(self):
        self.userformpopup.activateWindow()
        self.userformpopup.show()
        self.txt_username.setFocus()
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
            user_id = self.tbshow.item(select_row, 0).text().strip()
            username = self.tbshow.item(select_row, 1).text().strip()
            name = self.tbshow.item(select_row, 2).text().strip()
            password = self.tbshow.item(select_row, 3).text().strip()
           
           
     

            # Update the labels and combo boxes with the selected row data
            self.lbl_user_id.setText(user_id)
            self.lbl_id_popup.setText(user_id)
            self.txt_username.setText(username)
            self.txt_name.setText(name)
            self.txt_password.setText(password)
          

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a user to view information.",
                                    QMessageBox.StandardButton.Ok)


    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_user_id.clear()
        self.lbl_id_popup.clear()

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()


    def add_info(self):
        try:
            user_info = self.getUserInfo()
            
            if user_info is None:
                raise ValueError("No user info returned")

        
            
            if not user_info["username"].strip():
                QMessageBox.warning(self, "Validation Error", "Username must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormuser()
                return
            
            if not user_info["name"].strip():
                QMessageBox.warning(self, "Validation Error", "Name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormuser()
                return
            if not user_info["password"].strip():
                QMessageBox.warning(self, "Validation Error", "Please Enter your password",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormuser()
                return

        
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
                self.usercontroller.add_info(
                   
                    username = user_info["username"], 
                    name =user_info["name"],
                    password= user_info["password"]
                    

                )
                print('Info added successfully.')
                self.loadAndShowData()
                self.closePopUp()
                QMessageBox.information(self,"Success", "Info added successfully.",
                                        QMessageBox.StandardButton.Ok)
            else:
                self.openInsertPopUpFormuser()              

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')






    def updateData(self):
        try:
            user_info = self.getUserInfo()
            self.txt_password.setEnabled(False)
            
            if user_info is None:
                raise ValueError("No user info returned")

            
            
            
            if not user_info["username"].strip():
                QMessageBox.warning(self, "Validation Error", "Address must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormuser()
                return
            if not user_info["name"].strip():
                QMessageBox.warning(self, "Validation Error", "Name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormuser()
                return

            # Ensure the brand_id is available before proceeding with the update
            if not user_info["user_id"]:
                QMessageBox.warning(self, "Warning", "Please select a Username to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to upadte it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
                
                # Perform the update operation
                update_result = self.usercontroller.updateData(
                    user_id=user_info["user_id"],
                    username=user_info["username"],
                    name=user_info["name"],
                    password=user_info["password"]
                    
                
                )

                if update_result:
                    
                    QMessageBox.information(self, "Warning",
                                            f"Fail to update the information: {update_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "user information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.loadAndShowData()
                    self.closePopUp()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in user information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            user_info = self.getUserInfo()

            if not user_info["user_id"]:
                QMessageBox.warning(self, "Warning", "Please select a user to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.usercontroller.deleteData(user_id=user_info["user_id"])

                if delete_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to delete the information: {delete_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "user information deleted successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in user information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in delete_info: {e}",
                                QMessageBox.StandardButton.Ok)

    def getUserInfo(self):
        user_id = self.lbl_user_id.text().strip()
        username = self.txt_username.text().strip()
        name = self.txt_name.text().strip()
        password = self.txt_password.text().strip()

        user_info = {
            "user_id": user_id,   
            "username": username,
            "name": name,   
            "password": password
        }

        print('user Data:', user_info)  # Debug line
        return user_info



    
    