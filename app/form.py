from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField,validators, TextAreaField
from wtforms.validators import InputRequired, DataRequired , Length

class Addmember(FlaskForm):
    position = StringField('Position', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    f_name = StringField('First Name', validators=[InputRequired()])
    l_name = StringField('Last Name', validators=[InputRequired()])
    m_name = StringField('Middle Name', validators=[InputRequired()])
    dob = StringField('Date of Birth', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('Male', 'Male'),('Female','Female')])
    address = StringField('Address',  validators=[DataRequired(),InputRequired(),Length(max=700)])
    phonenum = StringField('Phone Number', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired()])
    