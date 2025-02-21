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
## Scenario Outline
```cmd
behave examples\scenario_outline\scenario_outline_demo.feature --no-capture --no-logcapture
behave examples\scenario_outline\scenario_outline_demo_2.feature --no-capture --no-logcapture

behave examples\scenario_outline\examples_in_slides --no-capture --no-logcapture
behave examples\scenario_outline --no-capture --no-logcapture --tags=tag1
```

## Tags
### Purpose of Tags
1. Selective Test Execution 
    behave --tags=@tag1
2. Categorize Tests
    @smoke for smoke tests,
    @regression for regression tests,
    @wip for work-in-progress tests.
3. Skip Tests
    behave --tags=~@integration (skip integration tests)
    behave --tags=(@aa and @bb) and not @cc (run aa, bb, skip cc)
4. Environment-Specific Tests
    behave --tags=@dev (@qa, @regression, @batch, @sit, @uat, @staging, @prod, etc.)

5. Apply Hooks to Specific Tests
    @before_scenario, @after_scenario, @before_feature, @after_feature, @before_all, @after_all,
    @before_tag, @after_tag, @before_step, @after_step

https://behave.readthedocs.io/en/latest/tag_expressions/

**Example:**
```gherkin
behave --show-skipped --tags=~@skip
behave --no-skipped --tags=~@skip

```

**Tags Help**
```cmd
behave --tags-help
    Scenarios inherit tags declared on the Feature level. The simplest
    TAG_EXPRESSION is simply a tag::
    
        --tags @dev
    
    You may even leave off the "@" - behave doesn't mind.
    
    When a tag in a tag expression starts with a ~, this represents boolean NOT::
    
        --tags ~@dev
    
    A tag expression can have several tags separated by a comma, which represents
    logical OR::
    
        --tags @dev,@wip
    
    The --tags option can be specified several times, and this represents logical
    AND, for instance this represents the boolean expression
    "(@foo or not @bar) and @zap"::
    
        --tags @foo,~@bar --tags @zap.
    
    Beware that if you want to use several negative tags to exclude several tags
    you have to use logical AND::
    
        --tags ~@fixme --tags ~@buggy.
```

### Tags DEMO
```cmd
behave examples\using_tags --no-capture --no-logcapture
behave examples\using_tags --no-capture --no-logcapture --tags @smoke
behave examples\using_tags --no-capture --no-logcapture --tags @homepage

behave examples\using_tags --no-capture --no-logcapture --tags ~@smoke
behave examples\using_tags --no-capture --no-logcapture --tags=@homepage,@smoke
behave examples\using_tags --no-capture --no-logcapture --tags=@homepage,@smoke --tags=~@logged_in
behave examples\using_tags --no-capture --no-logcapture --tags=@homepage,@smoke --tags=~@regression

behave examples\using_tags --no-capture --no-logcapture --tags=@homepage --tags=@logged_out

```

## Generate Reports
```cmd
behave examples\report_generation\my_feature_1.feature --no-capture --no-logcapture
    Assertion Failed: Step failed due to exception: ❌ Failing on purpose

behave examples\report_generation\my_feature_2.feature --no-capture --no-logcapture
behave examples\report_generation\my_feature_3.feature --no-capture --no-logcapture
    Assertion Failed: Step failed due to exception: ❌ Failing on purpose

behave examples\report_generation --no-capture --no-logcapture
```

https://behave.readthedocs.io/en/stable/behave.html
https://behave.readthedocs.io/en/stable/behave.html#cmdoption-junit
https://behave.readthedocs.io/en/stable/behave.html#cmdoption-f

