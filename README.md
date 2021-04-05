
# Cloud computing mini-project
## Team 8
  - Arshiya Khan
  - Benesh Tobin
  - Koravich
  - Poornima
  - Vickey
  - Surya

# Flask Web App Tutorial
This is a " To do List " application with authentication and CRUD functionality using the Python Flask micro-framework.

-You can take note of your daily routines update and delete your notes through this application

## Contents
 - [Third-Party Extensions]
 - [Setup & Installtion]
 - [Running The App]
 - [Viewing The App]

## [Third-Party Extensions]
     - External api used to get data from: https://www.abstractapi.com/holidays-api
     - We used Heroku to deploy our application.
     - Data Base Credentials
          Please note that these credentials are not permanent.

- Heroku rotates credentials periodically and updates applications where this database is attached.

- Host
- ec2-3-233-43-103.compute-1.amazonaws.com
- Database
 - d5282sjs51hun0
 - User
 - deobefiazugyyy
 - Port
   5432
 - Password
  -c23a9d5d05e18f0eebe6bf69a1d0ecc6bb4900ea2ced4e2d1f14856ade5b16ff
 - URI
   - postgres://deobefiazugyyy:c23a9d5d05e18f0eebe6bf69a1d0ecc6bb4900ea2ced4e2d1f14856ade5b16ff@ec2-3-233-43-103.compute-1.amazonaws.com:5432/d5282sjs51hun0
   - Heroku CLI
   - heroku pg:psql postgresql-silhouetted-15724 --app cc-mini-proj
## Setup & Installtion

To use this template, your computer needs:

- [Python 3](https://python.org)
- [Pip Package Manager](https://pypi.python.org/pypi)

Make sure you have the latest version of Python installed.

The website folder holds the skeleton of the project which inclues template and static folder along with .py files 

```
run main.py file using the below command

python3 main.py
```

Heroku's dynos are just managed runtime containers with a Linux operating system underneath. These containers run the processes that allow your custom application code to run.

```
web gunicorn wsgi:app --preload --workers 1
```
```bash
pip install -r requirements.txt
```


## Running The App

- Deploy using Heroku Git
 --https://devcenter.heroku.com/articles/heroku-cli
- Install the Heroku CLI
- Download and install the Heroku CLI.

If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key.
```
$ heroku login
Clone the repository
Use Git to clone cc-mini-proj's source code to your local machine.

$ heroku git:clone -a cc-mini-proj
$ cd cc-mini-proj
Deploy your changes
Make some changes to the code you just cloned and deploy them to Heroku using Git.
```
- $ git add .
- $ git commit -am "make it better"
- $ git push heroku master

In-order to create database in cloud follow this link:Database-postgressql-https://devcenter.heroku.com/categories/data-management
- Visualize your data with Dashboards, reports, complex SQL queries with simple UI using -https://devcenter.heroku.com/articles/draxlr



## Viewing The App

Go to https://cc-mini-proj.herokuapp.com/
