# BDD 
## Install environments

### Python virtual environment (different python version)
```cmd
where python
    C:\Program Files\Python313\python.exe
    C:\Users\samfi\AppData\Local\Microsoft\WindowsApps\python.exe

python --version
    Python 3.13.1

C:\Users\samfi\AppData\Local\Microsoft\WindowsApps\python --version
    Python 3.13.2

virtualenv c:\testpy313.1
    created virtual environment CPython3.13.1.final.0-64 in 506ms
    ...

cd c:\testpy313.1
python -m venv venv
Scripts\activate
    python --version
        Python 3.13.1
    deactivate
cd ..

virtualenv --python=C:\Users\samfi\AppData\Local\Microsoft\WindowsApps\python.exe c:\testpy313.2
    created virtual environment CPython3.13.2.final.0-64 in 8205ms
    ...

cd c:\testpy313.2
Scripts\activate
    python --version
        Python 3.13.2
    deactivate
cd ..

rd /s /q c:\testpy313.1
rd /s /q c:\testpy313.2

```
### Virtual Environment - BDD Python Course
```cmd
virtualenv C:\Users\samfi\PycharmProjects\BDD_Python_Course
cd C:\Users\samfi\PycharmProjects\BDD_Python_Course
Scripts\activate.bat
    deactivate
```
### Install behave and selenium
```cmd
pip install selenium
pip install behave
```

// Download Chromedriver
https://chromedriver.chromium.org/

## BDD Components

### BDD Foler structure
BDD Consists
   - Scenrio with Steps (Given, When, Then, And, located in feature files)
   - Step definition (located in python files)

BDD Folder structure
1. A 'steps' folder is required
2. A 'features' folder is optional

### Gherkin Keywords
1. Feature
2. Scenario
3. Given
4. When
5. Then
6. And
7. But

#### Folder Structure Example
```cmd
BDD_Python_Course
    examples
        login_negative.feature
        login_new_user.feature
        login_positive.feature
        steps
            steps.py

behave examples\directory_structure\feature_template.feature

```
### Running 1 file DEMO
```cmd
behave "examples\running_tests\Test Group\test_case_1.feature"
behave "examples\running_tests\Test Group\test_case_2.feature"
behave "examples\running_tests\Test Group\login\login.feature"

REM Running with print() in steps
behave "examples\running_tests\Test Group\test_case_1.feature" --no-capture
behave "examples\running_tests\Test Group\test_case_2.feature" --no-capture
behave "examples\running_tests\Test Group\login\login.feature" --no-capture

REM Output with logger.info() and print() in steps via environment.py
behave examples\displaying_output\displaying_output_demo.feature 
behave examples\displaying_output\displaying_output_demo.feature --no-capture

```
### Running all files DEMO
```cmd
behave "examples\running_tests\Test Group"
behave "examples\running_tests\Test Group" --no-capture
    Feature: Test Cases Group 1 # examples/running_tests/Test Group/test_case_1.feature:2
    ...
    Feature: Test Cases Group 2 # examples/running_tests/Test Group/test_case_2.feature:2
    ...
    Feature: Negative test for login # examples/running_tests/Test Group/login/login_negative/login_negative.feature:2
    ...
    4 features passed, 0 failed, 0 skipped
    ...
```

```cmd
behave "examples\running_tests\Test Group\login" --no-capture
    ...
    2 features passed, 0 failed, 0 skipped
    ...

```
### Displaying Output
```cmd
behave examples\displaying_output\displaying_output_demo.feature
behave examples\displaying_output\displaying_output_demo.feature --no-capture
behave examples\displaying_output\displaying_output_demo.feature --no-capture --no-logcapture
behave examples\displaying_output\displaying_output_demo.feature --no-capture --no-logcapture --logging-format "Info: %(message)s"
```

## Parameterization

### Example
Given I am 'New' User
Given I am 'Existing' User
@given('I am {user_type} User')

Then the page should '' contain the text Welcome
Then the page should 'not' contain the text Welcome
@then('the page should {contain} contain the text Welcome')

