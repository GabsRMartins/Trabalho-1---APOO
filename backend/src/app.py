from flask import Flask, jsonify, request

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from base_de_dados.base_dados import Base_Dados
from service.LoginService import LoginService

app = Flask(__name__)



@app.route('/')
def home():
    return "API rodando!"

@app.route('/eventos',methods=['GET'])
def obter_eventos():
    return jsonify(eventos)

@app.route('/eventos/<int:id>',methods=['GET'])
def obter_eventos_por_id(id):
    return eventos.id == id

from flask import request, jsonify

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Usuário e senha são obrigatórios'}), 400

    db = Base_Dados()
    db.connect()
    login_service = LoginService(db)

    autenticado = login_service.autenticar(username, password)
    db.close()

    if autenticado:
        return jsonify({'message': 'Login efetuado com sucesso'}), 200
    else:
        return jsonify({'error': 'Usuário ou senha inválidos'}), 401

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()  
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    tipo = data.get('tipo')
    if not username or not password or not email or not tipo:
        return jsonify({'error': 'Dados Incompletos'}), 400

    db = Base_Dados()
    db.connect()
    login_service = LoginService(db)
    cadastro = login_service.cadastrar(username,email,password,tipo)
    db.close()
    if cadastro:
        return jsonify({'message': 'Cadastro efetuado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao realizar cadastro'}), 401





if __name__ == '__main__':
    db = Base_Dados()
    db.connect()
    db.execute_script()  # Executa role_dia_db.sql
    db.close()
    app.run(port=5000, host='localhost', debug=True)
