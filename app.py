from flask import Flask, render_template, abort, url_for, json, jsonify

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

app = Flask(__name__, template_folder='.')

answer = "Hello world! Time is: " + current_time


@app.route("/")
def index():
    return render_template('index.html', title="page", output=answer)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
