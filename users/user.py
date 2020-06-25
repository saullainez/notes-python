import datetime
import hashlib
import users.connection as con

connect = con.connect()
database = connect[0]
cursor = connect[1]


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