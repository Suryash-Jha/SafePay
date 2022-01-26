from flask import Flask, render_template, request
import pyrebase
config= {
	"apiKey": "AIzaSyB4VSVSOd3RIdjsZ9OMKcRY1OMNgH5O9DU",
    "authDomain": "safepay-47417.firebaseapp.com",
    "projectId": "safepay-47417",
    "storageBucket": "safepay-47417.appspot.com",
    "messagingSenderId": "897420803391",
    "appId": "1:897420803391:web:a9e437278baedc46d5678a",
    "databaseURL": "https://safepay-47417-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase= pyrebase.initialize_app(config)
auth= firebase.auth()

app= Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
	s= "Success"
	us= "Wrong Credentials"
	if request.method== 'POST':
		email= request.form['lemail']
		password= request.form['lpass']
		try:
			user= auth.sign_in_with_email_and_password(email, password)
			return render_template("login.html", s= s)

		except:
			return render_template("login.html", us= us)
	return render_template("login.html")

@app.route("/signin", methods=['GET', 'POST'])
def signIn():
	text= "ID created."
	problem="Email exists"
	if request.method== 'POST':
		email= request.form['semail']
		password= request.form['spass']
		try:
			user= auth.create_user_with_email_and_password(email, password)
			return render_template("signin.html", text= text)
		except:
			return render_template("signin.html", problem= problem)
            


	return render_template("signin.html")

@app.route("/transaction")
def transaction():
	return render_template("transaction.html")

if __name__== "__main__":
	app.run(debug=True)