from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash

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
    dob = db.Column(db.DateTime,nullable=False)
    email = db.Column(db.String(120),nullable=False)
    pri = db.Column(db.Integer,nullable=False)
    address = db.Column(db.String(800),nullable=False)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)


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


class UserProfile(db.Model):
   
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))

    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.username