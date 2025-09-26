import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

class MySQLConnection:
    def __init__(self):
        self._username = os.getenv('USERNAME')
        self._password = os.getenv('PASSWORD')
        self._host = os.getenv('HOST')
        self._database = os.getenv('DATABASE')
        self.conn = self._connect()

    def _connect(self):
        return mysql.connector.connect(
            host = self._host, 
            user = self._username,
            password = self._password,
            database = self._database
            )
    
    def _close(self):
        if self.conn.is_connected():
            self.conn.close()

    def _query(self, query: str):
        if (not self.conn.is_connected()) or self.conn is None:
            self.conn = self._connect()

        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()

        return result