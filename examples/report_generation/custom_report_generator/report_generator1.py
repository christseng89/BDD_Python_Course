import json
import argparse
import webbrowser
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input_json_file',
                    required=True,
                    help="Path of input json file. JSON file is output of Behave test run")
parser.add_argument('--output_html_file',
                    required=True,
                    help="Path of the output html file to be generated")

args = parser.parse_args()

input_file = args.input_json_file
output_html_path = args.output_html_file

report_styles = """
    <style>
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
        text-align: left;
      }
      th {
        background-color: #4f4f4f;
        color: white;
        font-size: 18px;
      }
      .type-column {
        width: 15%;
      }
      .description-column {
        width: 85%;
      }
      .feature {
        font-weight: bold;
        font-size: 20px;
        background-color: #f8d7da;
      }
      .scenario {
        font-weight: bold;
        cursor: pointer;
      }
      .step {
        font-size: 16px;
        background-color: #fce4ec;
        display: none;
      }
      .type {
        font-weight: bold;
        width: 15%;
      }
      .feature-indent {
        padding-left: 20px;
      }
      .scenario-indent {
        padding-left: 40px;
      }
      .step-indent {
        padding-left: 60px;
      }
      .passed {
        color: blue;
      }
      .failed {
        color: red;
        background-color: #f8d7da;
      }
    </style>
"""

with open(input_file) as file:
    data = json.load(file)

feature_results = {'passed': 0, 'failed': 0}
scenario_results = {'passed': 0, 'failed': 0}

for feature in data:
    feature_results[feature['status']] += 1
    for scenario in feature['elements']:
        scenario_results[scenario['status']] += 1

feature_pass_rate = (
    feature_results['passed'] / sum(feature_results.values())) * 100
scenario_pass_rate = (
    scenario_results['passed'] / sum(scenario_results.values())) * 100

html_content = f"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    {report_styles}
    <title>BDD Custom Report1</title>
    <script>
        function toggleSteps(scenarioId) {{
            var steps = document.querySelectorAll('.step-' + scenarioId);
            steps.forEach(step => {{
                if (step.style.display === 'none') {{
                    step.style.display = 'table-row';
                }} else {{
                    step.style.display = 'none';
                }}
            }});
        }}
    </script>
</head>
<body>
    <h1 class='header'>Scenario Pass Rate: {scenario_pass_rate:.2f}% ({scenario_results['passed']}/{sum(scenario_results.values())})</h1>
    <table class='summary'>
        <tr><th></th><th>Passed</th><th>Failed</th><th>Pass Rate</th></tr>
        <tr><td>Features</td><td class='passed'>{feature_results['passed']}</td><td class='failed'>{feature_results['failed']}</td><td>{feature_pass_rate:.1f}%</td></tr>
        <tr><td>Scenario</td><td class='passed'>{scenario_results['passed']}</td><td class='failed'>{scenario_results['failed']}</td><td>{scenario_pass_rate:.1f}%</td></tr>
    </table>

    <table class='feature-summary'>
        <tr><th class='type-column'>Type</th><th class='description-column'>Description</th></tr>
"""
scenario_id = 0

for feature in data:
    feature_class = 'passed' if feature['status'] == 'passed' else 'failed'
    html_content += f"<tr class='feature {feature_class}'><td class='type'>Feature</td><td class='feature-indent'>{feature['name']}</td></tr>"
    for scenario in feature['elements']:
        scenario_class = 'passed' if scenario['status'] == 'passed' else 'failed'
        scenario_id += 1
        html_content += f"<tr class='scenario {scenario_class}' onclick='toggleSteps({scenario_id})'><td class='type'>Scenario</td><td class='scenario-indent'>{scenario['name']}</td></tr>"
        for step in scenario['steps']:
            if 'result' in step and step['result']['status'] == 'failed':
                error_msg = step.get('result', {}).get('error_message', '')
                html_content += f"<tr class='step step-{scenario_id} failed' style='display: none;'><td class='type'>Step</td><td class='step-indent'>{step['keyword']} {step['name']} {'- ' + error_msg if error_msg else ''}</td></tr>"

html_content += "</table></body></html>"

with open(output_html_path, 'w') as file:
    file.write(html_content)

print("***************************")
print("Feature count: {}".format(feature_results['failed'] + feature_results['passed']))
print("feature_failed_count: {}".format(feature_results['failed']))
print("feature_passed_count: {}".format(feature_results['passed']) + "\n")

print("scenario_count: {}".format(scenario_results['failed'] + scenario_results['passed']))
print("scenario_failed_count: {}".format(scenario_results['failed']))
print("scenario_passed_count: {}".format(scenario_results['passed']))
print("Output html: {}".format(output_html_path))
print("HTML report generated successfully.")
print("***************************")

# Open the generated HTML file in the default web browser
webbrowser.open('file://' + os.path.abspath(output_html_path))
