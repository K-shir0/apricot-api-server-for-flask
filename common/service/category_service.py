from common.repository.category_repository import CategoryRepository
from common.model.category_model import CategoryModel

# サービスにはhogeモデルが出来ることを書く

class CategoryService:
    _repository: CategoryRepository

    def __init__(self, repository: CategoryRepository):
        # クラス内でレポジトリを利用するため
        self._repository = repository

    def create_category(self, name: str):
        # nameからモデルを作成
        category = CategoryModel(name)

        # hogeモデルをレポジトリのstoreメソッドで永続化
        self._repository.store(category)



