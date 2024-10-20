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
<p>By default there are these files in the project. You can create multiple applications in django all at once.<br>
The __init__.py file is used to indicate that this directory should be treated as a python package.<br>
The settings.py file contains all the configuration settings that will dictate how your django application will behave.<br></p>
Key components in settings:
<li><code>DEBUG=True</code> It turns on or off the debug mode in your application. It should be turned off in production mode</li>
<li><code>ALLOWED_HOSTS = [*]</code> It represents list of all allowed hosts</li>



