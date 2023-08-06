from setuptools import setup

setup(name='selenium_bolid',
      version='1.3',
      description='Mtehods',
      packages=['selenium_bolid'],
      install_requires=["selenium", "pytest", "allure-pytest", "pytest-rerunfailures", "mimesis", "jsonpickle", "requests"],
      author_email='gorelov2895@yandex.ru',
      zip_safe=False)
