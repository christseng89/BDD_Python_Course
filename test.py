import json

with open('my_custom_reports.json') as file:
    data = json.load(file)

feature_results = {'passed': 0, 'failed': 0}
scenario_results = {'passed': 0, 'failed': 0}

for feature in data:
    feature_results[feature['status']] += 1
    for scenario in feature['elements']:
        scenario_results[scenario['status']] += 1

feature_pass_rate = (feature_results['passed'] / sum(feature_results.values())) * 100
scenario_pass_rate = (scenario_results['passed'] / sum(scenario_results.values())) * 100

html_content = f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <link rel='stylesheet' href='report_style.css'>
    <title>BDD Report</title>
</head>
<body>
    <h1 class='header'>Scenario Pass Rate: {scenario_pass_rate:.2f}% ({scenario_results['passed']}/{sum(scenario_results.values())})</h1>
    <table class='summary'>
        <tr><th></th><th>Passed</th><th>Failed</th><th>Pass Rate</th></tr>
        <tr><td>Features</td><td class='passed'>{feature_results['passed']}</td><td class='failed'>{feature_results['failed']}</td><td>{feature_pass_rate:.1f}%</td></tr>
        <tr><td>Scenario</td><td class='passed'>{scenario_results['passed']}</td><td class='failed'>{scenario_results['failed']}</td><td>{scenario_pass_rate:.1f}%</td></tr>
    </table>

    <table class='feature-summary'>
        <tr><th>Feature</th><th>Scenario</th><th>Status</th></tr>
"""

for feature in data:
    feature_class = 'passed' if feature['status'] == 'passed' else 'failed'
    html_content += f"<tr class='feature {feature_class}'><td colspan='3'>{feature['name']}</td></tr>"
    for scenario in feature['elements']:
        scenario_class = 'passed' if scenario['status'] == 'passed' else 'failed'
        html_content += f"<tr class='scenario {scenario_class}'><td></td><td>{scenario['name']}</td><td class='{scenario_class}'>{scenario['status'].upper()}</td></tr>"
        for step in scenario['steps']:
            if 'result' in step and step['result']['status'] == 'failed':
                error_msg = step.get('result', {}).get('error_message', '')
                html_content += f"<tr class='step failed'><td></td><td colspan='2'>{step['keyword']} {step['name']} {'- ' + error_msg if error_msg else ''}</td></tr>"

html_content += "</table></body></html>"

with open('report.html', 'w') as file:
    file.write(html_content)

with open('report_style.css', 'w') as css:
    css.write("""
    body {
      font-family: Arial, sans-serif;
    }
    .header {
      text-align: center;
      font-size: 24px;
      margin-top: 20px;
    }
    table.summary, table.feature-summary {
      width: 90%;
      margin: 20px auto;
      border-collapse: collapse;
    }
    th, td {
      border: 1px solid #999;
      padding: 12px;
      text-align: center;
    }
    th {
      background-color: #4f4f4f;
      color: white;
      font-size: 18px;
    }
    .feature {
      font-weight: bold;
      font-size: 20px;
      background-color: #ddd;
      text-align: left;
    }
    .scenario {
      text-align: left;
    }
    .passed {
      color: blue;
      font-weight: bold;
    }
    .failed {
      color: red;
      font-weight: bold;
      background-color: #f8d7da;
    }
    .step {
      text-align: left;
    }
    """)

print("HTML report and CSS stylesheet generated successfully.")
