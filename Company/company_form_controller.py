import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Company.company_form_controller_ui import Ui_frm_company
from Company.company_controller import companyController
from Company.company_form_popup import companyFormPopUp


class FrmCompanyController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_company()
        self.companyformpopup = companyFormPopUp()
        self.ui.setupUi(self)
        self.companycontroller = companyController()
        
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
      
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.companyformpopup.ui.btn_insert
        self.btn_edit_popup = self.companyformpopup.ui.btn_edit
        self.btn_cancel_popup = self.companyformpopup.ui.btn_cancel
        self.btn_clear_popup = self.companyformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_company_id = self.ui.lbl_did
        self.lbl_id_popup = self.companyformpopup.ui.lbl_did_
        self.txt_company_name = self.companyformpopup.ui.txt_company_name
        self.txt_remark = self.companyformpopup.ui.txt_remark
        self.txt_search = self.companyformpopup.ui.txt_search
       
    def initSignal(self):
        self.btn_insert.clicked.connect(self.openInsertPopUpFormcompany)
        self.btn_insert.clicked.connect(self.clearPopUp)
        self.btn_edit.clicked.connect(self.openEditPopUpFormcompany)
        self.btn_edit.clicked.connect(self.txt_company_name.setFocus)
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
        self.txt_company_name.clear()
        self.txt_company_name.setFocus()

    def closePopUp(self):
        self.companyformpopup.close()
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
            result = self.companycontroller.selectCompanyData()  # Ensure this method exists and fetches data
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
                    info.get("company_id", ""),
                    info.get("company_name", ""),
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
        self.lbl_company_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def openInsertPopUpFormcompany(self):
        self.companyformpopup.show()
        self.companyformpopup.activateWindow()
        self.txt_company_name.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)

    def openEditPopUpFormcompany(self):
        self.companyformpopup.show()
        self.companyformpopup.activateWindow()
        self.btn_edit_popup.setHidden(False)
        self.btn_insert_popup.setHidden(True)
        self.txt_company_name.setFocus()

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
            company_id = self.tbshow.item(select_row, 0).text().strip()
            company_name = self.tbshow.item(select_row, 1).text().strip()
            description = self.tbshow.item(select_row, 2).text().strip()
        

            # Update the labels and combo boxes with the selected row data
            self.lbl_company_id.setText(company_id)
            self.lbl_id_popup.setText(company_id)
            self.txt_company_name.setText(company_name)
            self.txt_remark.setText(description)

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a company to view information.",
                                    QMessageBox.StandardButton.Ok)


    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_company_id.clear()
        self.lbl_id_popup.clear()

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()


    def add_info(self):
        try:
            company_info = self.getCompanyInfo()
            if company_info is None:
                raise ValueError("No company info returned")

            
            if not company_info["company_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Company name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormcompany()
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:   
                add_result = self.companycontroller.add_info(                    
                    company_name=company_info["company_name"], 
                    description =company_info["description"]
                    )
                if add_result:
                    QMessageBox.critical(self, "Warning",
                                        f"Fail to update the information: {add_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "company information add successfully.",
                                        QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()
            else:
                self.openInsertPopUpFormcompany()
    
                   

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')






    def updateData(self):
        try:
            company_info = self.getCompanyInfo()
            
            # Ensure the company_id is available before proceeding with the update
            if company_info is None:
                raise ValueError("No company info returned")

            
            if not company_info["company_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Company name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormcompany()
                return

            # Ensure the company_id is available before proceeding with the update
            if not company_info["company_id"]:
                QMessageBox.warning(self, "Warning", "Please select a company to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
            
                # Perform the update operation
                update_result = self.companycontroller.updateData(
                    company_id=company_info["company_id"],
                    company_name=company_info["company_name"],
                    description=company_info["description"]
                )

                if update_result:
                    
                    QMessageBox.information(self, "Warning",
                                            f"Fail to update the information: {update_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "company information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()

            else: 
                self.openEditPopUpFormcompany()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in company information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            company_info = self.getCompanyInfo()

            if not company_info["company_id"]:
                QMessageBox.warning(self, "Warning", "Please select a company to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.companycontroller.deleteData(company_id=company_info["company_id"])

                if delete_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to delete the information: {delete_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "company information deleted successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in company information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in delete_info: {e}",
                                QMessageBox.StandardButton.Ok)

    def getCompanyInfo(self):
        company_id = self.lbl_company_id.text().strip()
        company_name = self.txt_company_name.text().strip()
        description = self.txt_remark.text().strip()


        company_info = {
            "company_id": company_id,   
            "company_name": company_name,
            "description": description
  
        }

        print('company Data:', company_info)  # Debug line
        return company_info



    
    