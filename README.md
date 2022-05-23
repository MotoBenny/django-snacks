# LAB - Class 26

## Project: 

Intro to Django

## Author: 

Benjamin Carter

## Links and Resources

JB's instruction 

## Setup

```python
py -m venv .venv
.\.venv\Scripts\activate
pip install django
django-admin startproject snacks_project .
python manage.py migrate
python manage.py runserver
python manage.py startapp snacks
# TUV 
# T - templates
# U - URLs
# V - Views 
```

## Tests

How do you run tests? import SimpleTestCase from django.tests, run: python manage.py test

Any tests of note?

* most tests are just to test that the paths exist
* other tests are looking at what templates are used and which aren't used.
* all tests are passing