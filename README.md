# Django: Employee Management System
## Go to Directory
1) cd CRUD/

## Create virtual environment for django project
1) pip3 install virtualenv
2) virtualenv env
3) source env/bin/activate

## Django installation steps
1) pip3 install django==3.2.13

## To create file for dependency.
1) pip3 freeze > requirements.txt

## To install all dependency
1) pip install -r requirements.txt

## Go to Directory
1) cd crud_practice/

## Migration Steps
1) python manage.py makemigrations
2) python manage.py migrate

## copy static files to assest folder
1) python manage.py collectstatic

## Run Project
1) python manage.py runserver
OR 
2) python manage.py runserver <ip_address>:<port_number>
  - e.g: python manage.py runserver 192.168.1.120:8000   
