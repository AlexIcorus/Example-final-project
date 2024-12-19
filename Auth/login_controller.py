import bcrypt
from Database.connect_database import ConnectDatabase


class LoginController:
    def __init__(self):
        self.db = ConnectDatabase()


    def selectData(self,username):

        self.db.connectDB()
        sql = f"select name,username, password from users where username = '{username}' "
        try:
            self.db.cursor.execute(sql)
            result = self.db.cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            self.db.con.close()


   
       



