# Join API
 This is an API written with Django 5.1.
 
 A user can register and login. With the login of a user, a few contacts will be created. These contacts are only for testing the app.
 The user create, edit and delete contacts.
 The user create, edit and delete tasks and subtasks.

### Requirements
You have to install the latest Python version on your computer.
https://www.python.org/downloads/

 ## Installation
 1. Clone this repository
 2. Create a virtual environment `python -m venv env`
 3. Activate the virtual environment `"env/Scripts/activate"`
 4. then you can run
    
 ```
 pip install requirements.txt
```
 
 3. Generate the database with command `python manage.py migrate`
 4. Run the command `python manage.py createsuperuser` to have access to the admin page
 5. Run the command `python manage.py runserver` to start the server on your machine

For the full experience the Join Frontend has to be also cloned and started.
https://github.com/RichardPeda/join-frontend
