# Apricot API Server

## Aboutについて - About Apricot


## 開発環境 - Environment
- Python 3.6.12
- PyCharm
- Flask

## スタートガイド - Getting Started
### 環境 - Prerequisites
- pipenv インストール済み

### インストール Installing

#### 1. pipenv installを実行
```
pipenv install
```

#### 2. config/config.sample.pyをコピーしてdb接続設定を書き込む
db接続設定にクォーテーション(')を忘れないで下さい。
```
import os

class DevelopmentConfig:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
        **{
            'user': os.getenv('DB_USER', ###ユーザ###),
            'password': os.getenv('DB_PASSWORD', ###パスワード###),
            'host': os.getenv('DB_HOST', ###接続先###),
            'database': os.getenv('DB_DATABASE', ###データベース名###),
        })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


Config = DevelopmentConfig
```

#### 3. migrationする
```
flask db migrate
flask db upgrade
```

#### 3. pipのshellに入る
```
pipenv shell

(exitでshellから抜けることが出来ます。)
```

#### 4. 実行
```
python run.py
```

