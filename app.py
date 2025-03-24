from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index_main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    mars_list = ["Человечество вырастает из детства.", "Человечеству мала одна планета.",
                 "Мы сделаем обитаемыми безжизненные пока планеты.", "И начнем с Марса!", "Присоединяйся!"]
    return '</br>'.join(mars_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for("static", filename="img/mars.png")}" alt='Марс'>
                        <figcaption>Вот она какая, красная планета.</figcaption>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def promotion_image():
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" 
                            type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Жди нас, Марс!</h1>
                            <img src="{url_for("static", filename="img/mars.png")}" alt='Марс'>
                            <div class="alert alert-primary" role="alert">
                                Человечество вырастает из детства.
                            </div>
                            <div class="alert alert-danger" role="alert">
                                Человечеству мала одна планета.
                            </div>
                            <div class="alert alert-warning" role="alert">
                                Мы сделаем обитаемыми безжизненные пока планеты.
                            </div>
                            <div class="alert alert-dark" role="alert">
                                И начнем с Марса!
                            </div>
                            <div class="alert alert-success" role="alert">
                                Присоединяйся!
                            </div>
                        </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                        crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css" 
                        href="{url_for('static', filename='css/style.css')}" />
                        <title>Пример формы</title>
                      </head>
                      <body>
                        <h1 class="name-form">Анкета претендента</h1>
                        <h2 class="name-form">на участие в миссии</h2>
                        <div>
                            <form class="login_form" method="post">
                                <input type="text" class="form-control" id="first-name"
                                 placeholder="Введите фамилию" name="first-name">
                                <input type="text" class="form-control" id="last-name"
                                 placeholder="Введите имя" name="last-name">
                                <label for="email"></label>
                                <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                 placeholder="Введите адрес почты" name="email">
                                <div class="form-group">
                                    <label for="classSelect">Какое у Вас образование?</label>
                                    <select class="form-control" id="classSelect" name="class">
                                      <option>Начальное общее образование</option>
                                      <option>Основное общее образование</option>
                                      <option>Среднее общее образование </option>
                                      <option>Среднее профессиональное образование</option>
                                      <option>Высшее образование</option>
                                    </select>
                                 </div>
                                <div class="form-group">
                                    <label for="form-checkbox">Какие у Вас есть профессии?</label>
                                    <div class="form-checkbox">
                                        <input type="checkbox" id="searcher" name="searcher"/>
                                        <label for="searcher">Инженер-исследователь</label>
                                        <br>
                                        <input type="checkbox" id="pilot" name="pilot"/>
                                        <label for="pilot">Пилот</label>
                                        <br>
                                        <input type="checkbox" id="builder" name="builder"/>
                                        <label for="builder">Строитель</label>
                                        <br>
                                        <input type="checkbox" id="biology" name="biology"/>
                                        <label for="biology">Экзобиолог</label>
                                        <br>
                                        <input type="checkbox" id="medic" name="medic"/>
                                        <label for="medic">Врач</label>
                                        <br>
                                        <input type="checkbox" id="meteorologist" name="meteorologist"/>
                                        <label for="meteorologist">Метеоролог</label>
                                        <br>
                                        <input type="checkbox" id="astrogeologist" name="astrogeologist"/>
                                        <label for="astrogeologist">Астрогеолог</label>
                                        <br>
                                        <input type="checkbox" id="climatologist" name="climatologist"/>
                                        <label for="climatologist">Климатолог</label>
                                    </div>
                                </div>
                                <div class="form-group">
                                    <label for="form-check">Укажите пол</label>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" 
                                      name="sex" id="male" value="male" checked>
                                      <label class="form-check-label" for="male">
                                        Мужской
                                      </label>
                                    </div>
                                    <div class="form-check">
                                      <input class="form-check-input" type="radio" 
                                      name="sex" id="female" value="female">
                                      <label class="form-check-label" for="female">
                                        Женский
                                      </label>
                                    </div>  
                                </div>
                                <div class="form-group">
                                    <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                </div>
                                <div class="form-group">
                                    <label for="photo">Приложите фотографию</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <div class="form-group form-check">
                                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                    <label class="form-check-label" 
                                    for="acceptRules">Готовы остаться на Марсе?</label>
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </div>
                      </body>
                    </html>'''


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" 
                            type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Мое предложение: {planet_name}</h1>
                            <h2>Эта планета близка к Земле</h2>
                            <div class="alert alert-success" role="alert">
                                На ней много необходимых ресурсов
                            </div>
                            <div class="alert alert-dark" role="alert">
                                На ней есть вода и атмосфера
                            </div>
                            <div class="alert alert-warning" role="alert">
                                На ней есть небольшое магнитное поле
                            </div>
                            <div class="alert alert-danger" role="alert">
                                Наконец, она просто красива!
                            </div>
                        </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" 
                            type="text/css" href="{url_for('static', filename='css/style.css')}">
                            <title>Колонизация</title>
                          </head>
                          <body>
                            <h1>Результаты отбора</h1>
                            <h2>Претендента на участие в миссии {nickname}:</h2>
                            <div class="alert alert-success" role="alert">
                                Поздравляем! Ваш рейтинг после {level} этапа отбора
                            </div>
                            <h2>составляет {rating}!</h2>
                            <div class="alert alert-warning" role="alert">
                                Желаем удачи!
                            </div>
                        </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 class="name-form">Загрузка фотографии</h1>
                            <h2 class="name-form">для участия в миссии</h2>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                    <div class="form-group">
                                        <label for="photo">Выберите файл</label>
                                        <br>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        <br>
                                        <image class="login_form" src="{url_for('static', filename='img/loaded_image.png')}">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        image_data = request.files['file'].read()
        with open('static/img/loaded_image.png', 'wb') as file:
            file.write(image_data)
        return f'''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                    crossorigin="anonymous">
                                    <link rel="stylesheet" type="text/css" 
                                    href="{url_for('static', filename='css/style.css')}" />
                                    <title>Отбор астронавтов</title>
                                  </head>
                                  <body>
                                    <h1 class="name-form">Загрузка фотографии</h1>
                                    <h2 class="name-form">для участия в миссии</h2>
                                    <div>
                                        <form class="login_form" method="post" enctype="multipart/form-data">
                                            <div class="form-group">
                                                <label for="photo">Выберите файл</label>
                                                <br>
                                                <input type="file" class="form-control-file" id="photo" name="file">
                                                <br>
                                                <image class="login_form" src="{url_for('static', filename='img/loaded_image.png')}">
                                            </div>
                                            <button type="submit" class="btn btn-primary">Отправить</button>
                                        </form>
                                    </div>
                                  </body>
                                </html>'''


if __name__ == '__main__':
    app.run()