**Format Options**
```cmd
behave --help

behave --format help
    Available formatters:
      json           JSON dump of test run
      json.pretty    JSON dump of test run (human readable)
      null           Provides formatter that does not output anything.
      plain          Very basic formatter with maximum compatibility
      pretty         Standard colourised pretty formatter
      progress       Shows dotted progress for each executed scenario.
      progress2      Shows dotted progress for each executed step.
      progress3      Shows detailed progress for each step of a scenario.
      rerun          Emits scenario file locations of failing scenarios
      sphinx.steps   Generate sphinx-based documentation for step definitions.
      steps          Shows step definitions (step implementations).
      steps.catalog  Shows non-technical documentation for step definitions.
      steps.doc      Shows documentation for step definitions.
      steps.usage    Shows how step definitions are used by steps.
      tags           Shows tags (and how often they are used).
      tags.location  Shows tags and the location where they are used.
```
#### Allure Report
https://allurereport.org/docs/install-for-windows/#install-from-an-archive

```cmd
allure --version
    2.32.0

allure serve allure-results
    http://10.39.101.8:64297/index.html
```

### Reports for Junit Compatible xml
```cmd
behave examples\report_generation --no-capture --no-logcapture --junit
// reports folder will be created

behave examples\report_generation --no-capture --no-logcapture --junit --junit-directory=reports_my_junit
```

### Reports for Json Pretty
```cmd
behave examples\report_generation --no-capture --no-logcapture --format=json.pretty
behave examples\report_generation --no-capture --no-logcapture --format=json.pretty --outfile=reports_my_json\my_report.json
```

### Reports for Allure

1. Install Allure
    https://allurereport.org/docs/install/

2. Install Allure Behave
    https://pypi.org/project/allure-behave/

3. Quick Start DEMO

```cmd
where allure
pip install allure-behave

behave examples\report_generation --no-capture --no-logcapture -f allure_behave.formatter:AllureFormatter -o reports_my_allure
allure serve reports_my_allure
```

### Custom Reports
```cmd
behave examples\report_generation --no-capture --no-logcapture -f json.pretty -o reports_my_json\my_custom_reports.json
python examples\report_generation\custom_report_generator\report_generator.py
    usage: report_generator.py [-h] --input_json_file INPUT_JSON_FILE --output_html_file OUTPUT_HTML_FILE
    report_generator.py: error: the following arguments are required: --input_json_file, --output_html_file
    
python examples\report_generation\custom_report_generator\report_generator.py --input_json_file=reports_my_json\my_custom_reports.json --output_html_file=reports_my_json\my_custom_reports.html
```

// AI Revised
```cmd
python examples\report_generation\custom_report_generator\report_generator1.py --input_json_file=reports_my_json\my_custom_reports.json --output_html_file=reports_my_json\my_custom_reports2.html
```

## Other features

### Calling Steps in step
```code snippet
context.execute_steps("""
    ...
""")
```

```code snippet
@given("I fill in the registration form and submit")
def fill_in_registration_form_and_submit(context):

    context.execute_steps("""
        Given I go to registration page
        When I fill in the form
        And I click on submit
    """)
```

```cmd
behave examples\running_steps_in_other_steps\registration_smoke.feature --no-capture --no-logcapture
```

### Pass Data from Command Line
```code snippet
@given("I create a new user")
def create_new_user(context):
    """
    Step to create a new user.
    :return:
    """
    print("I am creating a new user")
    print(":) :) :) :) :) :)")
    print("More code would go here")
    # user.user_creator()
    prefix = context.config.userdata.get('prefix') ### Get the prefix from the command line

```
```cmd
behave examples\basic_example\feature_example_1_scenario.feature --no-capture --no-logcapture -D prefix=ct -D username=John -D password=123
REM exit to exit the debugger
REM contunue to continue the execution
REM (Pdb) dir(context.config)
REM (Pdb) context.config.userdata ### 
REM {'prefix': 'ct', 'username': 'John', 'password': '123'}
REM (Pdb) context.config.userdata['prefix']
REM 'ct'

```
### Passing a Long String (Object) to a Step Definition
```code snippet
  // Feature File
  Then I another a passing step
    """
    {"first_name": "Admas", "last_name": "Kinfu",
    "phone": "4081111111"}
    """
  // Step Definition
    @step("I another a passing step")
    def i_another_a_passing_step(context):
        print("Another PASSING 1")
        print("Another PASSING 2")
        print("Another PASSING 3")
    
        my_json = json.loads(context.text)
        print(f"✅ Context text Json: {my_json}")
        print(f"✅ First name: {my_json['first_name']}")

```

