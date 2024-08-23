from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


# Hack 1: Endpoint que responde a solicitudes GET en /users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({'payload': 'success'})


# Hack 2: Endpoint que responde a solicitudes POST en /user
@app.route('/user', methods=['POST'])
def create_user():
    return jsonify({'payload': 'success'})


# Hack 3: Endpoint que responde a solicitudes DELETE en /user
@app.route('/user', methods=['DELETE'])
def delete_user():
    return jsonify({'payload': 'success'})


# Hack 4: Endpoint que responde a solicitudes PUT en /user
@app.route('/user', methods=['PUT'])
def update_user():
    return jsonify({'payload': 'success', 'error': False})


# Hack 5: Endpoint que responde a solicitudes GET en /api/v1/users
@app.route('/api/v1/users', methods=['GET'])
def get_api_users():
    return jsonify({'payload': []})


# Hack 6: Endpoint que responde a solicitudes POST en /api/v1/user
@app.route('/api/v1/user', methods=['POST'])
def post_api_user():
    # Extraer los parámetros de la solicitud
    email = request.args.get('email')
    name = request.args.get('name')
    # Crear la respuesta en formato JSON
    response = {
        'payload': {
            'email': email,
            'name': name
        }
    }
    return jsonify(response)


# Hack 7: Endpoint que responde a solicitudes POST en /api/v1/user/add
@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    # Extraer los valores del formulario utilizando request.form.get('key')
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    # Crear la respuesta en formato JSON
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    }
    return jsonify(response)


# Hack 8: Endpoint que responde a solicitudes POST en /api/v1/user/create
@app.route('/api/v1/user/create', methods=['POST'])
def create_user2():
    # Extraer los valores del JSON utilizando request.get_json()
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    # Crear la respuesta en formato JSON
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)