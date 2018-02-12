import os 
from datetime import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__)
messages = []

def add_messages(username, message):
    """Add messages to the messages list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages_dict = {"timesatmp": now, "from": username, "message": message}
    messages.append(messages_dict)
    
    
def get_all_messages():
    """Get all of the messages and seperate them by a <br>"""
    return messages


@app.route("/")
def index():
    """Main page for with instructions"""
    return render_template("index.html")
    
    
@app.route("/<username>")
def user(username):
    """Display chat message"""
    return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())
    
    
@app.route('/<username>/<message>')
def send_message(username, message):
    """Create a new message and redirect back to the chat page"""
    add_messages(username, message)
    return redirect(username)
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)
