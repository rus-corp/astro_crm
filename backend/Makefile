run:
	python manage.py runserver

mm:
	python manage.py makemigrations

mi:
	python manage.py migrate

new_apps:
	python manage.py startapp "$(c)"

drop:
	dropdb -U postgres astro

create:
	createdb -U postgres astro

superuser:
	python manage.py createsuperuser