from Database.connect_database import ConnectDatabase

class BrandController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectBrandData(self):
        self.db.connectDB()
        sql = """SELECT brand_id, brand_name, description from brands
        WHERE deleted_at IS NULL
        ORDER BY brand_id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, brand_name, description):
        self.db.connectDB()
        print(brand_name)
        sql = f"""
            INSERT INTO brands (brand_name, description, created_at) 
            VALUES ('{brand_name}', '{description}',NOW());
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

    def updateData(self,brand_id, brand_name, description):
        self.db.connectDB()
        sql = f"""
        update brands set brand_name ='{brand_name}',description='{description}'
        where brand_id = '{brand_id}' and deleted_at is null
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


    def deleteData(self,brand_id):
            self.db.connectDB()
            sql = f"""
            update brands set deleted_at = NOW() where brand_id = '{brand_id}' and deleted_at is null
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
        
    