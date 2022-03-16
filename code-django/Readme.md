FOR DJANGO

To create a virtual environment using pipenv
python3 -m pip install pipenv --upgrade

To activate virtual environment
pipenv shell

-- dir code-django/

To install django on the virtual environment
pipenv install --python <version> django==<version>

version used,
pipenv install --python 3.8.8 django==2.2

To create project with django in same directory(code-django/)
django-admin startproject <projectname> .
used,
django-admin startproject djangoBackend .

To create a app in django
python manage.py startapp app

To run the app
python3 manage.py runserver

# It's probably easier to just use manage.py instead of django-admin

python3 manage.py <command>

# If you really want to use django-admin, you can try this

export PYTHONPATH=/home/YOUR_NAME/project_path
export DJANGO_SETTINGS_MODULE=my_project.settings
django-admin <command>

FOR REACTJS
To create app.
npx create-react-app <your-app-name>
used,
npx create-react-app react-web
To start the app
npm start
