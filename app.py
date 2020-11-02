from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from database.db import init_db

from common.model.category_model import CategoryModel
from common.service.category_service import CategoryService
from common.repository.category_repository import CategoryRepository


def create_app():
    application = Flask(__name__)

    # db接続処理
    application.config.from_object('config.config.Config')

    init_db(application)

    return application


app = create_app()
db = SQLAlchemy(app)

# サービス定義する
_categoryApplicationservice = CategoryService(
    CategoryRepository(db)
)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/category')
def category_post():
    name = 'aaaaaa'

#     サービスを利用して,categoryを作成
    _categoryApplicationservice.create_category(
        name
    )


    # コミットはすべての処理が終わってから、整合性がとれなくなるため
    db.session.commit()

    return 'success'