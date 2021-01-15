import sqlite3

class Db():
    def __init__(self):
        self.conn = sqlite3.connect('phone.db')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS phonebook (fname TEXT, lname TEXT, mobno TEXT)")
        self.conn.commit()

    def insert(self, fname, lname, mob):
        self.cur.execute("INSERT INTO phonebook VALUES (?,?,?)", (fname, lname, mob))
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM phonebook")
        rows = self.cur.fetchall()
        return rows

    def search(self,str):
        self.cur.execute(f"SELECT * FROM phonebook WHERE fname like '%{str}%'")
        ser = self.cur.fetchall()
        return ser

    def __del__(self):
        self.conn.close()