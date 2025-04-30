import sqlite3
from datetime import datetime

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

    conn = sqlite3.connect('database/honeypot.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ip TEXT,
            endpoint TEXT,
            user_agent TEXT,
            data TEXT,
            timestamp TEXT
        )
    ''')
    c.execute('''
        INSERT INTO logs (ip, endpoint, user_agent, data, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (ip, endpoint, user_agent, str(data), datetime.now().isoformat()))
    
    conn.commit()
    conn.close()
