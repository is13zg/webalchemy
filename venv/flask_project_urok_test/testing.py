from flask import render_template
import requests
from flask import request
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение:{planet_name} </h1>
                    <div class="alert alert-light " role="alert">
                      Ближайшая к Земле планета
                    </div>
                    <div class="alert alert-danger " role="alert">
                      Человечеству мала одна планета
                    </div>
                    <div class="alert alert-secondary " role="alert">
                      Все на Марс
                    </div>
                    <div class="alert alert-warning " role="alert">
                      Вперед к новому миру
                    </div>
                    <div class="alert alert-info " role="alert">
                      Станьте первым колонизатором Марса
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')