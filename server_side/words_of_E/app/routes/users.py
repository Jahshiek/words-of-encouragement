from app.models.users import User
from config import app, db
from flask import jsonify, request

# returns a list of users
@app.route('/users', methods=['GET'])
def get_Users():
    users = User.query.all()
    json_users = list(map(lambda x: x.to_json(), users))
    return jsonify({"users": json_users})


#find user by id
@app.route('/users/<int:id>', methods=['GET'])
def get_User_By_Id(id):
    individual_user = User.query.get(id)
    print(f'my_log:{individual_user}')
    if individual_user:
        return jsonify({"users": individual_user.to_json()})
    return jsonify({"error": "User not found"}), 404 

#find user by username
@app.route('/users?username=<user_name>', methods=['GET'])
def get_User_By_Name(user_name):
    user = User.query.filter_by(user_name=user_name).first()
    print(f'my_log:{user}')
    if user:
        return jsonify({"users": user.to_json()})
    return jsonify({"error": "User not found"}), 404 

####################################################
#create user
@app.route('/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    password =  data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400
    
    new_user = User(username=username)
    new_user.set_password(password)

    existing_user = user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already taken'}), 409

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'user': new_user.to_json()}), 201
####################################################


# @app.route('/users/login', methods=['GET'])
# def update_user():
#     pass
####################################################

#updating user
@app.route('/users/<int:id>', methods=['PATCH']) #
def update_user():
    user = User.query.get(id)
    
    data = request.get_json()
    new_username = data.get('username')

    if new_username:
        user.username = new_username
    db.session.commit()
    return jsonify({"message": "User Updated successfully"}), 201
####################################################



#deleting user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user():
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not Found"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted successfully"}), 201
####################################################

# @app.route('/users/delete', methods=['DELETE'])

####################################################


