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
from .form import Addmember, searchForm
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
    return render_template('about.html', name=" ___")

@app.route("/Member/Addmember",methods=["POST", "GET"])
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

@app.route('/search/members')
def showmember():
    myform = searchForm()  
    if get_member_info() != []:
        
        lenght =length_hint(get_member_info())
        return render_template('Searchmember.html', form = myform, member = get_member_info() ,rootdiri = "rootdir",len = lenght)
    else: 
        flash("database is empty no properties to show", 'danger')
        return redirect('Searchmember.html')

@app.route('/update/members')
def updatemember():
    myform = searchForm()  
    if get_member_info() != []:
        
        lenght =length_hint(get_member_info())
        return render_template('updatemember.html', form = myform, member = get_member_info() ,rootdiri = "rootdir",len = lenght)
    else: 
        flash("database is empty no properties to show", 'danger')
        return redirect('updatehmember.html')
    

###
# The functions below should be applicable to all Flask apps.
###
@app.route('/members/<int:id>',methods=["POST", "GET"])
def viewprop(id):
    form = Addmember()
    info = Member.query.get_or_404(id)
    
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
        try:
            db.session.commit()
            flash("Updated member")
            return render_template('viewprop.html', form = form, info = info)
        except:
            flash("Error didnt update member", 'danger')
            return render_template('viewprop.html', form = form, info = info)
    else:
        return render_template('viewprop.html', form = form, info = info)
    

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
