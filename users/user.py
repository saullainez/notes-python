import mysql.connector
import datetime
import hashlib

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

        #Cifrar contraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (self.name, self.lastname, self.email, cifrado.hexdigest(), created_at)

        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result


    def login(self):
        return self