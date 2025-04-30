import sqlite3
from datetime import datetime
from bot.bot_detector import is_bot
import os

DATABASE_PATH = os.path.join(os.getcwd(), 'database', 'honeypot.db')

def get_logs():
    
    """Fetch all logs from the honeypot database."""
    conn = sqlite3.connect('database/honeypot.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM logs')  
    logs = c.fetchall()
    
    conn.close()
    return logs



def log_request(req):
    
    ip = req.remote_addr
    endpoint = req.path
    user_agent = req.headers.get('User-Agent')
    data = dict(req.form) if req.form else None
    headers    = dict(req.headers)
    is_bot_flag = is_bot(user_agent,headers)

    conn = sqlite3.connect('database/honeypot.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            endpoint TEXT,
            user_agent TEXT,
            data TEXT,
            is_bot INTEGER,
            timestamp TEXT
        )
    ''')
    c.execute('''
        INSERT INTO logs (ip, endpoint, user_agent, data, is_bot, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (ip, endpoint, user_agent, str(data), int(is_bot_flag), datetime.now().isoformat()))
    
    conn.commit()
    conn.close()


#this is methon are trigger ip address where come from ! 
def ip_request(request):
    
    ip = request.remote_addr
    
    try:
        geo_url = f'https://ipapi.co/{ip}/json/'
        response = request.get(geo_url, timeout=5)
        get_data = response.json()
        
        country = get_data.get('country_name','Unknown')
        city    = get_data.get('city',"unkown")
        
    except Exception:
        country = 'Unavailable'
        city = 'Unavailable'
        
    conn = sqlite3.connect('database/iplocation.db')
    c    = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            path TEXT,
            method TEXT,
            country TEXT,
            city TEXT,
            timestamp TEXT
        )
    ''')

    c.execute('''
        INSERT INTO locations (ip, path, method, country, city, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        ip,
        request.path,
        request.method,
        country,
        city,
        datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ))

    conn.commit()
    conn.close()

def ip_location():
       
       conn = sqlite3.connect('database/iplocation.db')
       c = conn.cursor()
    
       c.execute('SELECT * FROM locations')  
       logs = c.fetchall()
    
       conn.close()
       return logs
         