from flask_sqlalchemy import SQLAlchemy
from common.model.category_model import CategoryModel

# repositoryにはDBに関する処理を書いて閉じ込める、commitだけはここでしない

class CategoryRepository:
    _db: SQLAlchemy

    def __init__(self, db):
        self._db = db

    def store(self, category: CategoryModel):
        self._db.session.add(category)

