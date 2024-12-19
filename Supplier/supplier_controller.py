from Database.connect_database import ConnectDatabase

class supplierController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectSupplierData(self):
        self.db.connectDB()
        sql = """SELECT supplier_id, supplier_name, address, phone, fax, email, description from suppliers
        WHERE deleted_at IS NULL
        ORDER BY supplier_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, supplier_name, address,phone,fax,email, description):
        self.db.connectDB()
        sql = f"""
            INSERT INTO suppliers (supplier_name, address,phone,fax,email, description, created_at) 
            VALUES ('{supplier_name}', '{address}', '{phone}', '{fax}', '{email}', '{description}',NOW());
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

    def updateData(self,supplier_id, supplier_name, address,phone,fax,email, description):
        self.db.connectDB()
        sql = f"""
        update suppliers set supplier_name ='{supplier_name}',address='{address}',phone='{phone}',fax='{fax}'
        ,email='{email}',description='{description}'
        where supplier_id = '{supplier_id}' and deleted_at is null
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


    def deleteData(self,supplier_id):
            self.db.connectDB()
            sql = f"""
            update suppliers set deleted_at = NOW() where supplier_id = '{supplier_id}' and deleted_at is null
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
        
    