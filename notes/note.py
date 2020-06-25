import users.connection as con

connect = con.connect()
database = connect[0]
cursor = connect[1]

class Note:

    def __init__(self, user_id, title = "", desc = ""):
        self.user_id = user_id
        self.title = title
        self.desc = desc

    def save(self):
        sql = "INSERT INTO notes VALUES(null, %s, %s, %s, NOW())"
        note = (self.user_id, self.title, self.desc)

        cursor.execute(sql, note)
        database.commit()

        return [cursor.rowcount, self]

    def show(self):
        sql = f"SELECT * FROM notes WHERE user_id = {self.user_id}"

        cursor.execute(sql)
        result = cursor.fetchall()

        return result