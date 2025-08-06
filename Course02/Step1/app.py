import socket

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    assert 1 < 0, 'error'
    if app.debug:
        hostname = '컴퓨터(인스턴스):' + socket.gethostname()
    else:
        hostname = ''
    return render_template('index.html', computername=hostname)


@app.route('/test2')
def test2():
    return render_template('test2.html')


if __name__ == '__main__':
    print(__debug__)
    app.run(host='0.0.0.0', port=8080, debug=True)
