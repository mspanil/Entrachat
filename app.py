import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the OpenAI API client
openai.api_key = os.getenv('OPENAI_API_KEY')

def chatbot_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ],
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].message['content'].strip()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = chatbot_response(user_input)
    return jsonify({"response": response})

@app.route('/')
def home():
    return "Welcome to the Identity Policies Chatbot!"

if __name__ == '__main__':
    app.run(debug=True, port=8000)