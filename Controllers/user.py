from App.models import User
from App.database import db

def create_student(studentID, password):
    newuser = User(studentID=studentID, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def create_staff(staffID, password):
    newuser = User(staffID=staffID, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_student_by_studentID(studentID):
    return User.query.filter_by(studentID=studentID).first()

def get_staff_by_stafftID(staffID):
    return User.query.filter_by(staffID=staffID).first()

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_student(studentID):
    student = get_student(studentID)
    if student:
        student.studentID = studentID
        db.session.add(student)

def update_staff(stafftID):
    staff = get_student(staffID)
    if staff:
        staff.staffID = staffID
        db.session.add(staff)
        return db.session.commit()
    return None
    
