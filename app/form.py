from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField, SubmitField, TextAreaField, PasswordField, BooleanField, RadioField
from wtforms.validators import InputRequired, DataRequired, Length

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
    
class searchForm(FlaskForm):
    Search = StringField('Search')
    drop = SelectField('SearchBy', choices = [('Male', 'Male'),('Female','Female'),('f_name','f_name'),('l_name','l_name'),('m_name','m_name'),('Age','Age'),('general','general'),('Id','Id')], validators=[InputRequired()])
    order = RadioField('Order', choices=[('Ac','Ac'),('Dc','Dc'),('None','None')])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    remember_me = BooleanField('Remember me')

class UpdateForm(FlaskForm):
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
    submit = SubmitField('Submit')
    Cancel = SubmitField('Cancel')

class DeleteForm(FlaskForm):
    submit = SubmitField('Submit')
    Cancel = SubmitField('Cancel')