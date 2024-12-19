from Database.connect_database import ConnectDatabase
import bcrypt
class userController:
    def __init__(self):
        self.db = ConnectDatabase()
    
    def selectuserData(self):
        self.db.connectDB()
        sql = """SELECT id, username, name, password from users
        WHERE deleted_at IS NULL
        ORDER BY id"""
        try:
            
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
            return []
        finally:
            self.db.con.close()


    def add_info(self, username, name, password):
        self.db.connectDB()

        bytes = password.encode('utf-8') 
        
        # generating the salt 
        salt = bcrypt.gensalt() 
        
        # Hashing the password 
        password_hash = bcrypt.hashpw(bytes, salt) 
        
     
        sql = f"""
            INSERT INTO users ( username, name, password, created_at) 
            VALUES ('{username}', '{name}', '{password_hash.decode('utf-8')}',NOW());
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

    def updateData(self,user_id,username, name, password):
        self.db.connectDB()
        bytes = password.encode('utf-8') 
        
        # generating the salt 
        salt = bcrypt.gensalt() 
        
        # Hashing the password 
        password_hash = bcrypt.hashpw(bytes, salt) 
        
     
        sql = f"""
        update users set username ='{username}',name='{name}',password='{password_hash.decode('utf-8')}'
        where id = '{user_id}' and deleted_at is null
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


    def deleteData(self,user_id):
            self.db.connectDB()
            sql = f"""
            update users set deleted_at = NOW() where id = '{user_id}' and deleted_at is null
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
        
    