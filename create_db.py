from app import app, db
from models import Student, Major
import datetime as dt

with app.app_context():
    # rebuild all tables each time this script runs
    db.drop_all()
    db.create_all()
    # initial loading of majors (same as prof bono)
    majors = [
        'Aerospace Engineering', 'Biology', 'Civil Engineering', 'Computer Science',
        'Electrical Engineering', 'Finance', 'Information Systems', 'Marketing',
        'Mechanical Engineering'
    ]

    for each_major in majors:
        print(each_major)
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()
    # initial loading of students
    # added email field to each student because email is now required (nullable = False)
    students = [
        {
            'student_id': '1',
            'first_name': 'Robert',
            'last_name': 'Smith',
            'email': 'rsmith@example.edu',  # added email
            'major_id': 3,
            'birth_date': dt.datetime(2005, 6, 1),
            'is_honors': 1
        },
        {
            'student_id': '2',
            'first_name': 'Leo',
            'last_name': 'Van Munching',
            'email': 'lvanmunching@example.edu',  # added email
            'major_id': 6,
            'birth_date': dt.datetime(2004, 3, 24),
            'is_honors': 0
        },
    ]

    for each_student in students:
        print(f'{each_student["first_name"]} {each_student["last_name"]} inserted into Student')
        # create Student object
        # now passing email to match the updated __init__ in models.Student
        a_student = Student(
            first_name=each_student["first_name"],
            last_name=each_student["last_name"],
            email=each_student["email"],  # pass email into Student()
            major_id=each_student["major_id"],
            birth_date=each_student["birth_date"],
            is_honors=each_student["is_honors"]
        )
        db.session.add(a_student)
        db.session.commit()
