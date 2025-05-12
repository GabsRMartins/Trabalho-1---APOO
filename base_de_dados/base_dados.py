import sqlite3

class Base_Dados:
    def __init__(self):#inicializa a conexão com o banco de dados
        self.db_name = 'role_dia_db'
        self.connection = None

    def connect(self):#estabelece a conexão com o banco de dados
        try:
            self.connection = sqlite3.connect(self.db_name)
            print(f"Conexão com o banco '{self.db_name}' foi estabelecida com sucesso.")
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco: {e}")

    def execute_script(self):#executa o arquivo .sql
        try:
            with open('base_de_dados/role_dia_db.sql', 'r') as file:
                script = file.read()
            cursor = self.connection.cursor()
            cursor.executescript(script)
            self.connection.commit()
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
        except mysql.connector.Error as e:
            print(f"Erro ao adicionar usuário: {e}")

    def add_evento(self, nome_evento, local_evento, organizadora, id_usuario):
        cursor = self.connection.cursor()
        try:
            cursor.execute("""
            INSERT INTO eventos (nome_evento, local_evento, organizadora, id_usuario) 
            VALUES (?, ?, ?, ?)
            """, (nome_evento, local_evento, organizadora, id_usuario))
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Erro ao adicionar evento: {e}")

    def get_usuario(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM usuario ")
            return cursor.fetchone()
        except sqlite3.Error as e:
            print(f"Erro ao buscar usuário com ID {user_id}: {e}")
            return None

    def close(self): #encerra a conexão com o banco de dados
        if self.connection:
            self.connection.close()

# # Exemplo de uso
# db_manager = Base_Dados()
# db_manager.connect()
# db_manager.execute_script()
# # db_manager.add_evento(
# #     nome_evento='Workshop de Tecnologia',
# #     local_evento='Auditório da UFMG',
# #     organizadora='Elaine Santos',
# #     id_usuario=1  # Certifique-se de que o usuário com ID 1 existe
# # )
# db_manager.add_usuario('Carlos', 'carlos123@example.com', 'senha_segura123', 1)
# db_manager.close()
