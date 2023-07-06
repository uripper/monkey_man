from flask import Flask
from api import api_bp
from gui import gui_bp


app = Flask(__name__)

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(gui_bp)

if __name__ == "__main__":
    app.run(host='localhost', port=5001)