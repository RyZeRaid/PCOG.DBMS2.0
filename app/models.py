from . import db

class Member(db.Model):

    __tablename__ = 'members'

    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(100),nullable=False)
    f_name = db.Column(db.String(100),nullable=False)
    l_name = db.Column(db.String(100),nullable=False)
    m_name = db.Column(db.String(100),nullable=False)
    age = db.Column(db.String(6),nullable=False)
    gender = db.Column(db.String(20),nullable=False)
    phonenum = db.Column(db.String(80),nullable=False)
    dob = db.Column(db.String(20),nullable=False)
    email = db.Column(db.String(120),nullable=False)
    pri = db.Column(db.Integer,nullable=False)
    address = db.Column(db.String(800),nullable=False)


    def __init__(self, position ,f_name,l_name, m_name, age, gender,phonenum,dob,email,pri, address):
        self.position = position
        self.l_name = l_name
        self.f_name = f_name
        self.m_name = m_name
        self.age = age
        self.gender = gender
        self.phonenum = phonenum  
        self.dob = dob
        self.email = email
        self.pri = pri
        self.address = address

