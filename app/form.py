from xmlrpc.client import DateTime
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField,IntegerField, SelectField, SubmitField,TextAreaField, PasswordField, BooleanField, RadioField, DateField
from wtforms.validators import InputRequired, DataRequired, Length,Email

class Addmember(FlaskForm):
    position = StringField('Position', validators=[InputRequired()])
    age = StringField('Age', validators=[InputRequired()])
    f_name = StringField('First Name', validators=[InputRequired()])
    l_name = StringField('Last Name', validators=[InputRequired()])
    m_name = StringField('Middle Name', validators=[InputRequired()])
    dob = DateField('Date of Birth', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('general','general'),('Male', 'Male'),('Female','Female')], validators=[DataRequired()])
    address = StringField('Address',  validators=[DataRequired(),InputRequired(),Length(max=700)])
    phonenum = StringField('Phone Number', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(),Email('Please enter a valid email adress')])
    
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
    dob = DateField('Date of Birth', validators=[InputRequired()])
    gender = SelectField('Gender', choices = [('general','general'),('Male', 'Male'),('Female','Female')], validators=[DataRequired()])
    address = StringField('Address',  validators=[DataRequired(),InputRequired(),Length(max=700)])
    phonenum = StringField('Phone Number', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(),Email('Please enter a valid email adress')])
    submit = SubmitField('Submit')
    Cancel = SubmitField('Cancel')

class DeleteForm(FlaskForm):
    submit = SubmitField('Submit')
    Cancel = SubmitField('Cancel')

class GenerateListForm(FlaskForm):
    NumberOfMembers = IntegerField('Attendee Amount')
    submit = SubmitField('Submit')

class CheckForm(FlaskForm):
    submit = SubmitField('Submit')

class Deleteattendance(FlaskForm):
    submit = SubmitField('Submit')
    Cancel = SubmitField('Cancel')

class searchArchiveForm(FlaskForm):
    Search = StringField('Search')
    Searchdate = DateField('Date Search Feild:')
    drop = SelectField('SearchBy', choices = [('f_name','f_name'),('l_name','l_name'),('general','general'),('Id','Id'), ('date','date')], validators=[InputRequired()])
    order = RadioField('Order', choices=[('Ac','Ac'),('Dc','Dc'),('None','None')])

