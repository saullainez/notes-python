import mysql.connector

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
        

    def login(self):