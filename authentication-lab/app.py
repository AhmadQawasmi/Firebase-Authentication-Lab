from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase
config = {
  "apiKey": "AIzaSyC19gphgb8mHDT_jre2njqPSlH5g_I8WZM",
  "authDomain": "authentication-lab-f5d43.firebaseapp.com",
  "projectId": "authentication-lab-f5d43",
  "storageBucket": "authentication-lab-f5d43.appspot.com",
  "messagingSenderId": "882580710209",
  "appId": "1:882580710209:web:b76619292587a9064eb7c0",
  "measurementId": "G-M3302GFZTS",
  "databaseURL": ""
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
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect(url_for('add_tweet'))
        except:
            error = "Authentication failed"
            return render_template("signin.html")
     else:
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


if __name__ == '__main__':
    app.run(debug=True)