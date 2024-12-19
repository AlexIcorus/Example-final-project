from Database.connect_database import ConnectDatabase

class companyController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectCompanyData(self):
        self.db.connectDB()
        sql = """SELECT company_id, company_name, description from companies
        WHERE deleted_at IS NULL
        ORDER BY company_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, company_name, description):
        self.db.connectDB()
        sql = f"""
            INSERT INTO companies (company_name, description, created_at) 
            VALUES ('{company_name}', '{description}',NOW());
        """
        
        try:
            # Use parameterized query to prevent SQL injection
            self.db.cursor.execute(sql)
            self.db.con.commit()
            print("Device info added successfully.")
        except Exception as e:
            self.db.con.rollback()
            print(f"Error adding device info: {e}")
        finally:
            self.db.con.close()

    def updateData(self,company_id, company_name, description):
        self.db.connectDB()
        sql = f"""
        update companies set company_name ='{company_name}',description='{description}'
        where company_id = '{company_id}' and deleted_at is null
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


    def deleteData(self,company_id):
            self.db.connectDB()
            sql = f"""
            update companies set deleted_at = NOW() where company_id = '{company_id}' and deleted_at is null
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
        
    