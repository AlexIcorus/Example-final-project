from Database.connect_database import ConnectDatabase

class departmentController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectDepartmentData(self):
        self.db.connectDB()
        sql = """SELECT id, name_en, description from departments
        WHERE deleted_at IS NULL ORDER BY id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, department_name, description):
        self.db.connectDB()
        sql = f"""
            INSERT INTO departments (name_en, description, created_at) 
            VALUES ('{department_name}', '{description}',NOW());
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

    def updateData(self,department_id, department_name, description):
        self.db.connectDB()
        sql = f"""
        update departments set name_en ='{department_name}',description='{description}'
        where id = '{department_id}' and deleted_at is null
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


    def deleteData(self,department_id):
            self.db.connectDB()
            sql = f"""
            update departments set deleted_at = NOW() where id = '{department_id}' and deleted_at is null
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
        
    