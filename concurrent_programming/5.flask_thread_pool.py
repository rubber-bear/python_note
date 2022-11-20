import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor() # 全局


def read_file():
    time.sleep(0.1)
    return "file result"


def read_db():
    time.sleep(0.2)
    return "db result"


def read_api():
    time.sleep(0.3)
    return "api result"


@app.route('/')
def index():
    return json.dumps({
        'file_result': pool.submit(read_file).result(),
        'db_result': pool.submit(read_db).result(),
        'api_result': pool.submit(read_file).result(),
    })


if __name__ == '__main__':
    app.run()
