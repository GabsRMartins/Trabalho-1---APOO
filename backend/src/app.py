from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token, get_jwt


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from base_de_dados.base_dados import Base_Dados
from service.LoginService import LoginService
from service.UsuarioService import UsuarioService
from service.EventoService import EventoService
from entity.Evento import Evento

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "ACSACASSA"
app.config["JWT_BLACKLIST_ENABLED"] = True
app.config["JWT_BLACKLIST_TOKEN_CHECKS"] = ["access"]

jwt = JWTManager(app)


@app.route('/')
def home():
    return "API rodando!"




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
        access_token = create_access_token(identity=username)
        return jsonify({'access_token': access_token}), 200
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
    if (cadastro == True):
        return jsonify({'message': 'Cadastro efetuado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao realizar cadastro'}), 400


blacklist = set()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in blacklist


@app.route('/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]  # JWT ID único do token
    blacklist.add(jti)
    return jsonify({"msg": "Logout realizado com sucesso"}), 200

@app.route('/usuario/usuarioLogado', methods=['GET'])
@jwt_required()
def usuario_logado():
    db = Base_Dados()
    db.connect()
    usuario_id = get_jwt_identity()
    usuario_service = UsuarioService(None)
    usuario = usuario_service.buscarUsuarioId(usuario_id,db)
    if usuario:
        
        usuario_service.usuario = usuario
        nome = usuario_service.getNome()
        email = usuario_service.getEmail()

        return jsonify({
            "nome": nome,
            "email": email,
            "tipo":usuario.idTipo
        })
    else:
        return jsonify({"error": "Usuário não encontrado"}), 404





@app.route('/eventos',methods=['GET'])
def pegarEventos():
    db = Base_Dados()
    db.connect()
    evento_service = EventoService(None)
    eventos = evento_service.obterEventos(db)
    eventos_dict = [evento.to_dict() for evento in eventos]
    return jsonify(eventos_dict)                                     

@app.route('/eventos/<string:nome>', methods=['GET'])
@jwt_required()
def obter_evento_nome(nome):
    db = Base_Dados()
    db.connect()
    evento_service = EventoService(None)
    
    eventos = evento_service.obterEventosNome(db, nome)
    eventos_dict = [evento.to_dict() for evento in eventos]
    
    return jsonify(eventos_dict)   



@app.route('/eventos',methods=['POST'])
@jwt_required()
def cadastrarEvento():
    data = request.get_json()  
    nome = data.get('nome')
    horario = data.get('horario')
    local = data.get('local')
    preco = data.get('preco')
    organizadora = data.get('organizadora')
    usuario = data.get('usuario_id')
    if not nome or not horario or not local or not preco or not organizadora:
        return jsonify({'error': 'Todos os campos são obrigatórios'}), 400
    db = Base_Dados()
    db.connect()
    evento_service = EventoService(None)
    cadastro = evento_service.cadastraEvento(nome,local,horario,organizadora,preco,usuario,db)
    db.close()
    if (cadastro == True):
        return jsonify({'message': 'Cadastro efetuado com sucesso'}), 200
    else:
        return jsonify({'error': 'Erro ao realizar cadastro'}), 400


if __name__ == '__main__':
    db = Base_Dados()
    db.connect()
    db.execute_script()  # Executa role_dia_db.sql
    db.close()
    app.run(port=8000, host='localhost', debug=True)
