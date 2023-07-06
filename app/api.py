from flask import Flask, request, jsonify, Blueprint
from models import SimpleChatBotModel

api_bp = Blueprint('api', __name__)

@api_bp.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    chatbot = SimpleChatBotModel()
    response = chatbot.generate_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5001)
