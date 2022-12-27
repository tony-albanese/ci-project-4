![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

## technology used

gunicorn - server to run django on heroku
dj-database-url Use Database URLs in your Django Application.
dj3-cloudinary-storage - Allows use of cloudinary

# Deployment

## Project Creation
+ Cloned CI Repository
+ Initalized GitPod Workspace
+ Installed support libraries
    + django
    + gunicorn
    + dj-database-url
    + dj3-cloudinary storage
+ created requirements.txt
+ Create django project
```
django-admin startproject bookshelf .
```
+ create shelf app and add it to settings.py
+ migrate changes

## Deployment to Heroku
+ Create heroku app
+ setup ElephantSQL Account
+ create env.py
    + import os
    + entry for database URL
    + entry for secret key
+ update settings.py to connect to new database
+ run migrations again
+ check connection though table query in ElephantSQL dashboard