from tempmail import Throwaway
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    user = Throwaway()
	email = user.getEmailAddress()

