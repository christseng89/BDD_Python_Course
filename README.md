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