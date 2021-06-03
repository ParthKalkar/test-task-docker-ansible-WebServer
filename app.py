from flask import Flask

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


app = Flask(__name__)


@app.route('/')
def hello_world():
    answer = "Hello world! Time is:" + " " + current_time
    return answer


if __name__ == '__main__':
    app.run()
