![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Introduction
This web is a a chance for people who love books to share their favorites. The idea is not for people to create an extensive catalog of their library (although they may). Rather, it is for people to share from one to fifteen books from their shelf and have others be able to see and comment on what they read. There are 
many sites such as Goodreads where book lovers can discuss books. However, the website is rather slow, the search is poor, and the user interface is rather 
clunky. 

This site will allow people to sign in, share the books that they're interested in (called a shelf), and see what other people are reading. Users can comment
on books and like them. The whole idea is to get inspiration from other readers as to what books are out there.

## User Stories

As a adminstrator, I can login with privileges so that moderate all content on the site.
As a new user, I can create an account with a user name and password, so that I can log in to access content.
As a user, I can login with a user name and password, so that I can access the content of the site.


As a user, I can see a list of books so that I can get inspiration as to what I want to read next.

# Features

## Admin Panel
There is an admin panel which users with the correct privilefes (superusers), can see and manipulate all of the data in the site.
> As a adminstrator, I can login with privileges so that moderate all content on the site.

## allauth authentication
When the user navigates to the site, they are given a chance to login if they already have an account and to sign up if they do not.
After successful account creation or login attempt, they are taken to the home screen. If they log out, they are taken back to the login screen.
> As a new user, I can create an account with a user name and password, so that I can log in to access content.  
> As a user, I can login with a user name and password, so that I can access the content of the site.

## Home Page
On the home page, a logged in user will see a list of all the books in the database. 
> As a user, I can see a list of books so that I can get inspiration as to what I want to read next.

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

## Model Creation Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Model tables in Admin Panel|When I log into the admin panel as a superuser <br> I can see tables for Users, Book|PASS|

## User Login Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|allauth installation|When I enter accounts/signup as the url in the site <br> I am taken to the allauth signup screen|PASS|
|allauth user  creation|When I go the signup screen, and enter a user name and password, and press signup , my account is created and I am redirected to home screen| PASS|
|user creation verification|When I login to the admin panel, the new user is visible in the user table.| PASS|
|content display after login|When I login successfully, the homepage is displayed|PASS|
|redirect if not authenticated|When I navigate to the site <br> and I am not authenticated <br> I am taken to the login screen| PASS|
|redirect after sign up|When I successfully create an account <br> The site content is displayed| PASS|
|redirect after logout|Wheb I successfully logout <br> I am taken to the login screen|PASS|

## CRUD for Book Objects Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|list of books displayed on homepage|As a logged in user <br> when I am on the home screen <br> all of the books in the database are displayed|PASS|

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
