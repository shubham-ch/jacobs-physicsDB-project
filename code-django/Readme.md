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
	
To create project with django in same directory (code-django/)
	django-admin startproject <projectname> .
used,
	django-admin startproject djangoBackend .
	


FOR REACTJS
To create app.
	npx create-react-app <your-app-name>
used,
	npx create-react-app react-web
	
To start the app
	npm start
