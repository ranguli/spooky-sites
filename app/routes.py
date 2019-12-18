from flask import render_template, request, redirect
from decouple import config 
import slack

from app import app
    
SLACK_API_TOKEN = config('SLACK_API_TOKEN')
SLACK_USER = config('SLACK_USER')

client = slack.WebClient(SLACK_API_TOKEN)

@app.route('/')
def index():
    return render_template('google.html', title='Home')

@app.route('/login')
def login():
    return render_template('github.html', title='Home')

@app.route('/signin')
def signin():
    return render_template('linkedin.html', title='Home')

@app.route('/google', methods=['POST'])
def google():
    client.chat_postMessage(channel=SLACK_USER, text=request.form['Email'] + " please report to the principal's office.")
    return redirect("https://calendar.google.com", code=302)

@app.route('/github', methods=['POST'])
def github():
    client.chat_postMessage(channel=SLACK_USER, text=request.form['login'] + " is overdue for some security training.")
    return redirect("https://github.com", code=302)

@app.route('/linkedin', methods=['POST'])
def linkedin():
    client.chat_postMessage(channel=SLACK_USER, text=request.form['username'] + " fell for the phish.")
    return redirect("https://linkedin.com", code=302)

