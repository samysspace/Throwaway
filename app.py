from tempmail import Throwaway
from flask import Flask, render_template, request

app = Flask(__name__)

user = Throwaway()
email = user.get_email_address()
#email = "test"

@app.route("/")
def index():
    return """<form method="POST"><p>Your email is {email}</p><input type="submit" value="Check email" /></form>""".format(email=email)

@app.route('/', methods=['POST'])
def form_data():
	emails = user.get_mailbox(email)
	#emails = ["hi", "bye"]
	return """<p>Your emails are: {test}</p><form method="POST"><input type="submit" value="Recheck" /></form>""".format(test=emails)


