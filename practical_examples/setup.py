# from distutils.core import setup
from setuptools import setup
setup(name='PythonBDDtutorial',
      version='1.0',
      description='Python BDD Practical Examples',
      author='Admas Kinfu',
      author_email='admaskinfu@gmail.com',
      url='https://www.supersqa.com/',
      packages=[
            'BDDCommon',
            'BDDCommon.CommonFuncs',
            'BDDCommon.CommonSteps',
            'BDDCommon.CommonConfigs'
      ],
     )

