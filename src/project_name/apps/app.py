from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    """ Функция, отображающая приветствие на корневой странице """
    return 'Hello World!'

if __name__ == '__main__':
    app.run()