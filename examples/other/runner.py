
import subprocess
import argparse
from datetime import datetime
import os
import pathlib
import platform
import pdb

# Define run_id as a global variable
run_id = None

def add_drivers_to_path():
    curr_file_path = pathlib.Path(__file__).parent.absolute()

    if platform.system() == 'Darwin':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'mac')
    elif platform.system() == 'Windows':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'windows')
    elif platform.system() == 'Linux':
        webdriver_path = os.path.join(curr_file_path, 'webdrivers', 'linux')
    else:
        raise Exception("Unknown platform. Unable to add webdrivers to path.")

    # Fix: Call get() as a function, not a dictionary lookup
    current_path = os.environ.get('PATH', '')  # Provide a default empty string in case PATH is not set
    print(f"Webdriver path: {webdriver_path}")

    new_path = webdriver_path + ':' + current_path
    # pdb.set_trace()
    # print(f"New path: {new_path}")
    os.environ['PATH'] = new_path
    print (f"\n✅ Added webdrivers path '{webdriver_path}' to Path.")

def get_unique_run_id():
    global run_id

    # BUILD_NUMBER is a Jenkins environment variable
    # CUSTOM_BUILD_NUMBER is a custom environment variable

    if os.environ.get("BUILD_NUMBER"):
        unique_run_id = os.environ.get("BUILD_NUMBER")
    elif os.environ.get("CUSTOM_BUILD_NUMBER"):
        unique_run_id = os.environ.get("CUSTOM_BUILD_NUMBER")
    else:
        unique_run_id = datetime.now().strftime('%Y%m%d%H%M%S')

    os.environ['UNIQUE_RUN_ID'] = unique_run_id
    pdb.set_trace()

    return unique_run_id

def create_output_directory(prefix='results_'):
    run_id = get_unique_run_id()

    if not run_id:
        raise Exception("Variable 'run_id' is not set. Unable to create output directory")

    curr_file_path = pathlib.Path(__file__).parent.absolute()
    dir_to_create = os.path.join(curr_file_path, prefix + str(run_id))
    os.mkdir(dir_to_create)

    print(f"Created output directory: {dir_to_create}")

    return dir_to_create

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--test_dir', required=True, help="Location of test file.")
    parser.add_argument('--behave_options', type=str, required=False,
                        help="String of behave options. For Example tags like '-t <tag name>'")

    args = parser.parse_args()
    test_dir = args.test_dir
    behave_options = '' if not args.behave_options else args.behave_options

    output_dir = create_output_directory()
    json_out_dir = os.path.join(output_dir, 'json_report_out.json')
    junit_out_dir = os.path.join(output_dir, 'junit_report_out')

    command = f'behave -k --no-capture -f json.pretty -o "{json_out_dir}" ' \
              f'--junit --junit-directory "{junit_out_dir}" ' \
              f'{behave_options} ' \
              f'{test_dir} '

    try:
        rs = subprocess.run(command, shell=True)
        print(f"\n✅ Running command:\n{command}")
    except Exception as e:
        print(f"\n❌ Error running command:\n{command}")
        print(e)

    try:
        add_drivers_to_path()
    except Exception as e:
        print(f"\n❌ Error adding drivers to path.")
        print(e)

    print(f"Return code: {rs.returncode}")