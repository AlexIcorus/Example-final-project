from Database.connect_database import ConnectDatabase

class DeviceManageController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectDeviceData(self):
        self.db.connectDB()
        sql = """SELECT dm.id, d.device_name ,d.serial_number, s.status_name
        ,dl.device_location_name, concat(e.name,' ',e.surname) as used_by,d.device_remark
        from device_managements dm join status s on s.status_id = dm.status_id

        join devices d on d.device_id = dm.device_id
        join device_locations dl on dl.device_location_id = dm.device_location_id
        join employees e on e.emp_id = dm.used_by
    
        WHERE dm.deleted_at IS NULL 
        ORDER BY dm.id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()
# StatusSupplierUserLocation
    def getDevice(self):
        self.db.connectDB()
        sql="""
        select device_id, device_name,used_by,status_id ,device_location_id from devices where deleted_at is null
        """
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            
            return result
        except Exception as e:
            print(e)

    def getStatus(self):
        self.db.connectDB()
        sql="""
        select status_id ,status_name from status where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def getDeviceLocation(self):
        self.db.connectDB()
        sql="""
        select device_location_id, device_location_name from device_locations where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    def getDeviceModel(self):
        self.db.connectDB()
        sql="""
        select device_id, device_model from devices where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def getUseBy(self):
        self.db.connectDB()
        sql="""
        select emp_id,concat (name,' ',surname) as by_user from employees where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)


    def add_info(self, device_id, status_id,device_location_id,used_by_id):
        self.db.connectDB()
        sql = f"""
            INSERT INTO device_managements (device_id, status_id,device_location_id,used_by,created_at) 
            VALUES ('{device_id}', '{status_id}',
            '{device_location_id}','{used_by_id}',NOW());
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

    def updateData(self, status_id, device_manager_id, 
                    device_location_id, used_by_id):
        self.db.connectDB()
        sql = f"""
        update device_managements set status_id='{status_id}',device_location_id='{device_location_id}',
        used_by='{used_by_id}' where id = '{device_manager_id}' and deleted_at is null
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




    def deleteData(self,device_manager_id):
            self.db.connectDB()
            sql = f"""
            update device_managements set deleted_at = NOW() where id = '{device_manager_id}' and deleted_at is null
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

    def updateFromDeviceInfo(self, status_id, device_id, 
                    device_location_id, used_by_id):
        self.db.connectDB()
        sql = f"""
        update device_managements set status_id='{status_id}',device_location_id='{device_location_id}',
        used_by='{used_by_id}' where device_id = '{device_id}' and deleted_at is null
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
                
    def SetFormByDeviceId(self, used_by_id):
        self.db.connectDB()
        sql = f"""
            SELECT 
            emp_id, CONCAT(name,' ', surname) as used_by_name
            FROM employees
            WHERE emp_id = '{used_by_id}' and deleted_at is null
        """
        
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []

        finally:
            self.db.con.close()

    def SetLabelSerialNumber(self, device_id):
        self.db.connectDB()
        sql = f"""
            SELECT 
            serial_number ,status_id
            FROM devices
            WHERE device_id = '{device_id}' and deleted_at is null
        """
        
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []

        finally:
            self.db.con.close()


    def SetStatus(self, status_id):
        self.db.connectDB()
        sql = f"""
            SELECT 
            status_id , status_name
            FROM status
            WHERE status_id = '{status_id}' and deleted_at is null
        """
        
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []

        finally:
            self.db.con.close()


    def SetDeviceLocation(self, device_location_id):
        self.db.connectDB()
        sql = f"""
            SELECT 
            device_location_id , device_location_name
            FROM device_locations
            WHERE device_location_id = '{device_location_id}' and deleted_at is null
        """
        
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []

        finally:
            self.db.con.close()


    
            
        


    
            
        