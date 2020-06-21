import mysql.connector
import datetime

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="notes_py",
    port=3306
)

cursor = database.cursor(buffered=True)
class User:

    def __init__(self, name, lastname, email, password):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password
    
    def register(self):
        created_at = datetime.datetime.now()
        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.lastname, self.email, self.password, created_at)

        cursor.execute(sql, user)
        database.commit()

        return[cursor.rowcount, self]

    def login(self):
        return self