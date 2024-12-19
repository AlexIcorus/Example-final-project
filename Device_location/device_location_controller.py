from Database.connect_database import ConnectDatabase

class deviceLocationController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectDeviceLocationData(self):
        self.db.connectDB()
        sql = """SELECT device_location_id, device_location_name,address, description from device_locations
        WHERE deleted_at IS NULL
        ORDER BY device_location_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, device_location_name, description,address):
        self.db.connectDB()
        sql = f"""
            INSERT INTO device_locations (device_location_name,address, description, created_at) 
            VALUES ('{device_location_name}', '{address}','{description}',NOW());
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

    def updateData(self,device_location_id, device_location_name, description,address):
        self.db.connectDB()
        sql = f"""
        update device_locations set device_location_name ='{device_location_name}',description='{description}',address ='{address}'
        where device_location_id = '{device_location_id}' and deleted_at is null
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


    def deleteData(self,device_location_id):
            self.db.connectDB()
            sql = f"""
            update device_locations set deleted_at = NOW() where device_location_id = '{device_location_id}' and deleted_at is null
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
        
    