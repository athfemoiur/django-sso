# DJANGO SSO AUTHENTICATION

This is a django web application with the feature of sso auth using Google API

## Features
Google SSO authentication



## Installation

First clone the project

```bash
git clone https://github.com/athfemoiur/django-sso.git
```
For this project you need to have postgres-server installed.

First use psql to create a new user if you don't have already then create a new database ( remember this information , we need them later)

We need a virtual environment you can create like this : 

```bash
virtualenv venv
```
Then activate it
```bash
source venv/bin/activate
```
Now install all the packages in requirements.txt file in project directory 
```bash
pip install -r requirements.txt
```
Now You must create .env file in the project dir and fill the variables according to .env-sample file


Then you should have a superuser for accessing the admin panel 
```bash
python manage.py createsuperuser
```
Then migrating 
```bash
python manage.py migrate
```
That's finished now you can run the project , I hope so actually :)

```bash
python manage.py runserver
```
