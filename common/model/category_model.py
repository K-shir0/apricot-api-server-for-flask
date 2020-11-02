from database.db import db

# 根幹となるモデルを書く、migrationで生成されるのでしっかり書く

class CategoryModel(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<CategoryModel {}:{}>'.format(self.id, self.name)