from os import sep, mkdir
import sqlite3
from random import randint

class SQL:
    def __init__(self):

        try: mkdir("Dados")
        except: pass
        self.connection = sqlite3.connect("Dados" + sep + 'data.db')
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS usuarios(id INTERGER PRIMARY KEY, nome TEXT, cpf TEXT UNIQUE, telefone TEXT, email TEXT, regiao TEXT)")

    def connection_close(self):
        self.connection.close()

    def cadaster_user(self, data):
        self.cursor.execute("INSERT INTO usuarios VALUES(?, ?, ?, ?, ?, ?)", (randint(100000, 999999), data[0], data[1], data[2], data[3], data[4]))
        self.connection.commit()

    def get_user_regiao(self, data):
        return self.cursor.execute("SELECT * FROM usuarios WHERE regiao = ?", (data, )).fetchall()

    def get_users(self):
        return self.cursor.execute("SELECT * FROM usuarios").fetchall()
    
    def get_user_name(self, data):
        return self.cursor.execute("SELECT * FROM usuarios WHERE nome = ?", (data, )).fetchall()

    def get_user_cpf(self, data):
        return self.cursor.execute("SELECT * FROM usuarios WHERE cpf = ?", (data, )).fetchall()