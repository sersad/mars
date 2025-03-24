from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            print(file)
            if file.filename:
                file.save('static/img/creation.jpg')
    return f'''<!doctype html>
                 <html lang="en">
                   <head>
                     <meta charset="utf-8">
                     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                     <link rel="stylesheet"
                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                     crossorigin="anonymous">
                     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                     <title>Пример формы</title>
                   </head>
                   <body>
                     <h1 style="text-align: center;">Загрузка фотографии</h1>
                     <h4 style="text-align: center;">для участие в миссия</h4>
                     <div>
                         <form class="login_form" method="post" enctype="multipart/form-data">

                             <div class="form-group">
                                 <label for="photo">Приложите фотографию</label>
                                 <input type="file" class="form-control-file" id="photo" name="file">
                             </div>
                             <img src="{url_for('static', filename='img/creation.jpg')}" alt="Нету фотки">
                             <button type="submit" class="btn btn-primary">Записаться</button>
                         </form>
                     </div>
                   </body>
                 </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')