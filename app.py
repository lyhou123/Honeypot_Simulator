from flask import Flask, request, render_template, redirect, url_for
from logger.logger import get_logs, log_request


app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        log_request(request)
        return 'Invalid username or password.'
    return render_template('login.html')


@app.route('/logs', methods=['GET'])
def logged():
    logs = get_logs()
    return render_template('logs.html',logs = logs)


@app.route('/admin')
def admin():
    log_request(request)
    return 'Access denied. This incident will be reported.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