The user buy the order with 'credit' card
The user buy the order with 'debit' card
@then('the user buy the order with {card_type} card')

Given I am using 'English' language
Given I am using 'Spanish' language
@given('I am using {lang_type} language')

### Parameterization DEMO
```cmd
behave examples\step_parameters\step_parameters_parse.feature
behave examples\step_parameters\step_parameters_parse.feature --no-capture
```

### Sharing Data Between Steps
context.variable_name = value

### Sharing Data Between Steps DEMO
```cmd
behave examples\sharing_data_globally\sharing_data_globally_demo.feature
behave examples\sharing_data_globally\sharing_data_globally_demo.feature --no-capture
```

## Practical Example

### Project Setup Overview (Building a Python Package)
```cmd
pip install setuptools

cd practical_examples
pip install .
pip uninstall PythonBDDtutorial -y

pip install .
```

### Test Cases Group 1 Part 1 (python.org)
```cmd
behave tests\python_main_site\features\python_home_page_url.feature
behave tests\python_main_site\features\home_page_nav_bars.feature

behave tests\python_main_site\features\python_home_page_url.feature --no-capture
behave tests\python_main_site\features\home_page_nav_bars.feature --no-capture
```

## Setup and Tear Down

### Setup and Tear Down (Concept)
- Setup: Before all tests (Feature, Scenario, or Step)
- Tear Down: After all tests (Feature, Scenario, or Step)

behave support setup and tear down via environment.py

#### Examples
- Setup
  - Open browser
  - Login
  - Create a new Database 
  - Create a new table
  - Create a new user
  - Create files to be used for testing
  - Congigure things like logging, browser type, etc.
- Tear Down
  - Close browser
  - Logout
  - Delete a database
  - Delete a table
  - Delete the user
  - Delete files created for testing
  - Reset configurations 

#### Environmental Controls
https://behave.readthedocs.io/en/stable/tutorial.html#environmental-controls
- before_step(context, step), after_step(context, step)
    These run before and after every step.
- before_scenario(context, scenario), after_scenario(context, scenario)
    These run before and after each scenario is run.
- before_feature(context, feature), after_feature(context, feature)
    These run before and after each feature file is exercised.
- before_tag(context, tag), after_tag(context, tag)
    These run before and after a section tagged with the given name. They are invoked for each tag encountered in the order they’re found in the feature file. See controlling things with tags.
- before_all(context), after_all(context)
    These run before and after the whole shooting match.

### Setup and Tear Down DEMO
// enhance environment.py

```cmd
cd practical_examples
behave tests\python_main_site\features\home_page_nav_bars.feature --no-capture --no-logcapture
    ...
    INFO:behave_logger:Scenario 'Verify the navigation bars on home page are visible' is starting...
    ...
    INFO:behave_logger:Scenario 'Verify the navigation bars on home page are visible' passed.
    
cd ..
behave examples\setup_teardown_environment_py --no-capture --no-logcapture
```

### Background
[Before scenario vs Background](.\BDD Before Scenario vs Background.xlsx)

1. One background per feature file
2. Background runs before every scenario in the feature file
3. Background (Gherkin steps) runs after before_scenario
4. Background usage such as Open Browser, Login, etc.

#### DB Testing Recommended Structure:
**Example1: Migration**
1. **before_feature** → Create the database and tables before all scenarios.
2. **before_scenario** → Insert test records before each scenario.
3. **after_scenario** → Clean up the test records after each scenario.
4. **after_feature** → Drop the database and clean up after all scenarios have executed.
5. **Background** → Check test records exist before executing each scenario.

**Example2: Test create a record**
1. **before_feature** → Insert records before all scenarios.
2. **after_feature** → Delete records after all scenarios have executed.
3. **Background** → Check test records exist before executing each scenario.

**Example:**
```gherkin
Background:
    Given the users table is cleared
    And the following users exist in the database
      | id | name  | balance |
      | 1  | Alice | 1000    |
      | 2  | Bob   | 500     |
```
