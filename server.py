import logging

from flask import Flask, url_for, request, render_template, redirect, make_response, jsonify

from data import db_session, jobs_api, users_resource, jobs_resource
from data.jobs import Jobs
from data.users import User
from forms.job import JobForm
# from forms.job import JobForm
from forms.loginform import LoginForm

from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# from forms.user import RegisterForm

from flask_restful import reqparse, abort, Api, Resource

from forms.user import RegisterForm


# logging.basicConfig(level=logging.INFO,
#                     filename='logs/logfile.log',
#                     format='%(asctime)s %(levelname)s %(name)s %(message)s')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

api = Api(app)

# # для списка объектов
# api.add_resource(users_resources.UsersListResource, '/api/v2/users')
#
# # для одного объекта
# api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:users_id>')

login_manager = LoginManager()
login_manager.init_app(app)


api = Api(app)

# для списка объектов
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')

# для одного объекта
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:job_id>')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Url not found'}), 404)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            surname=form.surname.data,
            email=form.email.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@login_required
@app.route('/addjob', methods=['GET', 'POST'])
def addjob():
    form = JobForm()
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    form.team_leader.choices = [(i.id, i.name) for i in users]

    if form.validate_on_submit():
        job = Jobs(
            job=form.job.data,
            work_size=form.work_size.data,
            team_leader=form.team_leader.data,
            is_finished = form.is_finished.data
        )
        if form.collaborators.data:
            job.collaborators = form.collaborators.data
        if form.start_date.data:
            job.start_date = form.start_date.data
        if form.end_date.data:
            job.end_date = form.end_date.data

        db_sess.add(job)
        db_sess.commit()
        return redirect('/')
    return render_template('addjob.html', title='Добавление работы', form=form)


@app.route('/')
@app.route('/index')
def index(title='Журнал работ'):
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('index.html', title=title, jobs=jobs)


@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, title='Тренировки в полёте')


@app.route('/list_prof/')
@app.route('/list_prof/<prof>')
def list_prof(prof='ol'):
    professions = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                   'инженер по терраформированию', 'климатолог',
                   'специалист по радиационной защите', 'астрогеолог', 'гляциолог',
                   'инженер жизнеобеспечения', 'метеоролог', 'оператор марсохода', 'киберинженер',
                   'штурман', 'пилот дронов']
    return render_template('list_prof.html', prof=prof, professions=professions, title='Список профессий')


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {
        'title': 'Автоматический ответ',
        'surname': 'Biden',
        'name': 'Joe',
        'education': 'middle',
        'profession': 'enginer',
        'sex': 'male',
        'motivation': 'money',
        'ready': 'yes'
    }
    return render_template('auto_answer.html', **param)


@app.route('/promotion')
def promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Рекламная компания</title>
                  </head>
                  <body>
                    <h1>Человечество вырастает из детства.</h1>
                    <h1>Человечеству мала одна планета.</h1>
                    <h1>Мы сделаем обитаемыми безжизненные пока планеты.</h1>
                    <h1>И начнем с Марса!</h1>
                    <h1>Присоединяйся!</h1>
                  </body>
                </html>"""


@app.route('/image_sample')
def image():
    return f'''	<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                   </head>
                    <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                               alt="здесь должна была быть картинка, но не нашлась">
                        <br>Вот какая она, красная планета.<br>
                    </body>
                    </html>'''


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <title>Реклама с картинкой</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" 
                            width="300" height="300" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <div class="alert alert-secondary" role="alert"><p>Человечество вырастает из детства.</p></div>
                        <div class="alert alert-success" role="alert"><p>Человечеству мала одна планета.</p></div>
                        <div class="alert alert-secondary" role="alert"><p>Мы сделаем обитаемыми безжизненные пока планеты.</p></div>
                        <div class="alert alert-warning" role="alert"><p>И начнем с Марса!</p></div>
                        <div class="alert alert-danger" role="alert"><p>Присоединяйся!</p></div>
                      </body>
                    </html>"""


def user_create():
    session = db_session.create_session()
    user = User(surname='Scott',
                name='Ridley',
                age=21,
                position='captain',
                speciality='research engineer',
                address='module_1',
                email='scott_chief@mars.org')
    session.add(user)

    user = User(surname='Harry',
                name='Potter',
                age=14,
                position='magl',
                speciality='engineer',
                address='module_1',
                email='harry@mars.org')
    session.add(user)
    user = User(surname='Joe',
                name='Biden',
                age=65,
                position='president',
                speciality='biology',
                address='module_2',
                email='biden@mars.org')
    session.add(user)
    user = User(surname='Tramp',
                name='Mars',
                age=35,
                position='mechanic',
                speciality='electronic',
                address='module_3',
                email='tramp@mars.org')
    session.add(user)
    session.commit()


def jobs_create():
    session = db_session.create_session()
    job = Jobs(team_leader=1,
               job='deployment of residential modules 1 and 2',
               work_size=15,
               collaborators='2, 3')
    session.add(job)
    job = Jobs(team_leader=1,
               job='cleaning of residential modules 1 and 2',
               work_size=10,
               collaborators='3, 4')
    session.add(job)
    session.commit()


db_session.global_init('db/mars_explorer.db')
# app.register_blueprint(jobs_api.blueprint)
# user_create()
# jobs_create()
app.register_blueprint(jobs_api.blueprint)

