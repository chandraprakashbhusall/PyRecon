import socket
from config import RISK_MAP

def get_service(port):
    try:
        return socket.getservbyport(port, "tcp")
    except:
        return "Unknown"
    
def get_risk(service):
    return RISK_MAP.get(service, "Unknown")
