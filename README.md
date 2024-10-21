Django tutorial
I have created this application for learning the flow of Django in sqlite3 database.
To start with you need to setup the virtual environment using the command
```
python3 -m venv django-env
source django-env/bin/activate
```
After setting up the virtual environment for django, you need to install django. You can see if it is installed using the following command.
```pip show django```
Else you can install it using
```sudo apt install django```
To get a new django project, run the following command
```django-admin startproject mysite django_tutorial```
This will create a directory mysite (which is our project) and a manage.py file which is responsible for executing your application(s) and will look  something like this:
```
djangotutorial/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
By default there are these files in the project. You can create multiple applications in django all at once.<br / >
ldknwkejb

