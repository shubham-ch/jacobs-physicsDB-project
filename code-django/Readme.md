# Physics Homework Database

### About the Project:
The idea of the project is to create a dynamic database of assignments of different undergradaute Physics courses at Jacobs University Bremen (https://www.jacobs-university.de/study/undergraduate/programs/physics). In the initial phase, we create a workable prototybe wherein users can upload  homework files in different formats (.docx, .pdf, .tex, .txt) which are stored on the server. A user can then choose among the exisiting questions to create a new problem set. Each entry in a database is a Physics question with its attrributes defined by the associated Lecture, Field, Difficulty level, Source of the question, Learning outcome, comments, etc. Further functionalities such as control levels by user types (Professors, TAs, students) are to be added in future commits.



### Setup:
With python installed, create and activate virtual environemnt by running the following commands in the directory `/code-django/`

```
pip install virtualenv            (installs virtualenv, may require sudo privilege)
virtualenv env                    (creates a virtual environment 'env' in the working directory)
source env/bin/activate           (activates the virtual environment env)
```

Install the reuqired dependencies by

```
pip install -r requirements.txt
```

To run the program, run

```
python3 manage.py runserver
```

The webpage is then accessible at locathost `http://127.0.0.1:8000/`


### File Structure:

```
  \-- code-django
      \-- app                                   (main django functions implemented in the projec)
          \-- templates
              |-- add_forms.html                (display page to add an entry to database)
              |-- base.html
              |-- database_followup.html        (details of selected entry, preview pdf file)
              |-- database.html                 (display page for the entire database)
              |-- home.html
              |-- navbar.html                   (top menu bar, links to different pages)
              |-- search.html                   (display results of a particular search)
              |-- update_database.html          (Update an entry of database)
  
    \-- djangoBackend                           (Administrative)
    
    \-- media                                   (stores the uploaded files)
    
    \-- react-web                               (frontend codes)
    
    \-- users                                   (django login registration)
    
    |-- db.sqlite3                              (stored database)
    |-- manage.py

```














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
