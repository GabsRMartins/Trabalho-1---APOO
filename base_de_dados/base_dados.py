import sqlite3

class Base_Dados:
    def __init__(self, db_name:str) -> None:
        #inicializa a conexão com o banco de dados
        self._db_name = db_name
        self.__connection = None
        self.connect()
        self.__cursor = self.__connection.cursor()
        self.executa_script()

    def connect(self) -> None:
        self.__connection = sqlite3.connect(self._db_name)

    def executa_script(self) -> None:
        #executa o arquivo .sql
        with open('base_de_dados/{}.sql'.format(self.db_name), 'r') as file:
            script = file.read()
        self.__cursor.executescript(script)
        self.__connection.commit()

    def add_usuario(self, nome, email, senha, tipo_usuario) -> None:
        self.__cursor.execute("""
            INSERT INTO usuario (nome, email, senha, tipo_usuario) 
            VALUES (?, ?, ?, ?)
        """, (nome, email, senha, tipo_usuario))
        self.__connection.commit()

    def add_evento(self, nome_evento, local_evento, organizadora, id_usuario) -> None:
        self.__cursor.execute("""
        INSERT INTO eventos (nome_evento, local_evento, organizadora, id_usuario) 
        VALUES (?, ?, ?, ?)
        """, (nome_evento, local_evento, organizadora, id_usuario))
        self.__connection.commit()

    def get_nome_usuario(self) -> str:
        self.__cursor.execute("SELECT nome FROM usuario ")
        return self.__cursor.fetchone()

    def get_nome_evento(self) -> str:
        self.__cursor.execute("SELECT nome_evento FROM eventos ")
        return self.__cursor.fetchone()

    def __del__(self) -> None: 
        #encerra a conexão com o banco de dados
        if self.__connection:
            self.__connection.close()

# db = Base_Dados('role_dia_db')
# print(type(db.get_nome_usuario()))
# print(db.get_nome_evento())
# # nome = db.get_nome_usuario

# # print(nome)