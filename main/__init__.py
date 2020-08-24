from flask import Flask

app = Flask(__name__)

app.config.from_envvar('CONFIG')

if app.app_context():
    from main.routes import r_base
    app.register_blueprint(r_base)
