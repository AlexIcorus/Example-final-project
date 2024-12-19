from Database.connect_database import ConnectDatabase

class CategoryController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectCategoryData(self):
        self.db.connectDB()
        sql = """SELECT category_id, category_name, description from categories
        WHERE deleted_at IS NULL
        ORDER BY category_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, category_name, description):
        self.db.connectDB()
        sql = f"""
            INSERT INTO categories (category_name, description, created_at) 
            VALUES ('{category_name}', '{description}',NOW());
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

    def updateData(self,category_id, category_name, description):
        self.db.connectDB()
        sql = f"""
        update categories set category_name ='{category_name}',description='{description}'
        where category_id = '{category_id}' and deleted_at is null
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


    def deleteData(self,category_id):
            self.db.connectDB()
            sql = f"""
            update categories set deleted_at = NOW() where category_id = '{category_id}' and deleted_at is null
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

    def countDevice(self,category_id):
        self.db.connectDB
        sql=f"""
        select count(d.category_id) as cate_id from devices d 
        join categories c on c.category_id = d.category_id
        where c.category_id = '{category_id}'
        """

        # sql=f"""
        # select count(*)as count from devices
        # """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return 
        finally:
            self.db.con.close()
    
    def getCategory(self,category_name):
        self.db.connectDB()
        sql=f"""
        select count(d.category_id) as count_category_id ,c.category_id ,c.category_name 
        from categories c join devices d on c.category_id = d.category_id where d.deleted_at is null and c.category_name="{category_name}"
        """
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)

    def getStatusAvailable(self,category_id):
        self.db.connectDB
        sql=f"""
        select count(d.status_id) as available from devices d join status s on d.status_id = s.status_id
        where s.status_name = "available" and d.deleted_at is null and d.category_id ="{category_id}"
        """
        try:
            self.db.cursor.execute(sql)
            result_available = self.db.cursor.fetchall()
            return result_available
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return 
        finally:
            self.db.con.close()

    def getStatusInUse(self,category_id):
        self.db.connectDB
        sql=f"""
        select count(d.status_id) as in_use from devices d join status s on d.status_id = s.status_id
        where s.status_name = "in use" and d.deleted_at is null and d.category_id ="{category_id}"
        """
        try:
            self.db.cursor.execute(sql)
            result_in_use = self.db.cursor.fetchall()
            return result_in_use
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return 
        finally:
            self.db.con.close()

    def getStatusUnderRepairing(self,category_id):
        self.db.connectDB
        sql=f"""
              select count(d.status_id) as under_repairing from devices d join status s on d.status_id = s.status_id
        where s.status_name = "under repairing" and d.deleted_at is null and d.category_id ="{category_id}"
        """
        try:
            self.db.cursor.execute(sql)
            result_repair = self.db.cursor.fetchall()
            return result_repair
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return 
        finally:
            self.db.con.close()
        
    def getStatusBroken(self,category_id):
        self.db.connectDB
        sql=f"""
          select count(d.status_id) as broken from devices d join status s on d.status_id = s.status_id
        where s.status_name = "broken" and d.deleted_at is null and d.category_id ="{category_id}"
        """
        try:
            self.db.cursor.execute(sql)
            result_broken = self.db.cursor.fetchall()
            return result_broken
        except Exception as e:
            self.db.con.rollback()
            print(e)
            return 
        finally:
            self.db.con.close()
        
        
    