from flask import jsonify

def format_response(response):
    return jsonify({"response": response})

def validate_input(user_input):
    if not user_input or not isinstance(user_input, str):
        return False
    return True
