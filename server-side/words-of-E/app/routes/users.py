from app.models.users import User
from config import app
from flask import jsonify, request


@app.route('/users', methods=['GET'])
def get_Users():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_users})


@app.route('/users/<int:id>', methods=['GET'])
def get_User(id):
    individual_user = User.query.get(id)
    print(f'my_log:{individual_user}')
    if individual_user:
        return jsonify({"users": individual_user.to_json()})
    return jsonify({"error": "User not found"}), 404 


@app.route('/users/<int:id>', methods=['POST'])
def create_User():


#take script logic C, R, U, D, pass request object in python url params, request body
# @app.route('/users', methods=['POST'])
# @app.route('/users', methods=['DELETE'])
# @app.route('/users', methods=['PATCH'])