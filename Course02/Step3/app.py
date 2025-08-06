import socket

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    if app.debug:
        hostname = '컴퓨터(인스턴스):' + socket.gethostname()
    else:
        hostname = ''
    return render_template('index.html', computername=hostname)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
