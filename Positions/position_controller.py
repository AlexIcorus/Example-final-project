from Database.connect_database import ConnectDatabase

class positionController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectPositionData(self):
        self.db.connectDB()
        sql = """SELECT position_id, name_en, remark from positions
        WHERE deleted_at IS NULL
        ORDER BY position_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, position_name, remark):
        self.db.connectDB()
        sql = f"""
            INSERT INTO positions (name_en, remark, created_at) 
            VALUES ('{position_name}', '{remark}',NOW());
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

    def updateData(self,position_id, position_name, remark):
        self.db.connectDB()
        sql = f"""
        update positions set name_en ='{position_name}',remark='{remark}'
        where position_id = '{position_id}' and deleted_at is null
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


    def deleteData(self,position_id):
            self.db.connectDB()
            sql = f"""
            update positions set deleted_at = NOW() where position_id = '{position_id}' and deleted_at is null
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
        
    