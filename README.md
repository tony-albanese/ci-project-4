![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Introduction
This web is a a chance for people who love books to share their favorites. The idea is not for people to create an extensive catalog of their library (although they may). Rather, it is for people to share from one to fifteen books from their shelf and have others be able to see and comment on what they read. There are 
many sites such as Goodreads where book lovers can discuss books. However, the website is rather slow, the search is poor, and the user interface is rather 
clunky. 

This site will allow people to sign in, share the books that they're interested in (called a shelf), and see what other people are reading. Users can comment
on books and like them. The whole idea is to get inspiration from other readers as to what books are out there.

## User Stories

As a adminstrator, I can login with privileges so that moderate all content on the site.


# Features

## Admin Panel
There is an admin panel which users with the correct privilefes (superusers), can see and manipulate all of the data in the site.
> As a adminstrator, I can login with privileges so that moderate all content on the site.


# Testing
The testing done here is BDD testing.
## Initial Setup Testing
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
| Test djano installation| When I run the danjo server, <br> and open the webrowser with the address, <br> the default django landing page is shown| PASS|
|Test basic routing|When I run the server <br> and enter the hello/ endpoint <br> "Hello world" is displayed| PASS|
|Test static template| When I run the server <br>  and enter hello-template/ as the endpoint <br> I see the contents of hello_template.html displayed|PASS|
|Test static css loaded|When I run the server <br>  and enter hello-template/ as the endpoint <br> I see the contents of hello_template.html displayed with blanchedalmond background color and h1 as blue font |PASS|
|Test admin site login|When I run the server <br> and enter /admin as the endpoint <br>  and login with admin username and password <br>  the default django admin page is loaded| PASS|
|Test Heroku deployment|After deploying to Heroku <br> and loading the /hello and /hello-template/ endoints <br> The site content displayed is identical to the local version| PASS|
|Heroku admin login|When I navigate to the /admin endpoint in heroku, <br> and login with admin username <br> The admin panel is loaded| PASS|
|Admin Heroku Deployment|When I navigate to the /admin endpoint in heroku, <br> and login with admin username <br> The admin panel looks identical to the local version |FAIL The site loads but there is no styling|


# Deployment

## technology used

gunicorn - server to run django on heroku
dj-database-url Use Database URLs in your Django Application.
dj3-cloudinary-storage - Allows use of cloudinary


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
+ go to heroku dashboard for app
    + click settings
    + add three config vars: DATABASE_URL, SECRET_KEY, and PORT
+ setup cloudinary account (just in case)
+ add CLOUDINARY_URL as os.environ to settings.py
+ add CLOUDINARY_URL as config var to heroku
+ add cloudinary apps to settings.py in INSTALLED_APPS
+ set static file storage variables
+ add template variables
+ create media, static, and templates directories
+ add Procfile
+ connect to github respository
    + deploy from branch
