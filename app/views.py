"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
from operator import length_hint
import os
from sre_constants import SUCCESS
from app import app, db,login_manager
from flask import render_template, request, redirect, url_for,flash,send_from_directory
from flask_login import login_user, logout_user, current_user, login_required
from .models import Member,UserProfile
from .form import Addmember, searchForm, LoginForm, DeleteForm, UpdateForm
from sqlalchemy import desc
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash
from datetime import date

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name=" ___")

@app.route("/Member/Addmember",methods=["POST", "GET"])
@login_required
def addmember():
    myform = Addmember()

    if request.method == 'GET':
        return render_template('Addmember.html',form=myform )
    
    if request.method == 'POST'and myform.validate_on_submit():
        
        position = myform.position.data
        l_name = myform.l_name.data
        f_name = myform.f_name.data
        m_name = myform.m_name.data
        age = myform.age.data
        gender = myform.gender.data
        phonenum = myform.phonenum.data 
        dob = myform.dob.data
        email = myform.email.data
        address = myform.address.data
        pri = 0
       
        member = Member(position = position, l_name = l_name, f_name = f_name,
                        m_name = m_name, age = age, gender = gender,
                        phonenum = phonenum , dob = dob, email = email,
                        address = address, pri = pri) 
        
        db.session.add(member)
        db.session.commit()

        flash('Successfully added a new property','success')
        return redirect(url_for('home'))

    flash_errors(myform)
    return render_template('Addmember.html', form = myform)


@app.route('/view/members')
@login_required
def showmember():
    myform = searchForm()  
    if get_member_info() != []:
        return render_template('Viewmember.html', form = myform, member = get_member_info() )
    else: 
        flash("database is empty no members to show", 'danger')
        return render_template('Viewmember.html', form = myform, member = get_member_info() )


