
# Python script using Flask.
# login control the functionality of the Website.

from flask import Flask, render_template, request, session
import os
import sqlite3

app = Flask(__name__)

'''
Website
'''
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile', methods = ['GET', 'POST'])
def profile():
    return render_template('profile.html')

@app.route('/signup/student', methods = ['GET', 'POST'])
def student():
    if request.method == 'GET':
        return render_template('student.html', msg = "")
    else:
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        age = request.form['age']
        university = request.form['university']
        year = request.form['year']
        interest = request.form['interest']
        username = request.form['username']
        password = request.form['password']

        query = "Select * from Users WHERE username = '%s';"
        rslt = getQueryResult(query % (username))
        if len(rslt) != 0:
            return render_template('student.html', msg = "Choose another username")

        query1 = "Insert into Students VALUES('%s', '%s', '%s', %s, '%s', %s, '%s', '%s');"
        query2 = "Insert into Users VALUES('%s', '%s');"
        rslt = executeQuery(query1 % (firstname, middlename, lastname, age, university, year,
                interest, username), query2 % (username, password))
        
        return profile()

@app.route('/signup/mentor', methods = ['GET', 'POST'])
def mentor():
    if request.method == 'GET':
        return render_template('mentor.html', msg = "")
    else:
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        age = request.form['age']
        profession = request.form['profession']
        experience = request.form['experience']
        interest = request.form['interest']
        username = request.form['username']
        password = request.form['password']

        query = "Select * from Users WHERE username = '%s';"
        rslt = getQueryResult(query % (username))
        if len(rslt) != 0:
            return render_template('mentor.html', msg = "Choose another username")
        
        query1 = "Insert into Students VALUES('%s', '%s', '%s', %s, '%s', %s, '%s', '%s');"
        query2 = "Insert into Users VALUES('%s', '%s');"
        rslt = executeQuery(query1 % (firstname, middlename, lastname, age, profession, experience,
                interest, username), query2 % (username, password))
        return profile()

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', msg = " ")
    else:
        #Get the username and password from the login form
        un = request.form['name']
        pswd = request.form['get_pswd']

        #Check if the login credential is valid
        query = "Select * from Users WHERE username = '%s' AND password = '%s';"
        rslt = getQueryResult(query % (un, pswd))
        if (len(rslt)) == 0:
            return render_template('login.html', msg = "Login failed")
        return render_template('profile.html')

# Executes the query passed via argument and
# returns the result from executing the query on the database.
def getQueryResult(query):
    # Connect to the database
    conn = sqlite3.connect('Percept.db')
    cur = conn.cursor()
    rslt = cur.execute(query).fetchall()
    return rslt

# Inserts values into a table
def executeQuery(query1, query2):
    #Connect to the database
    conn = sqlite3.connect('Percept.db')
    cur = conn.cursor()
    cur.execute(query1)
    cur.execute(query2)
    conn.commit()
    return "Done"


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)