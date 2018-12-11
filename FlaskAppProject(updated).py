__author__ = 'Tony Teate'

#imports
import sqlite3
from flask import Flask, render_template
from flask import request, redirect, url_for

#instantiate
app = Flask(__name__)
# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'gagnonop' or request.form['password'] != 'happyhour':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('owen_profile'))
        
        if request.form['username'] != 'jackpk' or request.form['password'] != 'snowwhite':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('profile_jack'))
    return render_template('login.htm', error=error)

@app.route('/owen_profile', methods=['GET', 'POST'])
def owen_profile():
    memberID = None
    firstname = ''
    lastname = ''
    age = None
    email = ''
    bio = ''
    success = False

    #Called when the page is first loaded
    if request.method == 'GET':
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()

        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio = row[5]
        conn.close()
    if request.method == 'POST':
        memberID=request.form['memberID']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        age=request.form['age']
        email=request.form['email']
        bio=request.form['bio']
        success = True
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        if row:
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ? WHERE memberID=?''',(firstname, lastname, age, email, bio, memberID))
        else:
            c.execute('''INSERT INTO members VALUES (?,?,?,?,?,?)''',(memberID, firstname, lastname, age, email, bio))
            conn.commit()
            conn.close()
    return render_template('owen_profile.html', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)



        
@app.route('/profile_jack', methods=['GET', 'POST'])
def profile_jack():
    memberID = None
    firstname = ''
    lastname = ''
    age = None
    email = ''
    bio = ''
    success = False

    #Called when the page is first loaded
    if request.method == 'GET':
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()

        if row:
            memberID = row[0]
            firstname = row[1]
            lastname = row[2]
            age = row[3]
            email = row[4]
            bio = row[5]
        conn.close()
    if request.method == 'POST':
        memberID=request.form['memberID']
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        age=request.form['age']
        email=request.form['email']
        bio=request.form['bio']
        success = True
        conn = sqlite3.connect('celebrities.db')
        c = conn.cursor()
        c.execute('''SELECT * FROM members''')
        row = c.fetchone()
        if row:
            c.execute('''UPDATE members SET firstname = ?, lastname = ?, age = ?, email = ?, bio = ? WHERE memberID=?''',(firstname, lastname, age, email, bio, memberID))
        else:
            c.execute('''INSERT INTO members VALUES (?,?,?,?,?,?)''',(memberID, firstname, lastname, age, email, bio))
            conn.commit()
            conn.close()
    return render_template('profile_jack.html', memberID=memberID, firstname=firstname, lastname=lastname, age=age, email=email, bio=bio, success=success)

@app.route('/view_all_celebs')
def view_all():
    celebID = None
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    photo = ''
    bio = ''

    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')
    rows = c.fetchall()
    conn.close()
    return render_template('view_all_celebs.html', rows=rows)
    

@app.route('/view_one_celeb')
def view():
    celebID = None
    firstname = ''
    lastname = ''
    age = ''
    email = ''
    photo = ''
    bio = ''

    conn = sqlite3.connect('celebrities.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM celebs ORDER BY celebID''')
    row = c.fetchone()

    
    celebID = row[0]
    firstname = row[1]
    lastname = row[2]
    age = row[3]
    email = row[4]
    photo = row[5]
    bio = row[6]

    conn.close()
    return render_template('view_one_celeb.html', celebID = celebID, firstname = firstname, lastname = lastname, age = age, email = email, photo = photo, bio = bio) 

    
def get(request):
    pass

def post(request):
    pass

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run(debug=False)

