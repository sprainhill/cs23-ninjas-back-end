release: python manage.py migrate && python manage.py loaddata ./fixtures/generated_world.json

web: gunicorn adv_project.wsgi:application --log-file -