```cmd
behave examples\other\my_feature_1.feature --no-capture
REM context.text
REM context.text.strip()
REM continue
```

### How to Exclude Features Test by Regular Expression PATTERN
```cmd
behave examples\other -e ".*1\.feature"
behave examples\other -e ".*3\.feature" -t ~f1s1
behave examples\other -e ".*3\.feature" -t ~f1s1 --no-capture

behave examples\other -e ".*smoke.*\.feature"
behave examples\other -e ".*smoke.*\.feature" -t ~f1s1
behave examples\other -e ".*smoke.*\.feature" -t ~f1s1 --no-capture
```

### Rerun Failed Scenarios -f rerun (too complex)
```cmd
cd examples\other
del rerun_fails.feature && behave -f rerun -o rerun_fails.feature
REM continue
REM continue

behave @rerun_fails.feature && del rerun_fails.feature
del rerun_fails.feature && behave
cd ..\..
```

### Stop Execution at First Failure --stop
```cmd
behave examples\other --no-capture --no-logcapture --stop
    ...
    0 features passed, 1 failed, 0 skipped, 3 untested
    1 scenario passed, 1 failed, 0 skipped, 6 untested
    3 steps passed, 1 failed, 2 skipped, 0 undefined, 12 untested

```

### Run without Running --dry-run
```cmd
behave examples\other --no-capture --no-logcapture --dry-run
    ...
    0 Features passed, 0 failed, 0 skipped, 4 untested
    0 Scenarios passed, 0 failed, 0 skipped, 8 untested
    0 Steps passed, 0 failed, 0 skipped, 0 undefined, 18 untested
    
behave examples\other --no-capture --no-logcapture
    ...
    2 features passed, 2 failed, 0 skipped
    6 scenarios passed, 2 failed, 0 skipped
    14 steps passed, 2 failed, 2 skipped, 0 undefined

```

## Runner Script

### Runner Python Script to Run Tests
```cmd
python examples\other\runner.py --test_dir=examples\other
    ✅ Running command:
    behave -k --no-capture -f json.pretty -o "C:\Users\samfi\PycharmProjects\BDD_Python_Course\examples\other\results_20250217193130\json_report_out.json" --junit --junit-directory "C:\Users\samfi\PycharmProjects\BDD_Python_Course\examples\other\results_20250217193130\junit_report_out"  examples\other
    Return code: 1

REM Custom Reports
python examples\report_generation\custom_report_generator\report_generator1.py --input_json_file=examples\other\results_20250217175517\json_report_out.json --output_html_file=reports_my_json\my_custom_reports2.html
```

### Runner Python Script to Run Tests with Tags
```cmd
python examples\other\runner.py --test_dir=examples\other --behave_options="-t f1s1"

    unique_run_id
        '20250218133637'
    os.environ['UNIQUE_RUN_ID']
        '20250218133637'
    continue

    ✅ Running command:
    behave -k --no-capture -f json.pretty -o "C:\Users\samfi\PycharmProjects\BDD_Python_Course\examples\other\results_20250218133637\json_report_out.json" --junit --junit-directory "C:\Users\samfi\PycharmProjects\BDD_Python_Course\examples\other\results_20250218133637\junit_report_out" -t f1s1 examples\other
    Return code: 1
```

## BDD Practice Section

### Introduction
- TESTID (Test Case ID, not in order)
- Front End (FE), Back End (BE)

### Prepare the BDDPractice Project
Copy files from practical_examples to BDDPractice
- properties.ini
- BDDCommon\CommonConfigs\configurations.py
- tests\python_main_site\environment.py

### TCID-10-1 (FE) Valid user should be able to login (Framework Setup)

BDDCommon folder structure
```cmd
- CommonAPI
- CommonConfigs
- CommonDAO
- CommonFuncs
- CommonHelpers
- CommonSteps
```

