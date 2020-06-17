# Learning Django

This project will follow much of the same outline of the official Django tutorial.

- Starting a project
- Starting an application
- Adding views and routing

- Models and saving state in a database
- Migrations
- Object / Record collection
- The Django Admin site

- In depth views
  - functional
  - class based views
- Templates

- Forms

- Testing

- Style

- Deployment
    https://cloud.google.com/python/django/appengine
    cloud_sql_proxy -instances="ieor-tools-for-analytics:us-east4:adopt"=tcp:5432
    export GAE_APPLICATION=1
    pip install -r requirements.txt
    source env.sh
    python manage.py migrate

    gcloud init
    gcloud app deploy

sing the Google Cloud SQL
- https://cloud.google.com/sql/docs/postgres/connect-app-engine-standard
- Enable API
- Create CloudSQL instance
- Set permissions on app role
- Download service account key
- collectstatic on local machine
- explain start-env.sh

