import logging
import time
import argparse
from scanner import run_scan
from output import save_json, save_html

logging.basicConfig(
    filename="scan_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def parse_ports(port_range):
    start, end = port_range.split("-")
    return int(start), int(end)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyRecon - Network Scanner")
    
    parser.add_argument("target")
    parser.add_argument("-p", "--ports", default="1-1000")
    parser.add_argument("-m", "--mode", default="Normal")

    args = parser.parse_args()

    start_port, end_port = parse_ports(args.ports)

    results = run_scan(args.target, start_port, end_port, args.mode)

    time.sleep(1)

    save_json(args.target, results)
    save_html(args.target, results)

    print("\n[✓] Scan Completed")