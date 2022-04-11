# PCOG.DBMS 

Remember to always create a virtual environment and install the packages in your requirements file

```bash
$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt 
$ python run.py
$ pip install flask
$ 

# to start your viertual environment and run the flask app:
$ py3 -m venv venv
$ ".\venv\Scripts\activate" "(for windows)"
$ "source venv/bin/activate" "(other than windows)"
$ py run.py

```
```bash


# make the database in postgress sql shell
$ create user "pcog";
$ create database "pcog";
$ #\password pcog  #Password123
$ alter database pcog owner to pcog;

# create a coppy of the .env file with the following:
FLASK_ENV=development
FLASK_RUN_PORT=8080
FLASK_RUN_HOST=0.0.0.0
SECRET_KEY= ak%jh%asd9#!ad8@*^asd%fa$
DATABASE_URL=postgresql://pcog:Password123@localhost/pcog
UPLOAD_FOLDER= 'app/static/uploads'

# for migrations folder to be made initiate your virtual env and run the following commands.
$ pip install flask 
$ pip install Flask-Migrate
$ pip install python-dotenv
$ pip install flask_wtf

# after those commands are ran check the _init_.py and add 
# from flask_migrate import Migrate
# migrate = Migrate(app, db)
# to initiate the databse
# then to create the migrations file run the following commands
$ flask db init
$ flask db migrate 
$ flask db upgrade 
# any other changes made to the database after makeing the changes re use the commands above.

```
```bash

# after adding data to the database you can view the data by opening the psql shell and running the following commands after logging in.
$
$ \c pcog #allows you to enter the specific database
$ \ dt   # shows the tables in the database
$ select * from "insert table name  here";  #to see the data uploaded to the database remove the ("") when typing in the specific table.

# for favicon errors in html 5 add to base.html
# '<link rel="icon" href="data:;base64,iVBORw0KGgo=">'

# To add a user to the database for login to the system :
$ flask shell
$>>> from app import db
$>>> from app.models import UserProfile
$>>> user = UserProfile(first_name="Your name",last_name="Your last name", username="someusername",password="somepassword")
$>>> db.session.add(user)
$>>> db.session.commit()
$>>> quit()

```
```bash