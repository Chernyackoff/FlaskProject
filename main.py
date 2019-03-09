from flask import Flask
from flask import render_template, url_for
from flask import request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', source=url_for('static', filename='anchor.ico'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=1)
