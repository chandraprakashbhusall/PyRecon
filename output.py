import json
from datetime import datetime

def save_json(target, results):

    file = f"reports/{target}_report.json"

    data = {
        "target": target,
        "time": str(datetime.now()),
        "summary": {
            "open": len(results["open"]),
            "closed": len(results["closed"]),
            "filtered": len(results["filtered"])
        },
        "results": results
    }

    with open(file, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[+] JSON saved: {file}")


def save_html(target, results):

    file = f"reports/{target}_report.html"

    html = f"""
    <html>
    <head>
        <title>PyRecon Report</title>
        <style>
            body {{ font-family: Arial; background:#111; color:#eee; }}
            table {{ width:100%; border-collapse: collapse; }}
            th, td {{ border:1px solid #444; padding:8px; }}
            th {{ background:#222; }}
        </style>
    </head>
    <body>
        <h1>PyRecon Report</h1>
        <h3>Target: {target}</h3>

        <h2>OPEN PORTS</h2>
        <table>
        <tr><th>Port</th><th>Service</th><th>Banner</th><th>Risk</th></tr>
    """

    for r in results["open"]:
        html += f"""
        <tr>
            <td>{r['port']}</td>
            <td>{r.get('service','')}</td>
            <td>{r.get('banner','')}</td>
            <td>{r.get('risk','')}</td>
        </tr>
        """

    html += "</table></body></html>"

    with open(file, "w") as f:
        f.write(html)

    print(f"[+] HTML saved: {file}")