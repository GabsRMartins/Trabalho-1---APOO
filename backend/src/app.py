from flask import Flask, jsonify, request

app = Flask(__name__)

eventos = [
    {
        'id': 0,
        'endereço': "Amapa",
        'valor': 0
    }
]

@app.route('/eventos',methods=['GET'])
def obter_eventos():
    return jsonify(eventos)

@app.route('/eventos/<int:id>',methods=['GET'])
def obter_eventos_por_id(id):
    return eventos.id == id


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
