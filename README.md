Description

This program works with API GITGUB. For example: if you want to know the username or all its repositories, then you need to use API. 
res = requests.get(url.format(login.login)).json()
res_2 = requests.get(url.format(login.login) + '/repos').json()
This way you get a json file and can get the information you are interested in.

INSTALLATION

You still need to install libraries:

''' pip install Django

pip install requests

pip install pylint '''

To get started, you must first install the libraries listed above.
In order to run the project on your computer, you need to clone the project, 
then open it in the development environment and in the API Test directory, 
type the command: python manage.py runserver

Admin panel

In order to enter the admin panel you need to enter your 
login: admin
password: admin

Test

In order to run the tests, you need to write the command: python manage.py test

Linters

In order to run linters, you need to write the pylint name_file.
