from config import app, db
from flask import request, jsonify
from app.routes.users import get_Users
from app.models.users import User



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    # Check if user already exists to avoid duplicates
        if not User.query.filter_by(user_name="john_doe").first():
            new_user = User(user_name="john_doe", password="123me")
            db.session.add(new_user)
            db.session.commit()
            print("User added!")
        else:
            print("User already exists.")


    app.run(debug=True)

