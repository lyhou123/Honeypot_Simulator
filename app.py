from flask import Flask, request, render_template, redirect, url_for, flash
from logger.logger import get_logs, log_request, ip_location, ip_request
from validation.brute_force import is_ip_blocked, log_failed_attempt
from dotenv import load_dotenv
import os


load_dotenv()

ADMIN_USERNAME=os.getenv("ADMIN_USERNAME")
ADMIN_PASSWORD=os.getenv("ADMIN_PASSWORD")


app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    ip = request.remote_addr
    
    if is_ip_blocked(ip):
        
        log_request(request)
        ip_request(request)
        
        flash('Too many failed attempts. Try again later')
        return redirect(url_for('login'))
    
    if request.method == "POST":
        username = request.form['email'] 
        password = request.form['password']
        
        if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
            log_failed_attempt(ip)
            flash('Invalid credentails. Please Try Again!')
            return redirect(url_for('login'))
        
        # save activity into our database one for simple ip and the last is store with ip location !
        ip_request(request)
        log_request(request)
        return "Welcome !" 
    
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
