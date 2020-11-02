# サーバを起動するプログラム

from app import app

if __name__ == '__main__':
    # サーバ起動
    app.run(debug=False, host='127.0.0.1', port=8080)
