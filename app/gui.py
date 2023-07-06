from flask import Flask, render_template, request, jsonify, Blueprint
from models import SimpleChatBotModel

gui_bp = Blueprint('gui', __name__)

@gui_bp.route('/')
def home():
    return render_template('index.html')

@gui_bp.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    chatbot = SimpleChatBotModel()
    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    gui_bp.run(port=5001)