from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dados mockados
clientes = [
    {"id": 1, "nome": "João", "email": "joao@email.com"},
    {"id": 2, "nome": "Maria", "email": "maria@email.com"},
    {"id": 3, "nome": "Carlos", "email": "carlos@email.com"}
]

funcionarios = [
    {"id": 1, "nome": "Ana", "cargo": "Gerente"},
    {"id": 2, "nome": "Pedro", "cargo": "Atendente"},
    {"id": 3, "nome": "Lucas", "cargo": "Caixa"}
]

@app.route('/api/clientes', methods=['GET'])
def get_clientes():
    return jsonify(clientes)

@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    return jsonify(funcionarios)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)