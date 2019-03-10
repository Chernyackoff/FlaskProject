from models import *
from forms import *
from sqlalchemy.exc import IntegrityError
import json

Name = ""


@app.route('/')
def index():
    admin = False
    print(News.query.all())
    logged = 'username' in session
    if logged:
        if User.query.filter_by(username=Name).first().account_type == 'dev':
            admin = True
    return render_template('index.html', source=url_for('static', filename='anchor.ico'), logged_in=logged,
                           admin=admin, session=session, news=News.query.all(),
                           img1=url_for('static', filename='Carousel/img1.jpg'),
                           img2=url_for('static', filename='Carousel/img2.jpg'),
                           img3=url_for('static', filename='Carousel/img3.jpg'))


@app.route('/shop')
def shop():
    logged = 'username' in session
    with open("DB/yachts.json", "rt", encoding="utf8") as f:
        yacht_list = json.loads(f.read())

    name = yacht_list["yachts"][0]["name"]
    text = yacht_list["yachts"][0]["text"]

    return render_template('shop.html', source=url_for('static', filename='anchor.ico'),
                           source1=url_for('static', filename='Shop/green_marine.jpg'),
                           source2=url_for('static', filename='Shop/garcia1.jpg'),
                           source3=url_for('static', filename='Shop/botin1.jpg'),
                           logged_in=logged, session=session)


@app.route('/green_marine')
def boat_page():
    f = open("DB/green_marine.txt", 'r', encoding='UTF-8')
    return render_template('boat.html', source=url_for('static', filename='anchor.ico'),
                           img1=url_for('static', filename='Shop/green_marine.jpg'),
                           img2=url_for('static', filename='Shop/green_marine2.jpg'),
                           img3=url_for('static', filename='Shop/green_marine3.jpg'),
                           name="Green Marine",
                           text=f.read())


@app.route('/garcia_85_beniguet')
def boat1_page():
    f = open("DB/garcia.txt", 'r', encoding='UTF-8')
    return render_template('boat.html', source=url_for('static', filename='anchor.ico'),
                           img1=url_for('static', filename='Shop/garcia1.jpg'),
                           img2=url_for('static', filename='Shop/garcia2.jpg'),
                           img3=url_for('static', filename='Shop/garcia3.jpg'),
                           name="Garcia 85 Beniguet",
                           text=f.read())


@app.route('/botin_65_high_spirit')
def boat2_page():
    f = open("DB/botin.txt", 'r', encoding='UTF-8')
    return render_template('boat.html', source=url_for('static', filename='anchor.ico'),
                           img1=url_for('static', filename='Shop/botin1.jpg'),
                           img2=url_for('static', filename='Shop/botin2.jpg'),
                           img3=url_for('static', filename='Shop/botin3.jpg'),
                           name="Botin 65 HIGH SPIRIT",
                           text=f.read())


@app.route('/forum')
def forum():
    pass


@app.route('/logout')
def logout():
    global Admin
    Admin = 0
    session.pop('username')
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global Admin, Name
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                session['username'] = user.username
                Name = user.username
                if user.username == 'Power._.Vlad':
                    Admin = 1
                return redirect('/')
            else:
                return render_template('login.html',
                                       form=form,
                                       errors=['Неправильный пароль'])
        else:
            return render_template('login.html',
                                   form=form,
                                   errors=['Нет такого матроса!'])
    return render_template('login.html',
                           form=form)


@app.route('/register', methods=["POST", "GET"])
def register():
    global Name
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
            Name = user.username
            return redirect('/')
        except IntegrityError as error:
            print(error)
            return render_template('register.html', form=form,
                                   errors=['Есть такой матрос'])
    else:
        return render_template('register.html', form=form, errors=[])


@app.route('/add_news', methods=["POST", "GET"])
def add_news():
    if User.query.filter_by(username=Name).first().account_type == 'dev':
        form = NewsForm()
        if form.validate_on_submit():
            try:
                news = News(title=form.title.data, text=form.text.data,
                            description=form.description.data)
                db.session.add(news)
                db.session.commit()
                return redirect('/')
            except IntegrityError as error:
                return render_template('add_news.html', form=form, errors=[error])
    else:
        return redirect('/404')
    return render_template('add_news.html', form=form)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found.html', image=url_for('static', filename='404.png'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=1)
