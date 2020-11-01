# サーバを起動するプログラム

from app import app

if __name__ == '__main__':
    # サーバ起動
    app.run(debug=False, host='0.0.0.0', port=8080)
