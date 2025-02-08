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
