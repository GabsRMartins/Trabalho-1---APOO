import sqlite3
import os

class Base_Dados:
    def __init__(self):
        self.db_name = os.path.join(os.path.dirname(__file__), 'role_dia_db.db')
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Conexão com o banco '{self.db_name}' foi estabelecida com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def execute_script(self):
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'role_dia_db.sql')
            with open(script_path, 'r', encoding='utf-8') as file:
                script = file.read()
            cursor = self.connection.cursor()
            cursor.executescript(script)
            self.connection.commit()
            print("Script SQL executado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao executar o script SQL: {e}")

    def add_usuario(self, nome, email, senha, tipo_usuario):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuario (nome, email, senha, tipo_usuario) 
                VALUES (?, ?, ?, ?)
            """, (nome, email, senha, tipo_usuario))
            self.connection.commit()
            print("Usuário adicionado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")

    def add_evento(self, nome_evento, local_evento, organizadora, id_usuario):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO eventos (nome_evento, local_evento, organizadora, id_usuario) 
            VALUES (?, ?, ?, ?)
            """, (nome_evento, local_evento, organizadora, id_usuario))
            self.connection.commit()
            print("Evento adicionado com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao adicionar evento: {e}")

    def get_usuario(self, nome):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE nome = ?", (nome,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário por nome: {e}")
            return []
        
    def get_usuario_id(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE nome = ?", (id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário por id: {e}")
            return []    
        
    def get_senha(self, senha):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario WHERE senha = ?", (senha,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao obter credenciais: {e}")
            return []
        
    def cadastrar(self, username, email, password,  tipo):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
            INSERT INTO usuario (nome, email, senha, tipo_usuario)
            VALUES (?, ?, ?, ?)
            """, (username, email, password,  tipo))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Conexão com o banco encerrada.")

    def get_eventos(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM eventos ")
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao consultar eventos: {e}")
            return []