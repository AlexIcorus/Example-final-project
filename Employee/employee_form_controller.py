import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QApplication, QMessageBox,QHeaderView
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QFont
from Employee.employee_controller import EmployeeController
from Employee.form_employees_ui import Ui_frm_employee
from Employee.employee_form_popup import EmployeeFormPopup
from Employee.form_search_popup import EmployeeFormSearchPopup

class EmployeeFormController(QMainWindow):
    def __init__(self):
        super().__init__()
     
        self.employeecontroller = EmployeeController()
        self.employeeformpopup = EmployeeFormPopup()
        self.employeeformsearchpopup = EmployeeFormSearchPopup()
        self.ui = Ui_frm_employee()
        self.ui.setupUi(self)
        self.setCentralWidget(self.ui.frame_Main)
        self.initUi()
        self.initSignal()
        self.setupTable()
        self.validateFormSignal()
        self.getCompanyID()
        self.departmentData = [] 
             

       
    def initUi(self):
        self.tbshow = self.ui.tb_show
        self.btn_ok = self.ui.btn_insert
        self.btn_delete = self.ui.btn_delete
        self.btn_edit = self.ui.btn_edit
        self.unselect = self.ui.frame
        self.lbl_id = self.ui.lbl_id
        self.lbl_id_popup = self.employeeformpopup.ui.lbl_id_popup
        self.btn_clear_popup = self.employeeformpopup.ui.btn_clear_form
        self.btn_insert_popup = self.employeeformpopup.ui.btn_insert
        self.btn_cancel = self.employeeformpopup.ui.btn_cancel
        self.btn_edit_popup = self.employeeformpopup.ui.btn_edit
        self.rb_male = self.employeeformpopup.ui.rb_Male
        self.rb_female = self.employeeformpopup.ui.rb_Female
        self.txt_name = self.employeeformpopup.ui.txt_name
        self.txt_lastname = self.employeeformpopup.ui.txt_surname
        self.txt_address = self.employeeformpopup.ui.txt_address
        self.txt_email = self.employeeformpopup.ui.txt_email
        self.txt_emp_code = self.employeeformpopup.ui.txt_emp_code
        self.txt_phone = self.employeeformpopup.ui.txt_phone
        self.txt_search = self.ui.txt_search
        self.cmb_company = self.employeeformpopup.ui.cmb_company
        self.cmb_department = self.employeeformpopup.ui.cmb_department
        self.cmb_position = self.employeeformpopup.ui.cmb_position
        self.btn_refresh = self.ui.btn_refresh
        self.validate_name = self.employeeformpopup.ui.vld_name
        self.validate_last_name = self.employeeformpopup.ui.vld_last_name
        self.validate_emp_code = self.employeeformpopup.ui.vld_emp_code
        self.validate_company = self.employeeformpopup.ui.vld_company
        self.validate_position = self.employeeformpopup.ui.vld_position
        self.validate_department = self.employeeformpopup.ui.vld_department
        self.btn_search_data = self.ui.btn_search
        self.btn_search_name = self.employeeformpopup.ui.btn_search_name
        self.btn_search_department = self.employeeformpopup.ui.btn_search_department
        self.btn_search_position = self.employeeformpopup.ui.btn_search_position
        self.btn_search_name_popup = self.employeeformsearchpopup.ui.btn_search_name_lastname
        self.btn_search_department_popop = self.employeeformsearchpopup.ui.btn_search_department
        self.btn_search_position_popup = self.employeeformsearchpopup.ui.btn_search_position
        self.btn_cancel_search_popup = self.employeeformsearchpopup.ui.btn_search_cancel
        
        self.txt_search_popup = self.employeeformsearchpopup.ui.txt_search_popup
        
        self.setupStyleSheet()

    
    def initSignal(self): 
        self.btn_delete.clicked.connect(self.clearSelectionSettings)
        self.btn_ok.clicked.connect(self.clearForm)
        self.btn_ok.clicked.connect(self.openInsertPopUpFormEmployee)
        self.btn_edit.clicked.connect(self.openEditPopUpFormEmployee)
        self.tbshow.clicked.connect(self.selectRecord)
        self.btn_cancel.clicked.connect(self.closePopUp)
        self.btn_clear_popup.clicked.connect(self.clearForm)
        self.btn_insert_popup.clicked.connect(self.add_info)
        self.btn_refresh.clicked.connect(self.loadAndShowData)
        self.btn_edit_popup.clicked.connect(self.updateData)
        self.btn_delete.clicked.connect(self.delete_info)
        self.cmb_company.currentIndexChanged.connect(self.getCompanyID)
        self.btn_search_data.clicked.connect(self.searchData)
        self.txt_search.returnPressed.connect(self.searchData)
        self.btn_search_name.clicked.connect(self.openNameSearchFormEmployee)
        self.btn_search_name_popup.clicked.connect(self.afterSearchNameLastname)
        self.btn_search_department.clicked.connect(self.openDepartmentSearchFormEmployee)
        self.btn_search_position.clicked.connect(self.openPositionSearchFormEmployee)
        self.btn_search_department_popop.clicked.connect(self.afterSearchDepartment)
        self.btn_search_position_popup.clicked.connect(self.afterSearchPosition)
        self.btn_cancel_search_popup.clicked.connect(self.clearSearch)
        self.updatePositionDepartmentCompany()
        self.getSameData()
        self.hideEditButton()
        self.turnNormal()

    def validateFormSignal(self):
        self.txt_name.textChanged.connect(self.turnNormalName)
        self.txt_lastname.textChanged.connect(self.turnNormalLastName)
        self.txt_emp_code.textChanged.connect(self.turnNormalEmpCode)
        self.cmb_company.currentIndexChanged.connect(self.turnNormalCompany)
        self.cmb_department.currentIndexChanged.connect(self.turnNormalDepartment)
        self.cmb_position.currentIndexChanged.connect(self.turnNormalPosition)
       

    def setupStyleSheet(self):
        self.style_normal = "background-color: white;color: black; font-size: 12px; height: 40px;font: 18pt ;"
        self.style_validate = """
                        border: 2px solid red; 
                        background-color: white; 
                        border-radius: 5px; 
                        color: black; 
                        font: 18pt; 
                        height: 40px;
                        """
    def turnNormal(self):
        self.txt_phone.setStyleSheet(self.style_normal) 
        self.txt_email.setStyleSheet(self.style_normal)
        self.txt_address.setStyleSheet(self.style_normal)
    def turnNormalName(self):  
            self.txt_name.setStyleSheet(self.style_normal)
            self.validate_name.setHidden(True)
    def turnNormalLastName(self):    
            self.txt_lastname.setStyleSheet(self.style_normal)
            self.validate_last_name.setHidden(True)
    def turnNormalEmpCode(self): 
            self.txt_emp_code.setStyleSheet(self.style_normal)
            self.validate_emp_code.setHidden(True)
    def turnNormalCompany(self): 
            self.cmb_company.setStyleSheet(self.style_normal)
            self.validate_company.setHidden(True)
    def turnNormalDepartment(self): 
            self.cmb_department.setStyleSheet(self.style_normal)
            self.validate_department.setHidden(True)
    def turnNormalPosition(self): 
            self.cmb_position.setStyleSheet(self.style_normal)
            self.validate_position.setHidden(True)



    def hideEditButton(self):
        self.btn_edit.setHidden(True)
        self.btn_delete.setHidden(True)
        self.lbl_id.setHidden(True)
        self.lbl_id_popup.setHidden(True)
        self.validate_name.setHidden(True)
        self.validate_last_name.setHidden(True)
        self.validate_emp_code.setHidden(True)
        self.validate_company.setHidden(True)
        self.validate_department.setHidden(True)
        self.validate_position.setHidden(True)
        

    
    def showEditButton(self):
        self.btn_edit.setHidden(False)
        self.btn_delete.setHidden(False)

    

    def openInsertPopUpFormEmployee(self):
        self.employeeformpopup.show()
        self.employeeformpopup.activateWindow()
        self.txt_name.setFocus()
        self.btn_edit_popup.setHidden(True)
        self.btn_insert_popup.setHidden(False)
        self.validateFormSignal()
       

    def openEditPopUpFormEmployee(self):
        self.employeeformpopup.show()
        self.employeeformpopup.activateWindow()
        self.btn_edit_popup.setHidden(False)
        self.btn_insert_popup.setHidden(True)
        self.txt_name.setFocus()

    def openNameSearchFormEmployee(self):
        self.employeeformsearchpopup.show()
        self.employeeformsearchpopup.activateWindow()
        self.employeeformsearchpopup.setWindowTitle("Search Form Employee Name and Lastname")
        self.btn_search_name_popup.setHidden(False)
        self.btn_search_department_popop.setHidden(True)
        self.btn_search_position_popup.setHidden(True)
        self.txt_search_popup.setFocus()
       
    def openDepartmentSearchFormEmployee(self):
        self.employeeformsearchpopup.show()
        self.employeeformsearchpopup.activateWindow()
        self.employeeformsearchpopup.setWindowTitle("Search Form Employee Department")
        self.btn_search_name_popup.setHidden(True)
        self.btn_search_department_popop.setHidden(False)
        self.btn_search_position_popup.setHidden(True)
        self.txt_search_popup.setFocus()

    def openPositionSearchFormEmployee(self):
        self.employeeformsearchpopup.show()
        self.employeeformsearchpopup.activateWindow()
        self.employeeformsearchpopup.setWindowTitle("Search Form Employee Position")
        self.btn_search_name_popup.setHidden(True)
        self.btn_search_department_popop.setHidden(True)
        self.btn_search_position_popup.setHidden(False)
        self.txt_search_popup.setFocus()

    #Aftersearch popup and set Data on lineEdit 

    def afterSearchNameLastname(self):
        try:                                                                        
                employee_info = self.getEmployeeInfo()
                result = self.employeecontroller.afterSearchNameLastname(search_data=employee_info["search_line_edit"])
                if employee_info["search_line_edit"]=="":
                    QMessageBox.warning(self, "Alert", " data cannot be empty")
                    self.employeeformpopup.activateWindow()
                    self.employeeformsearchpopup.activateWindow()
                else:
                    if result:
                        first_entry = result[0]
                        self.txt_name.setText(first_entry.get("name", ""))
                        self.txt_lastname.setText(first_entry.get("surname", ""))
                        self.employeeformsearchpopup.close()

                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database")   
                        self.employeeformpopup.activateWindow()
                        self.employeeformsearchpopup.activateWindow() 
                        
        except Exception as e:
            print(e)

    def clearSearch(self):
        self.txt_search_popup.clear()
        self.employeeformsearchpopup.close()


    def afterSearchDepartment(self): 
        try:                                                                        
                employee_info = self.getEmployeeInfo()
                result = self.employeecontroller.afterSearchDepartment(search_data=employee_info["search_line_edit"])
              
                if employee_info["search_line_edit"]=="":
                    QMessageBox.warning(self, "Alert", " data cannot br empty")
                    self.employeeformpopup.activateWindow()
                    self.employeeformsearchpopup.activateWindow()
                else:
                    if result:
                        first_entry = result[0]
                        self.cmb_department.setCurrentText(first_entry.get("name_la", ""))
                        self.employeeformsearchpopup.close()
                        print("Search Successfull")

                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database") 
                        self.employeeformpopup.activateWindow()
                        self.employeeformsearchpopup.activateWindow()
                             
        except Exception as e:
            print(e)

    def afterSearchPosition(self):
        try:                                                                        
                employee_info = self.getEmployeeInfo()
                result = self.employeecontroller.afterSearchPosition(search_data=employee_info["search_line_edit"])
                if employee_info["search_line_edit"]=="":
                    QMessageBox.warning(self, "Alert", " data cannot br empty")
                    self.employeeformpopup.activateWindow()
                    self.employeeformsearchpopup.activateWindow()
                else:
                    if result:
                        first_entry = result[0]
                        self.cmb_position.setCurrentText(first_entry.get("name_en", ""))
                        self.employeeformsearchpopup.close()

                    else:
                        QMessageBox.information(self, "No Data Found", "No data found in Database") 
                        self.employeeformpopup.activateWindow()
                        self.employeeformsearchpopup.activateWindow()
                          
        except Exception as e:
            print(e)

    def clearForm(self):
        self.txt_name.clear()
        self.txt_lastname.clear()
        self.txt_address.clear()
        self.txt_email.clear()
        self.txt_emp_code.clear()
        self.txt_phone.clear()
        self.txt_search.clear()
        self.updatePositionDepartmentCompany()
        self.rb_male.setAutoExclusive(False)
        self.rb_female.setAutoExclusive(False)
        self.rb_male.setChecked(False)
        self.rb_female.setChecked(False)
        self.rb_male.setAutoExclusive(True)
        self.rb_female.setAutoExclusive(True)
        self.txt_name.setFocus()
        

    def clearValidate(self):
        self.validate_name.setHidden(True)
        self.validate_last_name.setHidden(True)
        self.validate_emp_code.setHidden(True)
        self.txt_name.setStyleSheet(self.style_normal)
        self.txt_lastname.setStyleSheet(self.style_normal)
        self.txt_emp_code.setStyleSheet(self.style_normal)
        


    def closePopUp(self):
        self.employeeformpopup.close()
        self.clearValidate()
        self.rb_male.setAutoExclusive(False)
        self.rb_female.setAutoExclusive(False)
        self.rb_male.setChecked(False)
        self.rb_female.setChecked(False)
        self.rb_male.setAutoExclusive(True)
        self.rb_female.setAutoExclusive(True)

        
    def setupTable(self):
    
        self.tbshow.setColumnCount(11)
        self.tbshow.setColumnHidden(0, True)
        self.tbshow.setHorizontalHeaderLabels([
            "ID", "Name", "Surname", "Address", "Phone Number",
            "Email", "Gender", "Emp Code", "Position ID", 
            "Department ID", "Company ID"
        ])
        
        # Set the resize mode of the columns to stretch
        header = self.tbshow.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Define the column widths
        column_widths = [50, 200, 200, 200, 100, 150, 70, 80, 100, 100, 100]
        # Apply the column widths
        for index, width in enumerate(column_widths):
            self.tbshow.setColumnWidth(index, width)

        header.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # ID column to resize to content
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive) 
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive) 
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive) 
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(8, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(9, QHeaderView.ResizeMode.Interactive)
        header.setSectionResizeMode(10, QHeaderView.ResizeMode.Interactive)    # Name column to be resizable
        self.tbshow.setColumnWidth(1, 150)
        self.tbshow.setColumnWidth(2, 200)
        self.tbshow.setColumnWidth(3, 200)
        self.tbshow.setColumnWidth(4, 200)
        self.tbshow.setColumnWidth(5, 250)
        self.tbshow.setColumnWidth(6, 80)
        self.tbshow.setColumnWidth(7, 200)
        self.tbshow.setColumnWidth(8, 200)
        self.tbshow.setColumnWidth(9, 200)
        self.tbshow.setColumnWidth(10, 200)

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
            employee_id = self.tbshow.item(select_row, 0).text().strip()
            employee_name = self.tbshow.item(select_row, 1).text().strip()
            surname = self.tbshow.item(select_row, 2).text().strip()
            address = self.tbshow.item(select_row, 3).text().strip()
            phone = self.tbshow.item(select_row, 4).text().strip()
            email = self.tbshow.item(select_row, 5).text().strip()
            gender = self.tbshow.item(select_row, 6).text().strip()
            emp_code = self.tbshow.item(select_row, 7).text().strip()
            position = self.tbshow.item(select_row, 8).text().strip()
            department = self.tbshow.item(select_row, 9).text().strip()
            company = self.tbshow.item(select_row, 10).text().strip()

            # Update the labels and combo boxes with the selected row data
            self.lbl_id.setText(employee_id)
            self.lbl_id_popup.setText(employee_id)
            self.txt_name.setText(employee_name)
            self.txt_lastname.setText(surname)
            self.txt_address.setText(address)
            self.txt_phone.setText(phone)
            self.txt_email.setText(email)
            if gender == 'M':
                self.rb_male.setChecked(True)
            else:
                self.rb_female.setChecked(True)
            self.txt_emp_code.setText(emp_code)
            self.cmb_position.setCurrentText(position)
            self.cmb_department.setCurrentText(department)
            self.cmb_company.setCurrentText(company)           
                

            self.showEditButton()

        else:
            self.clearSelectionSettings()
            QMessageBox.information(self, "Warning", "Please select a company to view information.",
                                    QMessageBox.StandardButton.Ok)

    
    def clearSelectionSettings(self):
        self.tbshow.clearSelection() 
      
       
    def loadAndShowData(self):
       
        try:
            result = self.employeecontroller.selectEmployeeData()  # Ensure this method exists and fetches data
            self.showData(result)
            # print(result)
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
                    info.get("emp_id", ""),
                    info.get("name", ""),
                    info.get("surname", ""),
                    info.get("address", ""),
                    info.get("phone_number", ""),
                    info.get("email", ""),
                    info.get("gender", ""),
                    info.get("emp_code", ""),
                    info.get("name_en", ""),
                    info.get("name_la", ""),
                    info.get("company_name", "")
                ]

                for column, item in enumerate(info_list):
                    cell_item = QTableWidgetItem(str(item))
                    cell_item.setFont(font)
                    self.tbshow.setItem(row, column, cell_item)
        else:
            self.tbshow.setRowCount(0)
    

    def getGender(self):
        if self.rb_male.isChecked():
            print("I'm a man")
            return
        else:
            print("I'm a Woman 555")
            return

    def getEmployeeInfo(self):
        employee_id = self.lbl_id.text().strip()
        name = self.txt_name.text().strip()
        lastname = self.txt_lastname.text().strip()
        address = self.txt_address.text().strip()
        phone = self.txt_phone.text().strip()
        email = self.txt_email.text().strip()
        emp_code = self.txt_emp_code.text().strip()
        position_name = self.cmb_position.currentText().strip()
        department_name = self.cmb_department.currentText().strip()
        company_name = self.cmb_company.currentText().strip()
        search_data = self.txt_search.text().strip()
        search_line_edit = self.txt_search_popup.text().strip()
        
        
        # Determine gender
        if self.rb_male.isChecked():
            gender = 'M'
        else:
            gender = 'F'

        # Initialize IDs
        position_id = None
        department_id = None
        company_id = None

        # Find position ID
        for position in self.positionData:
            if position['position_name'] == position_name:
                position_id = position['position_id']
                break

        # Find department ID
        for department in self.departmentData:
            if department['department_name'] == department_name:
                department_id = department['id']
                break

        # Find company ID
        for company in self.companyData:
            if company['company_name'] == company_name:
                company_id = company['company_id']
                break

        employee_info = {
            "employee_id" :employee_id,
            "name": name,
            "last_name": lastname,
            "address": address,
            "phone": phone,
            "email": email,
            "gender": gender,
            "emp_code": emp_code,
            "position_id": position_id,
            "department_id": department_id,
            "company_id": company_id,
            "search_data": search_data,
            "search_line_edit": search_line_edit
        }

        print("employeeData:", employee_info)
        return employee_info

    def getSameData(self):
        try:
          
            result_check = self.employeecontroller.selectEmployeeData()
            self.checkSameData = [] 
            

            for item in result_check:
                name = item.get('name', '')
                lastname = item.get('surname', '')

                if name or lastname :
                    self.checkSameData.append({'name': name, 'surname': lastname})
                    print("Same Data here",self.checkSameData)
                    

        except Exception as e:
            print('Exception occurred:', e)
    


    def updatePositionDepartmentCompany(self):
        try:
            # Company
            result_company = self.employeecontroller.getCompany()

            self.cmb_company.clear()
            self.cmb_company.addItem('No select')
            self.companyData = [] 

            for item in result_company:
                company_name = item.get('company_name', '')
                company_id = item.get('company_id', '')

                if company_name:
                    self.cmb_company.addItem(company_name)
                    self.companyData.append({'company_id': company_id, 'company_name': company_name})
                    
        
            
         
            #Position

            result_position = self.employeecontroller.getPosition()

            self.cmb_position.clear()
            self.cmb_position.addItem('No select')
            self.positionData = [] 

            for item in result_position:
                position_name = item.get('name_en', '')
                position_id = item.get('position_id', '')

                if position_name:
                    self.cmb_position.addItem(position_name)
                    self.positionData.append({'position_id': position_id, 'position_name': position_name})  
        except Exception as e:
            print('Exception occurred:', e)
    

    def add_info(self):
        try:
            employee_info = self.getEmployeeInfo()

            if employee_info is None:
                QMessageBox.critical(self, "Error", "Failed to retrieve employee data.",
                                    QMessageBox.StandardButton.Ok)
                return
            
            if not employee_info.get("name", "") and not employee_info.get("last_name", "") and not employee_info.get("emp_code", "") and "No Select":
                self.txt_name.setStyleSheet(self.style_validate)
                self.txt_lastname.setStyleSheet(self.style_validate)
                self.txt_emp_code.setStyleSheet(self.style_validate)
                self.validate_name.setHidden(False)
                self.validate_last_name.setHidden(False)
                self.validate_emp_code.setHidden(False)
                self.validate_company.setHidden(False)
                self.validate_department.setHidden(False)
                self.validate_position.setHidden(False)
                self.txt_name.setFocus()
                
                return

            # Check if essential fields are present
            elif not employee_info.get("name", "").strip() and not employee_info.get("last_name", ""):
                self.txt_name.setStyleSheet(self.style_validate)
                self.txt_lastname.setStyleSheet(self.style_validate)
                self.validate_name.setHidden(False)
                self.validate_last_name.setHidden(False)
                return
            
            elif not employee_info.get("name", "").strip() and not employee_info.get("emp_code", ""):
                self.txt_name.setStyleSheet(self.style_validate)
                self.txt_emp_code.setStyleSheet(self.style_validate)
                self.validate_name.setHidden(False)
                self.validate_emp_code.setHidden(False)
                return
            
            elif not employee_info.get("last_name", "").strip() and not employee_info.get("emp_code", ""):
                self.txt_lastname.setStyleSheet(self.style_validate)
                self.txt_emp_code.setStyleSheet(self.style_validate)
                self.validate_last_name.setHidden(False)
                self.validate_emp_code.setHidden(False)
                return
            
            elif not employee_info.get("last_name", "").strip():
                self.txt_lastname.setStyleSheet(self.style_validate)
                self.validate_last_name.setHidden(False)
                return
            
            # Check if essential fields are present
            elif not employee_info.get("emp_code", "").strip():
                self.txt_emp_code.setStyleSheet(self.style_validate)
                self.validate_emp_code.setHidden(False)
                return
            
            elif not employee_info.get("name", "").strip():
                self.txt_name.setStyleSheet(self.style_validate)
                self.validate_name.setHidden(False)
                return
            
            elif not employee_info["company_id"] and "No Select":
                # QMessageBox.warning(self, "Validation Error", "Company name must not be empty.",
                #                     QMessageBox.StandardButton.Ok)
                self.openInsertPopUpFormEmployee()
                self.validate_company.setHidden(False)
                return
            
            elif not employee_info["department_id"] and "No Select":
               
                self.openInsertPopUpFormEmployee()
                self.validate_department.setHidden(False)
                return
            
            elif not employee_info["position_id"] and "No Select":
               
                self.openInsertPopUpFormEmployee()
                self.validate_position.setHidden(False)
                return
            
            else:
                self.openInsertPopUpFormEmployee()
            
            # Check if essential fields are present
            if not employee_info.get("gender") :
                self.openInsertPopUpFormEmployee()
                return
            


            selected_option = QMessageBox.warning(
            self, "Warning", "Are you sure you want to add this employee?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )

            if selected_option == QMessageBox.StandardButton.Yes:
                name_exists = False
                for same_data in self.checkSameData:
                    if employee_info["name"] == same_data["name"] and employee_info["last_name"] == same_data["surname"]:
                        QMessageBox.information(
                            self, "Data Check", f"This Name:'{employee_info['name']} {employee_info["last_name"]}' is already in the database.",
                            QMessageBox.StandardButton.Ok
                        )
                        name_exists = True
                        break

                if not name_exists:
                    add_result = self.employeecontroller.insertEmployeeData(
                        name=employee_info["name"], 
                        surname=employee_info["last_name"],
                        address=employee_info["address"],
                        phone=employee_info["phone"],
                        email=employee_info["email"],
                        emp_code=employee_info["emp_code"],
                        gender=employee_info["gender"],
                        position_id=employee_info["position_id"],
                        department_id=employee_info["department_id"],
                        company_id=employee_info["company_id"]
                    )

                    if add_result:  # Assuming add_result is an error message on failure
                        QMessageBox.critical(
                            self, "Error",
                            f"Failed to add the employee information: {add_result}. Please try again.",
                            QMessageBox.StandardButton.Ok
                        )
                    else:
                        QMessageBox.information(
                            self, "Success", "Employee information added successfully.",
                            QMessageBox.StandardButton.Ok
                        )
                        self.closePopUp()
                        self.loadAndShowData()
            else:
                self.openInsertPopUpFormEmployee()


        except KeyError as e:
            print(f'KeyError in add_info: {e}')
            QMessageBox.critical(self, "Error", f"A KeyError occurred: {str(e)}. Please check the input data.",
                                QMessageBox.StandardButton.Ok)
        except ValueError as e:
            print(f'ValueError in add_info: {e}')
            QMessageBox.critical(self, "Error", f"ValueError: {str(e)}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            print(f'Error in add_info: {e}')
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}",
                                QMessageBox.StandardButton.Ok)


    
    def getCompanyID(self):
        try:
            current_index = self.cmb_company.currentIndex()
            if self.cmb_company.currentText() != 'No select' and current_index >= 0:
                company_id = self.companyData[current_index - 1]['company_id']
                print("company_id", company_id)
                
                # Call getDepartment with the company_id argument
                result_department = self.employeecontroller.getDepartment(company_id=str(company_id))
                
                # Department
                self.cmb_department.blockSignals(True) 
                self.cmb_department.clear()
                self.cmb_department.addItem('No select')
                self.departmentData = []


                for item in result_department:
                    department_name = item.get('name_la', '')
                    department_id = item.get('id', '')

                    if department_name:
                        self.cmb_department.addItem(department_name)
                        self.departmentData.append({'id': department_id, 'department_name': department_name})
                        
                self.cmb_department.blockSignals(False)  # Unblock signals
                self.cmb_department.setCurrentText(department_name)
                
            
            else:
                print("Error: No company selected")
                self.cmb_department.clear()
                self.cmb_department.addItem('No select')
        except Exception as e:
            print(f"Error: {e}")

    def updateData(self):
        
        try:
            employee_info = self.getEmployeeInfo()
            if employee_info is None:
                QMessageBox.critical(self, "Error", "Failed to retrieve employee data.",
                                    QMessageBox.StandardButton.Ok)
                return

            # Check if essential fields are present
            if not employee_info.get("name", "").strip():
                QMessageBox.warning(self, "Validation Error", "Name must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormEmployee()
                return
            
            # Check if essential fields are present
            if not employee_info.get("emp_code", "").strip():
                QMessageBox.warning(self, "Validation Error", "Employee Code must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormEmployee()
                return
            
            # Check if essential fields are present
            if not employee_info.get("gender", "") :
                QMessageBox.warning(self, "Validation Error", "Gender must not be empty.",
                                    QMessageBox.StandardButton.Ok)
                self.openEditPopUpFormEmployee()
                return
            if self.cmb_company.currentIndex() == -1:
                self.cmb_company.setStyleSheet(self.style_validate)
                self.validate_company.setHidden(False)
                valid = False
            if self.cmb_department.currentIndex() == -1:
                self.cmb_department.setStyleSheet(self.style_validate)
                self.validate_department.setHidden(False)
                valid = False
            if self.cmb_position.currentIndex() == -1:
                self.cmb_position.setStyleSheet(self.style_validate)
                self.validate_position.setHidden(False)
                valid = False
            
            

            # Ensure the brand_id is available before proceeding with the update
            if not employee_info["employee_id"]:
                QMessageBox.warning(self, "Warning", "Please select a employee to update.",
                                    QMessageBox.StandardButton.Ok)
                return
            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to update it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                     
                        
                # Perform the update operation
                update_result = self.employeecontroller.updateData(
                    employee_id = employee_info["employee_id"],
                    name=employee_info["name"], 
                    surname=employee_info["last_name"],
                    address=employee_info["address"],
                    phone=employee_info["phone"],
                    email=employee_info["email"],
                    emp_code=employee_info["emp_code"],
                    gender=employee_info["gender"],
                    position_id=employee_info["position_id"],
                    department_id=employee_info["department_id"],
                    company_id=employee_info["company_id"]
                )

                if update_result:
                    
                    QMessageBox.information(self, "Warning",
                                            f"Fail to update the information: {update_result}. Please try again.",
                                            QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "employee information updated successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()
            else:
                self.openEditPopUpFormEmployee()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in employee information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in updateData: {e}",
                                QMessageBox.StandardButton.Ok)

    def searchData(self):
        try:
            font = QFont()
            font.setPointSize(10)
            employee_info = self.getEmployeeInfo()
            result = self.employeecontroller.searchData(select_data=employee_info["search_data"])
            if employee_info["search_data"]=="":
                self.loadAndShowData()
            else:
                if result:
                    self.tbshow.setRowCount(len(result))
                    for row, info in enumerate(result):
                        info_list = [
                            info.get("emp_id", ""),
                            info.get("name", ""),
                            info.get("surname", ""),
                            info.get("address", ""),
                            info.get("phone_number", ""),
                            info.get("email", ""),
                            info.get("gender", ""),
                            info.get("emp_code", ""),
                            info.get("name_en", ""),
                            info.get("name_la", ""),
                            info.get("company_name", "")
                        ]

                        for column, item in enumerate(info_list):
                            cell_item = QTableWidgetItem(str(item))
                            cell_item.setFont(font)
                            self.tbshow.setItem(row, column, cell_item)

                        self.employeeformpopup.close()
                else:
                    self.tbshow.setRowCount(0)
                    QMessageBox.information(self, "No Data Found", "No data found in Database")
                    
                    self.loadAndShowData()


        except Exception as e:
            print(e)

    def delete_info(self):
        try:
            employee_info = self.getEmployeeInfo()

            if not employee_info["employee_id"]:
                QMessageBox.warning(self, "Warning", "Please select a employee to delete.",
                                    QMessageBox.StandardButton.Ok)
                return

            selected_option = QMessageBox.warning(self, "Warning", "Are you sure you want to delete it?",
                                                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)

            if selected_option == QMessageBox.StandardButton.Yes:
                delete_result = self.employeecontroller.deleteData(
                    employee_id=employee_info["employee_id"]
                    )

                if delete_result:
                    QMessageBox.warning(self, "Warning",
                                        f"Failed to delete the information: {delete_result}. Please try again.",
                                        QMessageBox.StandardButton.Ok)
                else:
                    QMessageBox.information(self, "Success", "employee information deleted successfully.",
                                            QMessageBox.StandardButton.Ok)
                    self.closePopUp()
                    self.loadAndShowData()

        except KeyError as e:
            QMessageBox.critical(self, "Error", f"KeyError: Missing key in employee information: {e}",
                                QMessageBox.StandardButton.Ok)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error in delete_info: {e}",
                                QMessageBox.StandardButton.Ok)

    