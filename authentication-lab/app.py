from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config= {
  "apiKey": "AIzaSyDJbN7Rtjqwdja1qBDJWDovmFrfmb4jBRo",
  "authDomain": "ella-s-firsts-firebase-project.firebaseapp.com",
  "projectId": "ella-s-firsts-firebase-project",
  "storageBucket": "ella-s-firsts-firebase-project.appspot.com",
  "messagingSenderId": "965372458361",
  "appId": "1:965372458361:web:2040960fd0e8f69c6e6ba8",
  "measurementId": "G-CH06891GD0",
  "databaseURL":""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

 
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
           login_session['user'] = auth.sign_in_with_email_and_password(email, password)
           return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
           return render_template("signin.html")
    if request.method == 'GET':
        return render_template("signin.html")



@app.route('/signup', methods=['GET', 'POST'])
def signup():
   error = ""
   if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
       except:
           error = "Authentication failed"
   return render_template("signup.html")



@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

@app.route('/signout')
def signout():
    login_session['user'] = None
    auth.current_user = None
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)