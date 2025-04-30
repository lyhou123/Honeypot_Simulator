SUSPICIOUS_AGENTS = ["curl", "httpie", "wget", "python", "sqlmap", "nmap"]

def is_bot(user_agent: str, headers: dict) -> bool:
    if not user_agent:
        return True
    ua = user_agent.lower()
    for agent in SUSPICIOUS_AGENTS:
        if agent in ua:
            return True
    if len(headers) < 3:
        return True
    return False
