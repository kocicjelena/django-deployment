python manage.py migrate
The migrate command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
https://docs.djangoproject.com/en/4.2/
https://www.youtube.com/watch?v=ZxMB6Njs3ck
python manage.py makemigrations 

python manage.py migrate
python manage.py shell
'
python manage.py createsuperuser
Enter your desired username and press enter.

Username: admin
You will then be prompted for your desired email address:

Email address: admin@example.com
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

Password: **********
Password (again): *********
Superuser created successfully.
Start the development server¶
The Django admin site is activated by default. Let’s start the development server and explore it.

If the server is not running start it like so:

/ 
$ python manage.py runserver