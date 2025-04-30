from flask import Flask, request, render_template, redirect, url_for
from logger.logger import get_logs, log_request, ip_location, ip_request


app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        log_request(request)
        ip_request(request)
        return 'Invalid username or password.'
    return render_template('login.html')


@app.route('/logs', methods=['GET'])
def logged():
    logs = get_logs()
    return render_template('logs.html',logs = logs)


@app.route('/locations', methods=['GET'])
def log_location():
    locations = ip_location()
    return render_template('location.html',locations = locations)


@app.route('/ftp')
@app.route('/config')
@app.route('/backup.zip')
def decoy():
    log_request(request)
    ip_request(request)
    return "404 Not Found - This attempt has been logged.", 404


@app.route('/admin')
def admin():
    log_request(request)
    ip_request(request)
    return 'Access denied. This incident will be reported.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
