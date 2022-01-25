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


email=input("Enter Email:")
password= input("Enter Password:")

# user= auth.create_user_with_email_and_password(email, password)

try:
	user= auth.sign_in_with_email_and_password(email, password)
	auth.get_account_info(user['idToken'])
	print("Success.. You are logged in.")
except:
	print("Invalid Password")
