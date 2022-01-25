from flask import Flask, render_template
app= Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signin")
def signIn():
	return render_template("signin.html")

@app.route("/transaction")
def transaction():
	return render_template("transaction.html")

if __name__== "__main__":
	app.run(debug=True)