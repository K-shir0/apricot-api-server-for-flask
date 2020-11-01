from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.db import init_db


def create_app():
    application = Flask(__name__)

    # db接続処理
    application.config.from_object('config.config.Config')

    init_db(application)

    return application


app = create_app()
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello World!'
