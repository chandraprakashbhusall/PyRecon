import socket
import time
import logging
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

from banner import banner_grab
from intel import get_service, get_risk
from config import MODES, MITRE

def run_scan(target, start_port, end_port, mode):
    cfg = MODES.get(mode, MODES["normal"])

    results = {
        "open": [],
        "closed": [],
        "filtered": []
    }
    lock = Lock()

    def scan_port(port):
        sock = None
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            start = time.time()
            result = sock.connect_ex((target, port))
            duration = time.time() - start

            time.sleep(cfg["delay"])

            if result == 0:
                banner = banner_grab(sock)

                try:
                    service = socket.getservbyport(port, "tcp")
                except:
                    service = "unknown"

                data = {
                    "port": port,
                    "state": "open",
                    "service": service,
                    "banner": banner,
                    "response_time": round(duration, 4),
                    "mitre": MITRE
                }

                with lock:
                    results["open"].append(data)

                print(f"[OPEN] {target}:{port} | {service} | {banner}")

            elif result == 111:
                with lock:
                    results["closed"].append({
                        "port": port,
                        "state": "closed",
                        "response_time": round(duration, 4),
                        "mitre": MITRE
                    })

            else:
                with lock:
                    results["filtered"].append({
                        "port": port,
                        "state": "filtered",
                        "response_time": round(duration, 4),
                        "mitre": MITRE
                    })

        except Exception as e:
            logging.error(f"Scan failed {target}:{port} - {e}")

        finally:
            try:
                sock.close()
            except:
                pass

    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, port)

    return results