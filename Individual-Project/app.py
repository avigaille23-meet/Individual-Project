from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

Config = {
  "apiKey": "AIzaSyD0n72GG_1GhyEqLY7OOYXE1DCWVtQlh5M",
  "authDomain": "scouts-a9024.firebaseapp.com",
  "projectId": "scouts-a9024",
  "storageBucket": "scouts-a9024.appspot.com",
  "messagingSenderId": "133652738723",
  "appId": "1:133652738723:web:2c64edd438df47c23f4516",
  "measurementId": "G-QLJVDVM9WT"
  "dataURL":"",
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
	

@app.route('/singin')
def singin():
	return render_template("home.html")

@app.route('/singup')
def singup():
	return render_template("singup.html")
	
	


if __name__ == '__main__':
    app.run(debug=True)