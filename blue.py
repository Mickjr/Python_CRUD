from flask import Flask
from flask import redirect
from flask import render_template
from flask import session
from flask import request
from flask import escape
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Welcome back %s' % escape(session['username'])+'!'+'<br/>'+'Your password is "%s' % escape(session['password'])+'"'+'<br/>'+'<img src="static/%s" />' % escape(session['file'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        session['file'] = request.form['file']
        return redirect(url_for('index'))
    return '''
    <!DOCTYPE HTML>
	<html>
	<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
	<title>Lab 6</title>
 	<link type="text/css" rel="stylesheet" href="static/css/styles.css">
 	</head>
 	<body>
 	<h1>Please login user</h1>
    <form action="" method="post">
        <p><input type=text name=username placeholder="Enter Username"></p>
        <p><input type=password name=password placeholder="Enter Password"></p>
        <p><input type=file name=file></p>
        <p><input type="submit" class="button4" name=login/><p>
    </form>
    '''

@app.route('/logout')
def logout():
    # remove the username and password from the session if it's there
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
	app.run()
