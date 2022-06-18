# Steps to reproduce working environment:

1 - git clone this repo
2 - python -m venv env (to create new enviornment)
3 - pip install -r requirements.txt (to install dependencies)
4 - Install postgresql and create a database named qanda with the default user postgres (check jimbo/jimbo/settings.py for DATABASES)
5 - test app: cd jimbo & python manage.py runserver
6 - When working with the project, make sure you are always in the directory jimbo/
7 - run python manage.py makemigrations and python manage.py migrate
8 - open browser: http://localhost:8000/ and check if there is a welcoming message
9 - For now there are two routes: / and qa/, use qa/ POST to answer questions and to save them to db, use qa/ GET to see them all
10 - If you have an issue of csrf token and you are working with POSTMAN: https://ourcodeworld.com/articles/read/1619/how-to-handle-postman-and-django-403-forbidden-error-csrf-verification-failed

(not completed)

# Steps to replicate project

1 - create virtual env

2 - install django

3 - start project with boilerplate code

django-admin startproject jimbo

4 - verify by running cd jimbo, python manage.py runserver 8080

5 - make sure that when you are working with django, same level with manage.py

6 - to create a new application in your django project python manage.py startapp scholar

7 - how to make your first view? first create in view.py, then map the view to an url in urls.py in the same application, then map urls.py in the project settings directory (jimbo)

8 - test by going to http://localhost:8080/scholar/

9 - We added a second view to simply mirror the request, to inspect it, to understand it
We got an error, the route path cannot be found, so we installed django-extensions (optional), be careful of parathensis, end with one but don't start with one in your route

10 - add database: we will use postgresql

```
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'ALDIA',
    'USER': 'postgres',
    'PASSWORD': '1234',
    'HOST': '127.0.0.1',
    'PORT': '5432',
    }
}
```

11 - if you face an issue with pip install psycopg2

12 - to test if db is connected and to apply migrations python manage.py migrate (should OK)

13 - Now create your models, development always start from models and expand from them
OH NEED TO STUDY DATABASE DESIGN

14 - add application to INSTALLED_APPS: so the migrations (models) are affected to the db

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'scholar.apps.ScholarConfig'
]

15 - makemigrations and migrate (python manage.py makemigrations scholar)

16 - to check your migrations in sql: python manage.py sqlmigrate scholar 0001

17 - to check if you have any problem with your prokect: python manage.py check

18 - To use interactive django API: python manage.py shell

```
# instructions you can use
from scholar.models import *
Document.objects.all()
from django.utils import timezone; doc = Document(title="first document",text="So what is the name of the owner of the project? It is khaled adrani", pub_date=timezone.now())

doc.save()
doc.id
doc.text = "new text"

```

19 - the str representation is bad for our models, we can improve it by adding dunder method of str to our models

20 - adding custom methods to your models is helpful

https://docs.djangoproject.com/en/4.0/intro/tutorial02/#:~:text=Note%20the%20addition,py%20shell%20again%3A

# for future

-  django-extensions
-  postgres and django
-  database design (progress: relationships design)
