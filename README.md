# Peanuts collection blog

Based on a fork of pydanny's cookiecutter-django, amended to use Django Rest Framework to power a
blogging platform. This commit includes an articles app and tests files in the articles and users apps.

Getting up and running
----------------------

The steps below will get you up and running with a local development environment. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the requirements for local development::

$ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

You can now run the usual Django ``runserver`` command (replace ``yourapp`` with the name of the directory containing the Django project)::

$ python yourapp/manage.py runserver

Then navigate to localhost:8000 in your browser.

> This application is still in the early stages of development so may not work as expected.