@app.route('/search/members',methods=["POST", "GET"])
@login_required
def searchmember():
    myform = searchForm()
    
    info = Member.query
    if request.method == 'GET':
        
        return render_template('Viewmember.html',form=myform )
    
    if request.method == 'POST'and myform.validate_on_submit():
        #Getting data from the search form
        Search = myform.Search.data
        drop = myform.drop.data
        order = myform.order.data
        print("this is drop ",drop)
        if drop == "general" :
            flash("Please select what you would like to search by", 'danger')
            info =  info.order_by(Member.f_name ).all()
        
        print("this is what was searched",Search,drop, order)
        #Query the database by what to search by 
        
        #First Name
        message= "There are no members currently with the first name "+ Search + "."
        if drop == "f_name" and order == "Ac":
            if Search == "":
                print("search feild was empty")
                info = info.order_by(Member.f_name).all()
            else:
                info = info.filter(Member.f_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        elif drop == "f_name" and order =="Dc":
            if Search == "":
                print("search feild was empty")
                info = info.order_by(desc(Member.f_name)).all()
            else:
                info = info.filter(Member.f_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        elif drop == "f_name":
            print("first name",drop)
            info = info.filter(Member.f_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        
        # Last name
        message = "There are no members currently with the Last Name "+ Search + "."
        if drop =="l_name" and order =="Ac":
            if Search == "" :
                info = info.order_by(Member.l_name).all()
            else:
                info = info.filter(Member.l_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        elif drop == "l_name" and order =="Dc":
            if Search == "":
                print("search feild was empty")
                info = info.order_by(desc(Member.l_name)).all()
            else:
                info = info.filter(Member.l_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        elif drop == "l_name":
            print("last name",drop)
            info = info.filter(Member.l_name.like('%'+ Search +'%')).all()
        if info == []:
                flash(message,'danger')    

        #Middle Name
        message = "There are no members currently with the Middle Name "+ Search + "."
        if drop == "m_name" and order =="Ac":
            if Search == "":
                print("search feild was empty")
                info = info.order_by(Member.m_name).all()
            else:
                info = info.filter(Member.m_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        elif drop == "m_name" and order =="Dc":
            if Search == "":
                print("search feild was empty")
                info = info.order_by(desc(Member.m_name)).all()
            else:
                info = info.filter(Member.m_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        elif drop == "m_name":
            print("middle name",drop)
            info = info.filter(Member.m_name.like('%'+ Search +'%')).all()
            if info == []:
                flash(message,'danger')
        
        #Genders Male
        message = "There are no members currently of the gender"+ drop + "."
        if drop == "Male":
            info = info.filter_by(gender=drop).all()
            if info == []:
                flash(message,'danger')
        #genders Female
        message = "There are no members currently of the gender "+ drop + "."
        if drop == "Female":
            info = info.filter_by(gender=drop).all()
            if info == []:
                flash(message,'danger')
        #Age
        message = "There are no members currently of the age "+ Search + "."
        if drop == "Age":
            if Search == "":
                info = info.order_by(Member.age).all()
            else:
                info = info.filter_by(age = Search).all()
            if info == []:
                flash(message,'danger')    
        # ID Number
        message = "There are no members currently with the ID Number "+ Search + "."
        if drop == "Id" and order =="Ac":
            if Search == "":
                info = info.order_by(Member.id).all()
            else:
                info = info.filter_by( id = Search ).all()
            if info == []:
                flash(message,'danger')
        elif drop == "Id" and order =="Dc":
            if Search == "":
               
                info = info.order_by(desc(Member.id)).all()
            else:
                info = info.filter_by( id = Search ).all()
            if info == []:
                flash(message,'danger')
        elif drop == "Id":
            
            info = info.filter_by( id = Search ).all()
            if info == []:
                flash(message,'danger')       
            
        return render_template('Searchmember.html',form=myform , Search = Search,drop = drop, member = info, order= order )


@app.route('/update/members/<int:id>',methods=["POST", "GET"])
@login_required
def updatemember(id):
    form = UpdateForm()
    info = Member.query.get_or_404(id)
    
    if form.Cancel.data:
        flash('Did not Update member.', 'success')
        return render_template('Viewmember.html', form = searchForm() , member = get_member_info())
    
    if request.method == "POST" and form.validate_on_submit(): 
        
        info.position = request.form['position']
        info.l_name = request.form['l_name']
        info.f_name = request.form['f_name']
        info.m_name = request.form['m_name']
        info.age = request.form['age']
        info.gender = request.form['gender']
        info.phonenum = request.form['phonenum'] 
        info.dob = request.form['dob']
        info.email = request.form['email']
        info.address = request.form['address']
        info.date_added = date.today()
        try:
            db.session.commit()
            flash("Updated member Successfully testibng :) ",'success')
            return render_template('Viewmember.html', form = searchForm(), member = get_member_info())
        except:
            flash("Error didnt update member", 'danger')
            return render_template('Updatemember.html', form = form, info = info)
    else:
        return render_template('Updatemember.html', form = form, info = info)
    
@app.route('/remove/member/<int:id>',methods = ["POST","GET"])
@login_required
def deletemember(id):
    form = DeleteForm()
    info = Member.query.get_or_404(id)
    
    #check if user wanted to cancel the deletion of the member and redirect them to the view page
    if form.Cancel.data:
        flash('Did not delete member.', 'success')
        return render_template('Viewmember.html', form = searchForm() , member = get_member_info())

    #if the user agreed to delete the member from the database
    if request.method == "POST" and form.validate_on_submit(): 
        try:
            db.session.delete(info)
            db.session.commit()
            flash("Deleted member from database Successfully :) ",'success')
            return render_template('Viewmember.html', form = searchForm(), member = get_member_info())
        except:
            flash("Error there was a problem deleting member Please try again", 'danger')
            return render_template('Viewmember.html', form = searchForm(), member = get_member_info())
    else:
        return render_template('Deletemember.html', form = form, info = info)

###
# The functions below should be applicable to all Flask apps.
### 
def showinfo(place):
    myform = searchForm()  
    if get_member_info() != []:
        render_template(place, form = myform, member = get_member_info())
    else: 
        flash("database is empty no members to show", 'danger')
        return redirect(place)


def get_member_info():
    prop_info = Member.query.all()
    return prop_info


@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        # if user is already logged in, just redirect them to our secure page
        # or some other page like a dashboard
        return redirect(url_for('home'))

    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    # Login and validate the user.
    if form.validate_on_submit():
        # Query the database to see if the username and password entered
        # match a user that is in the database.
        username = form.username.data
        password = form.password.data

        # user = UserProfile.query.filter_by(username=username, password=password)\
        # .first()
        # or
        user = UserProfile.query.filter_by(username=username).first()

        if user is not None and check_password_hash(user.password, password):
            remember_me = False

            if 'remember_me' in request.form:
                remember_me = True

            # If the user is not blank, meaning if a user was actually found,
            # then login the user and create the user session.
            
            login_user(user, remember=remember_me)

            flash('Logged in successfully. WELCOME TO THE PCOG.DBMS :)', 'success')

            next_page = request.args.get('next')
            return redirect(next_page or url_for('home'))
        else:
            flash('Username or Password is incorrect.', 'danger')

    flash_errors(form)
    return render_template('login.html', form=form)


#this call is used for logging out a user
@app.route("/logout")
def logout():
    # Logout the user and end the session
    logout_user()
    flash('You have been logged out.', 'danger')
    return redirect(url_for('home'))

# This callback is used to reload the user object from the user ID stored in the session.
# It should take the unicode ID of a user, and return the corresponding user object.
@login_manager.user_loader
def load_user(id):
    return UserProfile.query.get(int(id))

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    flash(error)
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
