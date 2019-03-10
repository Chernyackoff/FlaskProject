from models import *
from forms import *
from sqlalchemy.exc import IntegrityError


@app.route('/')
def index():
    logged = 'username' in session
    return render_template('index.html', source=url_for('static', filename='anchor.ico'), logged_in=logged,
                           session=session)


@app.route('/shop')
def shop():
    pass


@app.route('/forum')
def forum():
    pass


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/index')


@app.route('/login', methods=[])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                session['username'] = user.username
                return redirect('/index')
            else:
                return render_template('login.html',
                                       form=form,
                                       errors=['Incorrect password'])
        else:
            return render_template('login.html',
                                   form=form,
                                   errors=['No such user found!'])
    return render_template('login.html',
                           form=form)


@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User(username=form.username.data,
                        email=form.email.data,
                        password_hash=generate_password_hash(form.password.data),
                        account_type=form.account_type.data)
            session['username'] = user.username
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except IntegrityError:
            return render_template('register.html', form=form,
                                   errors=['Another user with this email/username already exists!'])
    return render_template('register.html', form=form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', image=url_for('static', filename='404.png'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=1)
