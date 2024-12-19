from Database.connect_database import ConnectDatabase

class DeviceController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectDeviceData(self):
        self.db.connectDB()
        sql = """SELECT d.device_id, b.brand_name,d.created_by ,d.device_name,d.device_model,d.serial_number, d.mac_address, s.status_name
        , category_name,d.device_remark,dl.device_location_name,us.username,IFNULL(concat(e.name,' ',e.surname),'No') as used_by
        from devices d join status s on s.status_id = d.status_id
        join brands b on b.brand_id = d.brand_id
       
        join categories c on c.category_id = d.category_id
        join device_locations dl on dl.device_location_id = d.device_location_id
        join users us on us.id = d.user_id
        join employees e on e.emp_id = d.used_by
    
        WHERE d.deleted_at IS NULL 
        ORDER BY d.device_id"""
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
    def getBrand(self):
        self.db.connectDB()
        sql="""
        select brand_id, brand_name from brands where deleted_at is null
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


    def getUser(self):
        self.db.connectDB()
        sql="""
        select id, username from users where deleted_at is null
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
        select device_model from devices where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    def getSerialNumber(self):
        self.db.connectDB()
        sql="""
        select serial_number from devices where deleted_at is null
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
    
    def getMacAddress(self):
        self.db.connectDB()
        sql="""
        select mac_address from devices where deleted_at is null
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

    def getCategory(self):
        self.db.connectDB()
        sql=f"""
        select category_id ,category_name from categories where deleted_at is null 
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    def add_info(self, brand_id, status_id, device_model,device_name,serial_number,mac_address,category_id,user_id,device_location_id,used_by_id,remark,created_by):
        self.db.connectDB()
        sql = f"""
            INSERT INTO devices (brand_id, device_name, status_id, device_model,serial_number,mac_address,category_id,user_id,device_location_id,created_by,used_by,device_remark,created_at) 
            VALUES ('{brand_id}','{device_name}', '{status_id}', '{device_model}','{serial_number}',
            '{mac_address}','{category_id}','{user_id}','{device_location_id}',
            '{created_by}','{used_by_id}','{remark}',NOW());
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
                user_id, category_id, device_location_id, used_by_id, remark,device_name):
        self.db.connectDB()
        sql = f"""
        update devices set brand_id ='{brand_id}',device_name='{device_name}',status_id='{status_id}',device_model='{device_model}',
        serial_number='{serial_number}',mac_address='{mac_address}',
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


    def deleteData(self,device_id):
            self.db.connectDB()
            sql = f"""
            update devices set deleted_at = NOW() where device_id = '{device_id}' and deleted_at is null
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
        
    def afterSearch(self,search_data):
        self.db.connectDB()
        sql = f"""
        SELECT brand_id, device_model, serial_number,mac_address,category,
        device_remark, device_location,used_by  FROM devices
        WHERE (brand_name LIKE '%{search_data}%' OR device_model LIKE '%{search_data}%'
        or serial_number like%{search_data}% or mac_address like%{search_data}% 
        or category like %{search_data}% or device_remark like%{search_data}%
        or device_location like%{search_data}% or used_by like%{search_data})
        AND deleted_at IS NULL order by device_id
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

    
    def searchData(self,select_data):
        self.db.connectDB()
        sql=f"""
           select d.device_id,b.brand_name,d.device_name, d.device_model,d.serial_number,d.mac_address,s.status_name,d.created_by,
           ,c.category_name,
           d.device_remark,dl.device_location_name, CONCAT(e.name,' ',e.surname)as used_by 
           from devices d 
           join brands b on b.brand_id = d.brand_id 
           join status s on s.status_id = d.status_id
          
           join categories c on c.category_id = d.category_id
           join device_locations dl on dl.device_location_id = d.device_location_id
           join employees e on e.emp_id = d.used_by where
           (b.brand_name like '%{select_data}%' or d.device_model  like '%{select_data}%' or d.device_name  like '%{select_data}%'
           or d.serial_number like'%{select_data}%' or d.mac_address like '%{select_data}%' or d.created_by like '%{select_data}%'
           or s.status_name like '%{select_data}%'  
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

    def updateUseby(self,used_by_id,device_id):
        self.db.connectDB()
        sql = f"""
            update devices set used_by ={used_by_id} where device_id = '{device_id}' and deleted_at is null
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

   
    def afterSearchDeviceName(self, search_data):
        self.db.connectDB()
        sql = f"""
        SELECT Device_name FROM Devices
        WHERE (device_name LIKE '%{search_data}%')
        AND deleted_at IS NULL order by device_id
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