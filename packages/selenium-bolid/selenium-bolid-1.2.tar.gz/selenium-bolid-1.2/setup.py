from setuptools import setup

setup(name='selenium-bolid',
      version='1.2',
      description='Mtehods distributions',
      packages=['selenium-bolid'],
      install_requires=["selenium", "pytest", "allure-pytest", "pytest-rerunfailures", "mimesis", "jsonpickle", "requests"],
      author_email='gorelov2895@yandex.ru',
      zip_safe=False)
