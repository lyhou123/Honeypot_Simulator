from datetime import datetime, timedelta

# Stores failed login attempts
failed_login = {}

# Limit configuration
LIMIT = 5
TIMEFRAME = timedelta(minutes=1)

def is_ip_blocked(ip):
    """Check if the IP is currently blocked."""
    if ip not in failed_login:
        failed_login[ip] = []

    # Remove outdated attempts
    failed_login[ip] = [
        time for time in failed_login[ip]
        if time > datetime.now() - TIMEFRAME
    ]

    return len(failed_login[ip]) >= LIMIT

def log_failed_attempt(ip):
    """Record a failed login attempt for this IP."""
    if ip not in failed_login:
        failed_login[ip] = []
    failed_login[ip].append(datetime.now())
