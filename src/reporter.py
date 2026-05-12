# reporter.py - Generate CSV and HTML cost reports
import csv
import os
import json
from datetime import datetime


def generate_report(data, output_dir='./reports'):
    os.makedirs(output_dir, exist_ok=True)
    ts = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    # CSV Report
    csv_path = f'{output_dir}/report_{ts}.csv'
    with open(csv_path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['id', 'name', 'type', 'state', 'avg_cpu_7d'])
        w.writeheader()
        for inst in data['instances']:
            w.writerow({k: inst.get(k, '') for k in ['id', 'name', 'type', 'state', 'avg_cpu_7d']})
    print(f'CSV report: {csv_path}')

    # HTML Report
    html_path = f'{output_dir}/report_{ts}.html'
    rows = ''.join(
        f'<tr><td>{i["id"]}</td><td>{i["name"]}</td><td>{i["type"]}</td><td>{i["state"]}</td></tr>'
        for i in data['instances']
    )
    html = f'''<!DOCTYPE html>
<html>
<head>
  <title>AWS Cost Report</title>
  <style>
    body {{ font-family: Arial; background: #0f172a; color: white; padding: 24px; }}
    table {{ border-collapse: collapse; width: 100%; }}
    th, td {{ padding: 10px; border: 1px solid #334155; text-align: left; }}
    th {{ background: #1e293b; }}
    h1 {{ color: #6366f1; }}
    .cost {{ font-size: 2em; color: #22c55e; }}
  </style>
</head>
<body>
  <h1>AWS Cloud Monitor Report</h1>
  <p>Generated: {data["timestamp"]} | Region: {data["region"]}</p>
  <div class="cost">Est. Monthly Cost: ${data["cost"]["total"]}</div>
  <p>EC2: ${data["cost"]["ec2"]} | S3: ${data["cost"]["s3"]}</p>
  <h2>EC2 Instances ({len(data["instances"])})</h2>
  <table>
    <tr><th>ID</th><th>Name</th><th>Type</th><th>State</th></tr>
    {rows}
  </table>
  <h2>Idle Instances ({len(data["idle_instances"])})</h2>
  <p>These instances have &lt;5% avg CPU over 7 days. Consider stopping them.</p>
</body>
</html>'''
    with open(html_path, 'w') as f:
        f.write(html)
    print(f'HTML report: {html_path}')
