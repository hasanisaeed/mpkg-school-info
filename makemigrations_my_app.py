# school_info/makemigrations_my_app.py

from django.core.management import call_command
from boot_my_app import boot_my_app

boot_my_app()

# python manage.py makemigrations my_app
call_command("makemigrations", "my_app")

# python manage.py migrate
call_command("migrate")
