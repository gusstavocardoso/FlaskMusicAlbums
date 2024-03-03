from api.albums import albums_bp
from api.auth import auth_bp
from flask_jwt_extended import JWTManager
from flask import Flask
import os
import sys

# Adiciona o diretório 'api' ao PYTHONPATH
sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'api')))


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'
jwt = JWTManager(app)

app.register_blueprint(auth_bp)
app.register_blueprint(albums_bp)

if __name__ == '__main__':
    app.run(debug=True)
