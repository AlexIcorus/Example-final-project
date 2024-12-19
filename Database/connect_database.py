import mysql.connector


class ConnectDatabase:
    def __init__(self):
        self._host = "localhost"
        self._port = 3306
        self._user = "root"
        self._password = ""
        self._database = "exim_device"
        self.con = None
        self.cursor = None

    def connectDB(self):
        # Establish a database connection
        self.con = mysql.connector.connect(
            host=self._host,
            port=self._port,
            database=self._database,
            user=self._user,
            password=self._password
        )

        # Create a cursor for executing SQL queries
        self.cursor = self.con.cursor(dictionary=True)

