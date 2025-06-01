import sqlite3
import os

class Base_Dados:
    def __init__(self)-> None:
        self.db_name = os.path.join(os.path.dirname(__file__), 'role_dia_db.db')
        self.connection = None

    def connect(self) -> None:
        try:
            self.connection = sqlite3.connect(self.db_name)
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def execute_script(self)-> None:
        try:
            script_path = os.path.join(os.path.dirname(__file__), 'role_dia_db.sql')
            with open(script_path, 'r', encoding='utf-8') as file:
                script = file.read()
            cursor = self.connection.cursor()
            cursor.executescript(script)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao executar o script SQL: {e}")

    def add_usuario(self, nome, email, senha, tipo_usuario)-> str:
        cursor =  self.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO usuario (nome, email, senha, tipo_usuario) 
                VALUES (?, ?, ?, ?)
            """, (nome, email, senha, tipo_usuario))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao adicionar usuário: {e}")

    def add_evento(self, nome_evento:str, local_evento:str, organizadora:str, id_usuario:str)-> str:
        cursor =  self.connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO eventos (nome_evento, local_evento, organizadora, id_usuario) 
            VALUES (?, ?, ?, ?)
            """, (nome_evento, local_evento, organizadora, id_usuario))
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Erro ao adicionar evento: {e}")

    def get_usuario(self, nome):
        cursor =  self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM usuario WHERE nome = ?", (nome,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário por nome: {e}")
            return []

    def get_usuario_id(self, id):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM usuario WHERE nome = ?", (id,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário por id: {e}")
            return []

    def get_senha(self, senha)->str:
        cursor =  self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM usuario WHERE senha = ?", (senha,))
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Erro ao obter credenciais: {e}")
            return []
            
    def cadastrar(self, username, email, password,  tipo)-> bool:
        cursor =  self.connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO usuario (nome, email, senha, tipo_usuario)
            VALUES (?, ?, ?, ?)
            """, (username, email, password,  tipo))
            self.connection.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao cadastrar usuário: {e}")
            return False

    def close(self)-> None:
        if self.connection:
            self.connection.close()
            print("Conexão com o banco encerrada.")

    def get_eventos(self):
        cursor =  self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM eventos ")

            eventos = cursor.fetchall()
            # Adiciona o print para debug
            print("\nResultado da consulta de eventos:")
            for evento in eventos:
                print(evento)
            print(f"Total de eventos encontrados: {len(eventos)}\n")    

            return eventos
        except sqlite3.Error as e:
            print(f"Erro ao consultar eventos: {e}")
            return []