# Outline

## Part 1
- Create parent dir to hold venv and project root
- python3 -m venv venv
- Activate venv
- Install django
- django-admin startproject project
- Navigate into project directory
- Create a GitHub repo for our project
- Add a .gitignore file
- Add a LICENSE
- Add a README
- Check out the structure of project
- Run project
  - python manage.py runserver
      - with args and reloading
- Add items to gitignore if need be
- Commit
- Start an application
  -  django-admin startapp adopt
- Check out structure of app
- Add index view
  - adopt/views.py
  - adopt/urls.py
  - project/urls.py
- Run project
- Add items to gitignore if need be
- Commit

## Part 2
- Talk about databases and why we are going to stick with sqlite for now
- Run migrate
- Add Pet model
- Add adopt/apps.py file
- Add app to INSTALLED_APPS
- Make Migrations
  - python manage.py makemigrations adopt
  - uh, oh. Install Pillow
- View migration before performing it
  - python manage.py sqlmigrate adopt 0001
  - look at migration file in migrations dir
- python manage.py migrate
- Add some records
  - python manage.py shell

	(venv) ➜  project git:(master) ✗ python manage.py shell
	Python 3.7.3 (default, Apr 29 2019, 23:22:45)
	[Clang 10.0.1 (clang-1001.0.46.4)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	(InteractiveConsole)
	>>> from adopt.models import Pet
	>>> from django.utils import timezone
	>>> greg = Pet(
	...   name='Greg',
	...   breed='Leatherback sea turtle',
	...   sex='male',
	...   birth_date=timezone.datetime(2017, 10, 10).date(),
	...   vaccinated=True,
	...   bio='A      great    guy.',
	...   adopt_me_if='You like the color green',
	...   first_thing_people_notice_about_me='My eyes',
	...   friday_night='Surfing the waves',
	... )
	>>> greg.save()

  - Pet.objects.all()
- Create admin user
  - python manage.py createsuperuser
- Go to admin
  - Show user exists but not pets
- Add adopt/admin.py
  - Show pet is unnamed and confusing
- Update model with __str__ method
- Update model in Django admin, image field cause update to fail
  - Must provide a photo
  - Show where photo goes when uploaded, root of repo. That's bad for organization.
  - Remove file and explain that we just corrupted the database, db still thinks file exists
    Not a huge problem, but something to consider for production sites
- Change location of MEDIA_ROOT in settings
  - Add MEDIA_ROOT to .gitignore with placeholder file
  - Reupload file for greg
- Add a few more models in Django Admin
  - As "required fields" errors pop up, remove the need for fields
  - Make migrations
  - migrate
  - Add records

## Part 3
- Write more functional views
- Add views to URLs
- Add views that return data from database
- templates
  - make directory for templates
    - mkdir -p adopt/templates/adopt/
  - render
- Get an object that does not exist
  - raise 404
  - show short cuts
- Update templates to use reverse URLs

## Part 4
- Write a form to adopt a pet
  - Add model
  - Migrate model
  - Write ModelForm
  - Write view
  - Write URLs
  - Write template
  - Add admin page

## Part 5, tests


## Part 6, better static content


## Part 7, Deployment


## Part 8, Clean Up


## Part 9, JSON endpoints


## Part 10, Continuous Deployment
