from models import *


@app.route('/')
def index():
    return render_template('index.html', source=url_for('static', filename='anchor.ico'))


@app.route('/shop')
def shop():
    pass


@app.route('/forum')
def forum():
    pass


@app.route('/login')
def login():
    pass


@app.route('/register')
def register():
    pass


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', image=url_for('static', filename='404.png'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=1)
