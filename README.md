# Bank security console
This is script for site which is bank security console with remote access for visitors database of bank vault.

## How to install

For working with this project, you have to copy all files in the working directory at your choice.  Create in working 
directory subdirectory "venv" and file ".env" in this subdirectory. In this file, you have to write 7 lines like this:
```python
ENGINE='django.db.backends.postgresql_psycopg2'
HOST='forexample.example.org'
PORT='5400'
NAME='checkexample'
USER='foruserexample'
PASSWORD='example'
ALLOWED_HOSTS=['localhost', '127.0.0.1', 'my.example.org']
DEBUG=True
SECRET_KEY='EXAMPLE'
```
(presented values are not correct, it's just for example). 
>Note: 
The first six lines are settings for database.
DEBUG has to take just boolean values (`True`/`False`).
SECRET_KEY is secret key for site.
Variables ALLOWED_HOSTS, DEBUG and SECRET_KEY have default settings. 

Python3 should already be installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```python
pip install -r requirements.txt
```
Then, in command line you have to input:
```python
python manage.py runserver
```
After that, you have to press for a pop-up link. If you've been redirected to the bank security console, 
it means all is good.

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
