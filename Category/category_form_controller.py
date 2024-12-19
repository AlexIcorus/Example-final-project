import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView,QWidget
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont

from Category.category_form_controller_ui import Ui_frm_category
from Category.category_controller import CategoryController
from Category.category_form_popup import categoryFormPopUp


class FrmCategoryController(QWidget):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_frm_category()
        self.Categoryformpopup = categoryFormPopUp()
        self.ui.setupUi(self)
        self.categorycontroller = CategoryController()
        
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.clearSelectionSettings()
        # self.showSelectCategory()

      
   
        # self.updateFormComboBox()

       
        
        

    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_insert_popup = self.Categoryformpopup.ui.btn_insert
        self.btn_edit_popup = self.Categoryformpopup.ui.btn_edit
        self.btn_cancel_popup = self.Categoryformpopup.ui.btn_cancel
        self.btn_clear_popup = self.Categoryformpopup.ui.btn_clear
        self.btn_insert = self.ui.btn_Add
        self.btn_edit = self.ui.btn_Edit
        self.btn_delete = self.ui.btn_Delete
        self.btn_refresh = self.ui.btn_refresh
        self.lbl_category_id = self.ui.lbl_did
        self.lbl_id_popup = self.Categoryformpopup.ui.lbl_did_
        self.txt_category_name = self.Categoryformpopup.ui.txt_category_name
        self.txt_remark = self.Categoryformpopup.ui.txt_remark
        self.txt_search = self.Categoryformpopup.ui.txt_search
        self.lbl_category = self.ui.lbl_category_name_2
        self.lbl_total = self.ui.lbl_total
        self.lbl_available = self.ui.lbl_available
        self.lbl_in_use = self.ui.lbl_in_use
        self.lbl_repair = self.ui.lbl_repair
        self.lbl_broken = self.ui.lbl_broken
        
       
    def initSignal(self):
        self.btn_insert.clicked.connect(self.openInsertPopUpFormcategory)
        self.btn_insert.clicked.connect(self.clearPopUp)
        self.btn_edit.clicked.connect(self.openEditPopUpFormcategory)
        self.btn_edit.clicked.connect(self.txt_category_name.setFocus)
        self.btn_cancel_popup.clicked.connect(self.closePopUp)
        self.btn_clear_popup.clicked.connect(self.clearPopUp)
        self.btn_refresh.clicked.connect(self.loadAndShowData)
        self.btn_insert_popup.clicked.connect(self.add_info)
        self.btn_edit_popup.clicked.connect(self.updateData)
        self.btn_edit_popup.clicked.connect(self.loadAndShowData)
        self.tbshow.itemSelectionChanged.connect(self.selectRecord)
        self.tbshow.itemSelectionChanged.connect(self.checkSelection)
        self.tbshow.itemSelectionChanged.connect(self.afterSelectAvailable)
        self.btn_delete.clicked.connect(self.delete_info)
        self.txt_category_name.returnPressed.connect(self.setFocusRemark)
        self.hideEditButton()


    def clearPopUp(self):
        self.txt_search.clear()
        self.txt_category_name.setFocus()
        self.txt_remark.clear()
        self.txt_category_name.clear()

    def closePopUp(self):
        self.Categoryformpopup.close()
        self.clearPopUp()
        self.txt_category_name.setFocus()

    # def getCategory(self):
    # # category
    #     result_category= self.categorycontroller.getCategory()

    #     # self.lbl_total.setText('No select')
    #     self.categoryData = [] 

    #     for item in result_category:
    #         category_name = item.get('category_name', '')
    #         category_id = item.get('category_id', '')

    #         if category_name:
                    
    #             self.categoryData.append({'category_id': category_id, 'category_name': category_name})  

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
            result = self.categorycontroller.selectCategoryData()  # Ensure this method exists and fetches data
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
                    info.get("category_id", ""),
                    info.get("category_name", ""),
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
        self.lbl_category_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    def setFocusRemark(self):
        self.txt_remark.setFocus()

    def openInsertPopUpFormcategory(self):
        self.Categoryformpopup.show()
        self.Categoryformpopup.activateWindow()
        self.txt_category_name.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)

    def openEditPopUpFormcategory(self):
        self.Categoryformpopup.show()
        self.Categoryformpopup.activateWindow()
        self.btn_edit_popup.setHidden(False)
        self.btn_insert_popup.setHidden(True)
        self.txt_category_name.setFocus()

    def selectRecord(self):
        try:
            self.tbshow.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)

            self.tbshow.setStyleSheet("""
                QTableWidget::item:selected {
                    background-color: blue;
                    color: white;
                }
            """)

            select_row = self.tbshow.currentRow()

            if select_row != -1:
                category_id = self.tbshow.item(select_row, 0).text().strip()
                category_name = self.tbshow.item(select_row, 1).text().strip()
                description = self.tbshow.item(select_row, 2).text().strip()

                self.lbl_category_id.setText(category_id)
                self.lbl_id_popup.setText(category_id)
                self.txt_category_name.setText(category_name)
                self.txt_remark.setText(description)
                self.lbl_category.setText(category_name)

                self.showEditButton()
               

            else:
                self.clearSelectionSettings()
                QMessageBox.information(self, "Warning", "Please select a category to view information.",
                                        QMessageBox.StandardButton.Ok)
        except KeyError as e:
            print(f'KeyError in Select: {e}')
        except ValueError as e:
            print(f'ValueError in Select: {e}')
        except Exception as e:
            print(f'Error in Select: {e}')



    


    # def showSelectCategory(self):
    #     try:
    #         result_category= self.categorycontroller.getCategory()

    #         self.lbl_total.clear()
    #         # self.cmb_category.addItem('No select')
    #         self.categoryData = [] 
           

    #         for item in result_category:
    #             category_name = item.get('category_name', '')
    #             category_id = item.get('category_id', '')
    #             count_category_id = item.get('count_category_id')

    #             if category_name:
                   
    #                 # self.cmb_category.addItem(category_name)
    #                 self.categoryData.append({'category_id': category_id, 
    #                                           'category_name': category_name,
    #                                           'count_category_id': count_category_id})  
    #         count_category_id = self.categoryData[0]["count_category_id"]
    #         # self.cmb_category.addItem(str(category_id))
    #         # self.txt_remark.setText(str(category_id))
    #         self.lbl_total.setText(str(count_category_id))

    #     except KeyError as e:
    #         print(f'KeyError in showSelectCategory: {e}')
    #     except ValueError as e:
    #         print(f'ValueError in showSelectCategory: {e}')
    #     except Exception as e:
    #         print(f'Error in showSelectCategory: {e}')



    def afterSelectAvailable(self):
        try:                                                                        
                category_info = self.getCategoryInfo()

                #Total
                result = self.categorycontroller.getCategory(category_name=category_info["category_name_label"])
                if category_info["category_name_label"]=="":
                    QMessageBox.warning(self, "Alert", " category Name cannot be empty")
                 
                else:
                    if result:
                        first_entry = result[0]
                        self.lbl_total.setText(str(first_entry.get("count_category_id", "")))
                        result_available = self.categorycontroller.getStatusAvailable(category_id=category_info["category_id"])
                        if str(first_entry.get("count_category_id", ""))=="0":
                            self.lbl_available.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_repair.setText(str(first_entry.get("count_category_id", ""))) 
                            self.lbl_broken.setText(str(first_entry.get("count_category_id", "")))
                        else:
                            if  result:
                                first_entry_available = result_available[0]
                                self.lbl_available.setText(str(first_entry_available.get("available", "")))
                                self.afterSelectInUse()
                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database")
                

        except KeyError as e:
            print(f'KeyError in : {e}')
        except ValueError as e:
            print(f'ValueError in: {e}')
        except Exception as e:
            print(f'Error in : {e}')

    def afterSelectInUse(self):
        try:                                                                        
                category_info = self.getCategoryInfo()

                #Total
                result = self.categorycontroller.getCategory(category_name=category_info["category_name_label"])
                if category_info["category_name_label"]=="":
                    QMessageBox.warning(self, "Alert", " category Name cannot be empty")
                 
                else:
                    if result:
                        first_entry = result[0]
                        self.lbl_total.setText(str(first_entry.get("count_category_id", "")))
                        result_in_use = self.categorycontroller.getStatusInUse(category_id=category_info["category_id"])
                        if str(first_entry.get("count_category_id", ""))=="0":
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_repair.setText(str(first_entry.get("count_category_id", ""))) 
                            self.lbl_broken.setText(str(first_entry.get("count_category_id", "")))
                        else:
                            if  result:
                                first_entry_in_use = result_in_use[0]
                                self.lbl_in_use.setText(str(first_entry_in_use.get("in_use", "")))
                                self.afterSelectUnderRepair()
                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database") 

        except KeyError as e:
            print(f'KeyError in : {e}')
        except ValueError as e:
            print(f'ValueError in: {e}')
        except Exception as e:
            print(f'Error in : {e}')

    def afterSelectUnderRepair(self):
        try:                                                                        
                category_info = self.getCategoryInfo()

                #Total
                result = self.categorycontroller.getCategory(category_name=category_info["category_name_label"])
                if category_info["category_name_label"]=="":
                    QMessageBox.warning(self, "Alert", " category Name cannot be empty")
                 
                else:
                    if result:
                        first_entry = result[0]
                        self.lbl_total.setText(str(first_entry.get("count_category_id", "")))
                        result_under_repairing = self.categorycontroller.getStatusUnderRepairing(category_id=category_info["category_id"])
                        if str(first_entry.get("count_category_id", ""))=="0":
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_repair.setText(str(first_entry.get("count_category_id", ""))) 
                            self.lbl_broken.setText(str(first_entry.get("count_category_id", "")))
                        else:
                            if  result:
                                first_entry_under_repairing = result_under_repairing[0]
                                self.lbl_repair.setText(str(first_entry_under_repairing.get("under_repairing", "")))
                                self.afterSelectBroken()
                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database") 

        except KeyError as e:
            print(f'KeyError in : {e}')
        except ValueError as e:
            print(f'ValueError in: {e}')
        except Exception as e:
            print(f'Error in : {e}')
    def afterSelectBroken(self):
        try:                                                                        
                category_info = self.getCategoryInfo()

                #Total
                result = self.categorycontroller.getCategory(category_name=category_info["category_name_label"])
                if category_info["category_name_label"]=="":
                    QMessageBox.warning(self, "Alert", " category Name cannot be empty")
                 
                else:
                    if result:
                        first_entry = result[0]
                        self.lbl_total.setText(str(first_entry.get("count_category_id", "")))
                        result_broken = self.categorycontroller.getStatusBroken(category_id=category_info["category_id"])
                        if str(first_entry.get("count_category_id", ""))=="0":
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_in_use.setText(str(first_entry.get("count_category_id", "")))
                            self.lbl_repair.setText(str(first_entry.get("count_category_id", ""))) 
                            self.lbl_broken.setText(str(first_entry.get("count_category_id", "")))
                        else:
                            if  result:
                                first_entry_broken = result_broken[0]
                                self.lbl_broken.setText(str(first_entry_broken.get("broken", "")))
                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database") 

        except KeyError as e:
            print(f'KeyError in : {e}')
        except ValueError as e:
            print(f'ValueError in: {e}')
        except Exception as e:
            print(f'Error in : {e}')



    def clearSelectionSettings(self):
        self.tbshow.clearSelection()
        self.hideEditButton()
        self.lbl_category_id.clear()
        self.lbl_id_popup.clear()

    def checkSelection(self):
        if not self.tbshow.selectedItems():
            self.clearSelectionSettings()


    def add_info(self):
        try:
            
            category_info = self.getCategoryInfo()

            if category_info is None:
                raise ValueError("No category info returned")

            
            if not category_info["category_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Category name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormcategory()
                self.txt_category_name.setFocus()
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to add it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:

            # Check if all IDs are valid
                    
                    add_result = self.categorycontroller.add_info(
                        category_name=category_info["category_name"],
                        description =category_info["description"]

                    )
                    if add_result:
                        QMessageBox.critical(self, "Warning",
                                            f"Fail to update the information: {add_result}. Please try again.",
                                                QMessageBox.StandardButton.Ok)
                    else:
                        QMessageBox.information(self, "Success", "Category information add successfully.",
                                            QMessageBox.StandardButton.Ok)
                        self.closePopUp()
                        self.loadAndShowData()
            else: 
                self.openInsertPopUpFormcategory()
                self.txt_category_name.setFocus()

        except KeyError as e:
            print(f'KeyError in add_info: {e}')
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
        except Exception as e:
            print(f'Error in add_info: {e}')






    def updateData(self):
        try:
            category_info = self.getCategoryInfo()
            if category_info is None:
                raise ValueError("No category info returned")

            
            if not category_info["category_name"].strip():
                QMessageBox.warning(self, "Validation Error", "Category name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormcategory()
                self.txt_category_name.setFocus()
                return

            if not category_info["category_id"]:
                QMessageBox.warning(self, "Warning", "Please select a category to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                # Perform the update operation
                update_result = self.categorycontroller.updateData(
                    category_id=category_info["category_id"],
                    category_name=category_info["category_name"],
                    description=category_info["description"]
                )
                
                if update_result:
                    
                    QMessageBox.information(self, "Warning",
                                            f"Fail to update the information: {update_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "Category information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
            else:
                self.openEditPopUpFormcategory()
                self.txt_category_name.setFocus()
                

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in category information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)


    def delete_info(self):
        try:
            category_info = self.getCategoryInfo()

            if not category_info["category_id"]:
                QMessageBox.warning(self, "Warning", "Please select a category to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.categorycontroller.deleteData(category_id=category_info["category_id"])

                if delete_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to delete the information: {delete_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "category information deleted successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in category information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in delete_info: {e}",
                                QMessageBox.StandardButton.Ok)

    def getCategoryInfo(self):
        category_id = self.lbl_category_id.text().strip()
        category_name = self.txt_category_name.text().strip()
        category_name_label = self.lbl_category.text().strip()
        description = self.txt_remark.text().strip()

        # data = 'ຫສສ'.encode("utf-8")
        # print(data.decode())

        # for category in self.categoryData:
        #     if category['category_name'] == category_name:
        #         category_id = category['category_id']
        #         break 

        category_info = {
            "category_id": category_id,   
            "category_name": category_name,
            "category_name_label": category_name_label,
            "description":description,
  
        }

    
        return category_info



    
    