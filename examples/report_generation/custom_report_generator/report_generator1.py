import json
import argparse
import os
from jinja2 import Template

parser = argparse.ArgumentParser()
parser.add_argument('--input_json_file', required=True, help="Path of input json file. JSON file is output of Behave test run")
parser.add_argument('--output_html_file', required=True, help="Path of the output html file to be generated")
args = parser.parse_args()

input_file = args.input_json_file
output_html_path = args.output_html_file

feature_count, feature_failed_count, feature_passed_count = 0, 0, 0
scenario_count, scenario_failed_count, scenario_passed_count = 0, 0, 0

with open(input_file) as f:
    reports = json.load(f)

def calculate_percent_passed():
    total = scenario_failed_count + scenario_passed_count
    return round((scenario_passed_count / total) * 100, 2) if total else 100

rows = []
for report in reports:
    if report['keyword'] == 'Feature':
        feature_count += 1
        if report['status'] == 'passed':
            feature_passed_count += 1
        elif report['status'] == 'failed':
            feature_failed_count += 1

        for scenario in report['elements']:
            scenario_count += 1
            if scenario['status'] == 'passed':
                scenario_passed_count += 1
            elif scenario['status'] == 'failed':
                scenario_failed_count += 1
            rows.append({
                'feature': report['name'],
                'scenario': scenario['name'],
                'status': scenario['status']
            })

percent_passed = calculate_percent_passed()

current_dir = os.path.dirname(os.path.realpath(__file__))
template_path = os.path.join(current_dir, 'template.html')

with open(template_path, 'r') as file:
    html_template = Template(file.read())

html_content = html_template.render(
    percent_passed=percent_passed,
    feature_count=feature_count,
    feature_passed_count=feature_passed_count,
    feature_failed_count=feature_failed_count,
    scenario_count=scenario_count,
    scenario_passed_count=scenario_passed_count,
    scenario_failed_count=scenario_failed_count,
    rows=rows,
    chart_width='600px',
    chart_height='600px',
    chart_style='margin: 20px auto; display: block; border: 1px solid #ddd; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);',
    table_style='margin: 20px auto; border-collapse: collapse; width: 80%; text-align: left; font-family: Arial, sans-serif;',
    th_style='background-color: #343a40; color: white; padding: 10px;',
    td_style='padding: 8px; border: 1px solid #ddd;',
    row_even_style='background-color: #f2f2f2;',
    row_odd_style='background-color: #ffffff;'
)

with open(output_html_path, 'w') as f:
    f.write(html_content)

print("HTML report generated at", output_html_path)

