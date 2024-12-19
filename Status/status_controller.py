from Database.connect_database import ConnectDatabase

class statusController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectStatusData(self):
        self.db.connectDB()
        sql = """SELECT status_id, status_name, remark from status
        WHERE deleted_at IS NULL
        ORDER BY status_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, status_name, remark):
        self.db.connectDB()
        sql = f"""
            INSERT INTO status (status_name, remark, created_at) 
            VALUES ('{status_name}', '{remark}',NOW());
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

    def updateData(self,status_id, status_name, remark):
        self.db.connectDB()
        sql = f"""
        update status set status_name ='{status_name}',remark='{remark}'
        where status_id = '{status_id}' and deleted_at is null
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


    def deleteData(self,status_id):
            self.db.connectDB()
            sql = f"""
            update status set deleted_at = NOW() where status_id = '{status_id}' and deleted_at is null
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
        
    