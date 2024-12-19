from Menu.form_menu_ui import Ui_Frm_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QMdiSubWindow,QMessageBox
from Employee.employee_form_controller import EmployeeFormController
from Device_info.device_form_controller import FrmDeviceController
from Brand.brand_form_controller import FrmBrandController
from Category.category_form_controller import FrmCategoryController
from Company.company_form_controller import FrmCompanyController
from Department.department_form_controller import FrmDepartmentController
from Device_location.device_location_form_controller import FrmDeviceLocationController
from Supplier.supplier_form_controller import FrmSupplierController
from Users.user_form_controller import FrmuserController
from Positions.position_form_controller import FrmpositionController
from Status.status_form_controller import FrmstatusController
from Device_manager.device_form_manager_controller import FrmDeviceManageController
from History.devive_history_form_controller import FrmDeviceHistoryController
class MenuFormController(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_Frm_MainWindow()
        self.ui.setupUi(self)
        
        self.itm_open_employee = self.ui.itm_Employees
        self.itm_open_device = self.ui.itm_Device
        self.itm_open_brand = self.ui.itm_Brand
        self.itm_open_category = self.ui.itm_Categories
        self.itm_open_company = self.ui.itm_Company
        self.itm_open_department = self.ui.itm_Department
        self.itm_open_device_location = self.ui.itm_Device_Location
        self.itm_open_supplier = self.ui.itm_Suppliers
        self.itm_open_user = self.ui.itm_Users
        self.itm_open_position = self.ui.itm_Position
        self.itm_open_status = self.ui.itm_Device_Status
        self.itm_open_device_manage = self.ui.itm_Device_Management
        self.itm_open_device_history = self.ui.itm_history
     
        self.mdiArea = self.ui.mdiArea  

        # self.mdiArea.subWindowActivated.connect(self.updateActions)
        
        self.initUi()
        self.initSignal()

    def initUi(self):
        self.btn_ok = EmployeeFormController().ui.btn_insert

    def setUserAfterLogin(self, user):
        # print(user)
        self.setWindowTitle(user[0]['name'])
        self.user = user

    def initSignal(self):
        self.itm_open_employee.triggered.connect(self.openEmployeeForm)
        self.itm_open_device.triggered.connect(lambda: self.openDeviceForm(self.user))
        self.itm_open_brand.triggered.connect(self.openBrandForm)
        self.itm_open_category.triggered.connect(self.openCategoryForm)
        self.itm_open_company.triggered.connect(self.openCompanyForm)
        self.itm_open_department.triggered.connect(self.openDepartmentForm)
        self.itm_open_device_location.triggered.connect(self.openDeviceLocationForm)
        self.itm_open_supplier.triggered.connect(self.openSupplierForm)
        self.itm_open_user.triggered.connect(self.openUserForm)
        self.itm_open_position.triggered.connect(self.openPositionForm)
        self.itm_open_status.triggered.connect(self.openStatusForm)
        self.itm_open_device_manage.triggered.connect(lambda: self.openDeviceManageForm(self.user))
        self.itm_open_device_history.triggered.connect(lambda: self.openDeviceHistoryForm(self.user))

    def disableItm(self):
        self.itm_open_employee.setDisabled(True)
        self.itm_open_device.setDisabled(True)

    def enableItm(self):
        self.itm_open_employee.setEnabled(True)
        self.itm_open_device.setEnabled(True)
    

    def openEmployeeForm(self):
        self.employeeformcontroller = EmployeeFormController()
        self.sub_window = self.mdiArea.addSubWindow(self.employeeformcontroller)
        self.sub_window.showMaximized()
        self.employeeformcontroller.loadAndShowData()

    def openDeviceForm(self,user):
        self.deviceformcontroller = FrmDeviceController()
        self.sub_window2 = self.mdiArea.addSubWindow(self.deviceformcontroller)
        self.sub_window2.showMaximized()
        self.deviceformcontroller.setUsername(user)
       
        self.deviceformcontroller.loadAndShowData()


    def openBrandForm(self):
        self.brandformcontroller = FrmBrandController()
        self.sub_window3 = self.mdiArea.addSubWindow(self.brandformcontroller)
        self.sub_window3.showMaximized()
        self.brandformcontroller.loadAndShowData()

    def openCategoryForm(self):
        self.categoryformcontroller = FrmCategoryController()
        self.sub_window4 = self.mdiArea.addSubWindow(self.categoryformcontroller)
        self.sub_window4.showMaximized()
        self.categoryformcontroller.loadAndShowData()

    def openCompanyForm(self):
        self.companyformcontroller = FrmCompanyController()
        self.sub_window5 = self.mdiArea.addSubWindow(self.companyformcontroller)
        self.sub_window5.showMaximized()
        self.companyformcontroller.loadAndShowData()

    def openDepartmentForm(self):
        self.departmentformcontroller = FrmDepartmentController()
        self.sub_window5 = self.mdiArea.addSubWindow(self.departmentformcontroller)
        self.sub_window5.showMaximized()
        self.departmentformcontroller.loadAndShowData()

    def openDeviceLocationForm(self):
        self.devicelocationformcontroller = FrmDeviceLocationController()
        self.sub_window6 = self.mdiArea.addSubWindow(self.devicelocationformcontroller)
        self.sub_window6.showMaximized()
        self.devicelocationformcontroller.loadAndShowData()

    def openSupplierForm(self):
        self.supplierformcontroller = FrmSupplierController()
        self.sub_window7 = self.mdiArea.addSubWindow(self.supplierformcontroller)
        self.sub_window7.showMaximized()
        self.supplierformcontroller.loadAndShowData()

    def openUserForm(self):
        self.userformcontroller = FrmuserController()
        self.sub_window8 = self.mdiArea.addSubWindow(self.userformcontroller)
        self.sub_window8.showMaximized()
        self.userformcontroller.loadAndShowData()

    def openPositionForm(self):
        self.positionformcontroller = FrmpositionController()
        self.sub_window9 = self.mdiArea.addSubWindow(self.positionformcontroller)
        self.sub_window9.showMaximized()
        self.positionformcontroller.loadAndShowData()

    def openStatusForm(self):
        self.statusformcontroller = FrmstatusController()
        self.sub_window10 = self.mdiArea.addSubWindow(self.statusformcontroller)
        self.sub_window10.showMaximized()
        self.statusformcontroller.loadAndShowData()

    def openDeviceManageForm(self,user):
        self.devicemanageformcontroller = FrmDeviceManageController()
        self.sub_window11 = self.mdiArea.addSubWindow(self.devicemanageformcontroller)
        self.sub_window11.showMaximized()
        self.devicemanageformcontroller.lbl_username.clear()
        self.devicemanageformcontroller.setUsername(user)
        self.devicemanageformcontroller.loadAndShowData()
    
    def openDeviceHistoryForm(self,user):
        self.devicehistoryformcontroller = FrmDeviceHistoryController()
        self.sub_window12 = self.mdiArea.addSubWindow(self.devicehistoryformcontroller)
        self.sub_window12.showMaximized()
        self.devicehistoryformcontroller.setUsername(user)
       
        self.devicehistoryformcontroller.loadAndShowData()

    def updateActions(self, sub_window2):
        if sub_window2:
            self.itm_open_device.setDisabled(True)
        else:
            self.itm_open_device.setEnabled(True)

    
    def closePopUpForm(self):
        for dialog in self.popup_forms:
            dialog.close()
        self.popup_forms.clear()


    def afterCloseEvent(self):
        print('Hi')
        self.closePopUpForm()
        return

    def closeAllSubWindows(self):
        # Close all subwindows in the MDI area
        self.mdiArea.closeAllSubWindows()

        # Optionally, if you want to explicitly ensure the forms are set to None:
        self.employeeformcontroller = None
        self.deviceformcontroller = None
        self.brandformcontroller = None
        self.categoryformcontroller = None
        self.companyformcontroller = None
        self.departmentformcontroller = None
        self.devicelocationformcontroller = None
        self.supplierformcontroller = None
        self.userformcontroller = None
        self.positionformcontroller = None
        self.statusformcontroller = None
        self.devicemanageformcontroller = None
        self.devicehistoryformcontroller = None