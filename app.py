from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Identity Policies Chatbot!"

@app.route('/auth')
def auth():
    return "Authentication successful!"

if __name__ == '__main__':
    app.run(debug=True, port=8080)