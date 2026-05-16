MODES = {
    "fast": {"workers": 150, "delay": 0.01},
    "normal":{"workers": 100, "delay": 0.05},
    "stealth": {"workers": 30, "delay": 0.2}
}

MITRE = "T1595 - Active Scanning"

RISK_MAP = {
    "ssh" : "medium",
    "http": "low",
    "https": "low",
    "ftp": "medium",
    "telnet": "high"

}