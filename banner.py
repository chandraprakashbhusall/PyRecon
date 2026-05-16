import logging

def banner_grab(sock):
    try:
        sock.settimeout(0.5)
        data = sock.recv(1024).decode(errors="ignore").strip()

        banner = data.split("\n")[0].strip()
        return banner

    except Exception as e:
        logging.error(f"Banner grabbing failed {e}")
        return "No Banner"