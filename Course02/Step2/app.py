from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world() -> str:
    return 'Hello World!'


@app.route('/menu')
def menu():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
