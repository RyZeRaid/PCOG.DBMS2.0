"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
from operator import length_hint
import os
from app import app, db
from flask import render_template, request, redirect, url_for,flash,send_from_directory 
from .models import Member
from .form import Addmember
from werkzeug.utils import secure_filename

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
    return render_template('about.html', name="Mary Jane")

@app.route("/Member/Addmember",methods=["POST", "GET"])
def addmember():
    myform = Addmember()

    if request.method == 'GET':
        return render_template('Addmember.html',form=myform )
    print("i see it now")
    if request.method == 'POST':
        if myform.validate_on_submit():
            print("see the error yet ?")
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
            print(type(pri))
            member = Member(position = position, l_name = l_name, f_name = f_name,
                            m_name = m_name, age = age, gender = gender,
                            phonenum = phonenum , dob = dob, email = email,
                            address = address, pri = pri) 
            print("came here")
            db.session.add(member)
            db.session.commit()

            flash('Successfully added a new property','success')
            return redirect(url_for('home'))

    flash_errors(myform)
    return render_template('Addmember.html', form = myform)

@app.route('/properties')
def showmember():
    
    
    if get_member_info() != []:
        rootdir = 'uploads/'
        lenght =length_hint(get_member_info())
        return render_template('properties.html',  member = get_member_info() ,rootdiri = rootdir,len = lenght)
    else: 
        flash("database is empty no properties to show", 'danger')
        return redirect('properties.html')
    

###
# The functions below should be applicable to all Flask apps.
###
@app.route('/properties/<int:id>')
def viewprop(id):
    view_prop = Member.query.get_or_404(id)
    return render_template('viewprop.html', view_prop = view_prop,rootdiri = 'uploads/')


def get_member_info():
    prop_info = Member.query.all()
    return prop_info

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
