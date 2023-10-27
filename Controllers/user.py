from App.models import User
from App.database import db

def create_user(userID, password):
    newuser = User(userID=userID, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_userID(userID):
    return User.query.filter_by(userID=userID).first()

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(userID):
    user = get_user(userID)
    if user:
        user.userID = userID
        db.session.add(user)
        return db.session.commit()
    return None
    
