from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.secret_key = "your_secret_key_here"

    # Configure upload folder
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Import and initialize routes
    from .routes import init_routes
    init_routes(app)

    return app
