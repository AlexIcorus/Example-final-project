from Database.connect_database import ConnectDatabase

class EmployeeController:
    def __init__(self):
        self.db = ConnectDatabase()

    def selectEmployeeData(self):
        self.db.connectDB()
        sql = """SELECT e.emp_id ,e.name,e.surname,e.address,e.phone_number,e.email,
        e.gender,e.emp_code,p.name_en,d.name_la,c.company_name
        FROM employees e join positions
        p on p.position_id = e.position_id join departments 
        d on d.id = e.department_id join companies 
        c on c.company_id = e.company_id 
        WHERE e.deleted_at IS NULL order by e.emp_id"""
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()

    def insertEmployeeData(self,name,surname,address,phone,email,gender,emp_code,position_id,department_id,company_id):
            self.db.connectDB()
            sql = f"""insert into 
            employees(name,surname,address,phone_number,email,gender,emp_code,position_id,department_id,company_id,created_at) 
            values('{name}','{surname}','{address}','{phone}','{email}'
            ,'{gender}','{emp_code}','{position_id}','{department_id}','{company_id}',NOW())"""
            try:
                self.db.cursor.execute(sql)
                self.db.con.commit()
                return None
            except Exception as e:
                self.db.con.rollback()
                print(e)
            finally:
                self.db.con.close()

    def updateData(self,employee_id,name,surname,address,phone,email,gender,emp_code,position_id,department_id,company_id):
        self.db.connectDB()
        sql=f"""
            update employees set 
            name='{name}',surname='{surname}',address='{address}',phone_number='{phone}',email='{email}'
            ,gender='{gender}',emp_code='{emp_code}',position_id='{position_id}',department_id='{department_id}',company_id='{company_id}',updated_at = NOW()
            where emp_id = '{employee_id}' and deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            self.db.con.commit()
            
        except Exception as e:
            self.db.con.rollback()
            print(e)
        finally:
            self.db.con.close()

    def searchData(self,select_data):
        self.db.connectDB()
        sql=f"""
           select e.emp_id, e.name,e.surname,e.address,e.phone_number,e.email,e.gender,e.emp_code,p.name_en,d.name_la,c.company_name 
           from employees e join positions p on p.position_id = e.position_id join departments d on d.id = e.department_id join companies c
           on c.company_id = e.company_id where 
           (e.emp_id like '%{select_data}%' or e.name like '%{select_data}%' or e.surname like'%{select_data}%' or
           e.address like '%{select_data}%' or e.phone_number like '%{select_data}%' or e.email like'%{select_data}%' or
           e.gender like '%{select_data}%' or e.emp_code like '%{select_data}%' or p.name_en like'%{select_data}%' or
            d.name_la like '%{select_data}%' or c.company_name like '%{select_data}%' )and e.deleted_at is null
            order by e.emp_id
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            print("Search Data",result)
            return result
            
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return []
        finally:
            self.db.con.close()

    def afterSearchNameLastname(self, search_data):
        self.db.connectDB()
        sql = f"""
        SELECT name, surname FROM employees
        WHERE (name LIKE '%{search_data}%' OR surname LIKE '%{search_data}%')
        AND deleted_at IS NULL order by emp_id
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            self.db.con.rollback()
            print(e)
          
        finally:
            self.db.con.close()


    def afterSearchDepartment(self, search_data):
        self.db.connectDB()
        sql = f"""
        SELECT name_la FROM departments
        WHERE name_la LIKE '%{search_data}%'
        AND deleted_at IS NULL order by id
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            self.db.con.rollback()
            print(e)
          
        finally:
            self.db.con.close()

    def afterSearchPosition(self, search_data):
        self.db.connectDB()
        sql = f"""
        SELECT name_en FROM positions
        WHERE (name_en LIKE '%{search_data}%')
        AND deleted_at IS NULL order by position_id
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            self.db.con.rollback()
            print(e)
          
        finally:
            self.db.con.close()


    def deleteData(self,employee_id):
            self.db.connectDB()
            sql = f"""
            update employees set deleted_at = NOW() where emp_id = '{employee_id}' and deleted_at is null
            """
            try:
                self.db.cursor.execute(sql)
                self.db.con.commit()
            except Exception as e:
                self.db.con.rollback()
                print(e)
                return e
            finally:
                self.db.con.close()

    def getPosition(self):
        
        self.db.connectDB()
       
        sql = """
            select position_id, name_en from positions where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    def getDepartment(self, company_id):
        self.db.connectDB()
        sql = f"""
        SELECT id, name_la FROM departments WHERE deleted_at IS NULL AND company_id = '{company_id}'
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []

    def getCompany(self):
        self.db.connectDB()
        sql = """
        select company_id, company_name from companies where deleted_at is null 
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)



    # def insertEmployeeData(self,name,lastname,address,phone,email,emp_code,gender):
    #     self.db.connectDB()
    #     sql = f"insert into employee values(null,'{name}','{lastname}','{address}','{phone}','{email}','{gender}'{emp_code}')"

    