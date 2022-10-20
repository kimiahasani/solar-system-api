from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    
    from .routes import hello_world_bp, planets_bp
    app.register_blueprint(hello_world_bp)
    app.register_blueprint(planets_bp)
    
    return app
