# PCOG.DBMS 

Remember to always create a virtual environment and install the packages in your requirements file

```bash
$ python -m venv venv (you may need to use python3 instead)
$ source venv/bin/activate (or .\venv\Scripts\activate on Windows)
$ pip install -r requirements.txt 
$ python run.py
$ pip install flask
$ 
```
```bash
# make the database in postgress sql shell
$ create user "pcog";
$ create database "pcog";
$ #\password pcog  #Password123
$ alter database pcog owner to pcog;

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
$ falsk db init
$ flask db migrate 
$ flask db upgrade 
# any other changes made to the database after makeing the changes re use the commands above.
```
# after adding data to the database you can view the data by opening the psql shell and running the following commands after logging in.
$
$ \c pcog #allows you to enter the specific database
$ \ dt   # shows the tables in the database
$ select * from "insert table name  here"  # to see the data uploaded to the database