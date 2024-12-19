from Database.connect_database import ConnectDatabase

class DeviceHistoryController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectDeviceData(self):
        self.db.connectDB()
        sql = """select h.id, h.device_name,h.serial_number,s.status_name, h.created_at, dl.device_location_name ,h.device_created_date,h.created_by,h.used_by
        from histories h join status s on s.status_id = h.status_id 
        join device_locations dl on dl.device_location_id = h.address
        WHERE h.deleted_at IS NULL
        ORDER BY h.id desc"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()

    def addDeviceInfo(self, device_name,serial_number,status_id,device_location_id,created_by):
        self.db.connectDB()
        sql = f"""
           insert into histories(device_name,serial_number,status_id,created_at,
           address,device_created_date,created_by) 
           values('{device_name}','{serial_number}','{status_id}',Now(),'{device_location_id}'
           ,Now(),'{created_by}')
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

    def addDeviceManage(self, device_name,serial_number,status_id,device_location_id,used_by,created_by):
        self.db.connectDB()
        sql = f"""
           insert into histories(device_name,serial_number,status_id,created_at,
           address,used_by,created_by) 
           values('{device_name}','{serial_number}','{status_id}',Now(),'{device_location_id}'
           ,'{used_by}','{created_by}')
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

    def updateData(self, brand_id, status_id, device_id, device_model, serial_number, mac_address,
               supplier_id, user_id, category_id, device_location_id, used_by_id, remark,device_name):
        self.db.connectDB()
        sql = f"""
        update devices set brand_id ='{brand_id}',device_name='{device_name}',status_id='{status_id}',device_model='{device_model}',
        serial_number='{serial_number}',mac_address='{mac_address}',supplier_id='{supplier_id}',
        user_id='{user_id}',category_id='{category_id}',device_location_id='{device_location_id}',
        used_by='{used_by_id}',device_remark='{remark}' where device_id = '{device_id}' and deleted_at is null
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


    def deleteData(self,history_id):
            self.db.connectDB()
            sql = f"""
            update histories set deleted_at = NOW() where id = '{history_id}' and deleted_at is null
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

    

    
    def searchData(self,select_data):
        self.db.connectDB()
        sql=f"""
           select d.device_id,b.brand_name,d.device_name, d.device_model,d.serial_number,d.mac_address,s.status_name,
           sp.supplier_name,c.category_name,
           d.device_remark,dl.device_location_name, CONCAT(e.name,' ',e.surname)as used_by 
           from devices d 
           join brands b on b.brand_id = d.brand_id 
           join status s on s.status_id = d.status_id
           join suppliers sp on sp.supplier_id=d.supplier_id
           join categories c on c.category_id = d.category_id
           join device_locations dl on dl.device_location_id = d.device_location_id
           join employees e on e.emp_id = d.used_by where
           (b.brand_name like '%{select_data}%' or d.device_model  like '%{select_data}%' 
           or d.serial_number like'%{select_data}%' or d.mac_address like '%{select_data}%' 
           or s.status_name like '%{select_data}%' or supplier_name like'%{select_data}%' 
           or c.category_name like '%{select_data}%') and d.deleted_at is null OrDer by d.device_id
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            print("Search Data Of devices",result)
            return result
            
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return []
        finally:
            self.db.con.close()


    def afterSearch(self, search_data):
        self.db.connectDB()
        # sql = f"""
        # SELECT d.device_id, c.category_name,
        #     COUNT(*) AS total_devices,
        #     SUM(s.status_name = 'available') AS available_count,
        #     SUM(s.status_name = 'in use') AS in_use_count,
        #     SUM(s.status_name = 'under repair') AS under_repair_count,
        #     SUM(s.status_name = 'broken') AS broken_count
        # FROM devices d
        # JOIN categories c ON c.category_id = d.category_id
        # JOIN status s ON d.status_id = s.status_id
        # WHERE d.device_id = '{search_data}' 
        # AND c.category_name = '{search_data}'
        # AND d.deleted_at IS NULL
     
        # """
        sql = f"""
        SELECT c.category_name
        from categories c join devices d
        WHERE d.category_id = '{search_data}' 
        AND d.deleted_at IS NULL
     
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return []
        finally:
            self.db.con.close()
