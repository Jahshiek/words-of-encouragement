from config import app, db
from flask import request, jsonify
from app.routes.users import get_Users
from app.models.users import User
# from app.models.messages import Messages
from sqlalchemy import inspect



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created:")
        # Correct way to list tables in recent SQLAlchemy versions
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(tables)

    # Check if user already exists to avoid duplicates
        if not User.query.filter_by(user_name="john_doe").first():
            new_user = User(user_name="john_doe", password="123me")
            db.session.add(new_user)
            db.session.commit()
            print("User added!")
        else:
            print("User already exists.")


    app.run(debug=True)