Main Steps
```cmd
tests\steps\main_steps.py
    from BDDCommon.CommonSteps import webstepscommon
    from frontend.MyAccountPage.steps import my_account_steps
    from frontend.HomePage.steps import home_page_steps
    from frontend.CartPage.steps import cart_page_steps
    from frontend.CheckoutPage.steps import checkout_page_steps
    from frontend.OrderReceivedPage.steps import order_received_page_steps
    from BDDCommon.CommonSteps import products_api_steps
    from BDDCommon.CommonSteps import user_api_steps
    from BDDCommon.CommonSteps import order_api_steps
    from BDDCommon.CommonSteps import coupons_api_steps
```
Url Config
```cmd
- BDDCommon\CommonConfigs\urlconfig.py
   
    URLCONFIG = {
    ...
        'base_url': 'http://mylocalwp.local/',
        'my account': '/my-account'
    ...
```

```cmd
cd BDDPractice
pip install -r requirements.txt
pip install .

behave tests\frontend\MyAccountPage --no-capture --no-logcapture -t TCID-10 
```

### TCID-11 (FE) User with wrong password should get correct error message

```cmd
behave tests\frontend\MyAccountPage --no-capture --no-logcapture -t TCID-11
```

### TCID-12 (FE) User with none-existing email should get correct error message

```cmd
behave tests\frontend\MyAccountPage --no-capture --no-logcapture -t TCID-12
```

### Backend Helper - http GET method
https://woocommerce.github.io/woocommerce-rest-api-docs/#introduction
// Using properties.ini and get_config() method
wooRequestHelpers.py

```cmd
python BDDCommon\CommonHelpers\wooRequestHelpers.py
```

### Backend Helper - http POST method
```cmd
python BDDCommon\CommonHelpers\wooRequestHelpers.py
```
### Backend Helper - Database Helper
dbHelpers.py

```cmd
python BDDCommon\CommonHelpers\dbHelpers.py
    ✅ MySQL connection successful!

```

### TCID-24-1 (BE) Verify 'GET /products' returns all products

```cmd
@TCID-24
Scenario: Verify 'get all products' returns the expected number of products

    Given I get number of available products from db
    When I get number of available products from api
    Then the total number of products in api should be same as in db
```

```notes
Step definition from BDDCommon\CommonSteps\products_api_steps.py
DAO from BDDCommon\CommonDAO\productsDAO.py
```

```cmd
pip install .
behave tests\backend\products\ --no-capture --no-logcapture -t TCID-24
```

### TCID-25 (BE) Verify 'products/id' returns a product with the given id
```note
- Step definition
    BDDCommon\CommonSteps\products_api_steps.py
        ...
        from BDDCommon.CommonDAO.productsDAO import ProductsDAO
        from BDDCommon.CommonAPI import products_api
        ...
    
    BDDCommon\CommonDAO\productsDAO.py
    SQL => 
        SELECT * FROM local.wp_posts WHERE post_type = 'product' ORDER BY RAND() LIMIT 1; # Performance issue;
        SELECT * FROM local.wp_posts WHERE post_type = 'product' ORDER BY id DESC LIMIT 5000; # Randomly by python;
    
```

```cmd
behave tests\backend\products\ --no-capture --no-logcapture -t TCID-25
```

### TCID-29-1 (BE) Verify 'POST /customers' creates user via API then DB
```note
- Feature file
  Given I generate random email and password
  When I call 'create customer' api
  Then customer should be created
- Step definition
    BDDCommon\CommonSteps\user_api_steps.py
    BDDCommon\CommonDAO\userDAO.py
```

```cmd
behave tests\backend\users\ --no-capture --no-logcapture -t TCID-29
```

### TCID-33-1 (FE) New user place order with 1 item without creating account
```note
- Feature file
  order_placement.feature
  
- Step definition
    frontend\CartPage\steps\cart_api_steps.py
    
```

```cmd
behave tests\frontend\EndToEnd --no-capture --no-logcapture -t TCID-33
```
