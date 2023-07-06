from flask import Flask, render_template, request, jsonify
from .models import SimpleChatBotUI

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    chatbot = SimpleChatBotUI()
    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(port=5001)