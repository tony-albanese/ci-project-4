# Test Tables
## Initial Setup Testing
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Test django installation| When I run the django server, <br> and open the browser with the address, <br> the default django landing page is shown| PASS|
|Test basic routing|When I run the server <br> and enter the hello/ endpoint <br> "Hello world" is displayed| PASS|
|Test static template| When I run the server <br>  and enter hello-template/ as the endpoint <br> I see the contents of hello_template.html displayed|PASS|
|Test static css loaded|When I run the server <br>  and enter hello-template/ as the endpoint <br> I see the contents of hello_template.html displayed with blanchedalmond background color and h1 as blue font |PASS|
|Test admin site login|When I run the server <br> and enter /admin as the endpoint <br>  and login with admin username and password <br>  the default django admin page is loaded| PASS|
|Test Heroku deployment|After deploying to Heroku <br> and loading the /hello and /hello-template/ endpoints <br> The site content displayed is identical to the local version| PASS|
|Heroku admin login|When I navigate to the /admin endpoint in heroku, <br> and login with admin username <br> The admin panel is loaded| PASS|
|Admin Heroku Deployment|When I navigate to the /admin endpoint in heroku, <br> and login with admin username <br> The admin panel looks identical to the local version |PASS|

## Model Creation Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Model tables in Admin Panel|When I log into the admin panel as a superuser <br> I can see tables for Users, Book|PASS|

## User Login Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|allauth installation|As a user <br> when I enter accounts/signup as the url in the site <br> I am taken to the allauth signup screen|PASS|
|allauth user  creation|When I go the signup screen, and enter a user name and password, and press signup , my account is created and I am redirected to home screen| PASS|
|user creation verification|As a user <br> when I login to the admin panel, the new user is visible in the user table.| PASS|
|content display after login|As a user <br> when I login successfully, the homepage is displayed|PASS|
|redirect if not authenticated|As a user <br>when I navigate to the site <br> and I am not authenticated <br> I am taken to the login screen| PASS|
|redirect after sign up|As a user <br>when I successfully create an account <br> The site content is displayed| PASS|
|redirect after logout|As a user <br>when I successfully logout <br> I am taken to the login screen|PASS|

## CRUD for Book Objects Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|list of books displayed on homepage|As a logged in user <br> when I am on the home screen <br> all of the books in the database are displayed|PASS|
|add book form|As a logged in user <br> when i click on Add Book link <br> and fill in fields and submit forms <br> The added book shows up in the list on the home page. |PASS|
|delete book link |As a logged in user <br> when I click on the delete book link <br> the book is removed from the list| PASS |
|list of comments is displayed| As a logged in user <br> when I click on View Comments <br> I am taken to the details page where book details and comments displayed.| PASS|
|update book link navigation|As a logged in user <br> when I click on the edit book link <br> A page with a form pre-populated with the book's details is displayed|PASS|
|updated data submission|As a logged in user <br> When I press the "Update Book" button on the edit page <br> I am taken to the home page and the updated fields are reflected in the list.|PASS|
|Add a comment|As a logged in user <br> when I have entered a comment <br> and press submit <br> my comment is saved and is displayed in the list comments|PASS|
|Delete/modify own content|As a logged in user <br> when I am on the home page <br> I see links to edit / delete books only for entries I have submitted| PASS|
|My Books Page|As a logged in user <br> when I navigate to the My Books page <br> I see a list of only the books that I have added. |PASS|
|Favorites Page|As a logged in user <br> when I navigate to the Favorites page <br> I see a list of the books that I have liked| PASS|
|Username as link in post|As a logged in user <br> When I look at each book post <br> the other users' names appear as a link |PASS|
|Links to user posts|As a logged in user <br> when I click on the user name link in a post <br> All of the posts by that user are shown|PASS|

## Delete Comment Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Modify own comment|As a logged in user <br> When I look at the comments for a book <br> I only see icons to delete or edit a comment <br> if I am the one that created the comment.|PASS|
|Confirmation of Delete|As a logged in user <br> When I click on the trash icon to delete a comment <br> A dialog asking me to confirm my choice is shown. |PASS|
|Delete Works|As a logged in user <br> When I click on the trash icon to delete a comment <br> And I press the Delete button <br> The comment is deleted <br> and is no longer visible in the comments list|PASS|
|Cancel Button Works|As a logged in user <br> When I click on the trash icon to delete a comment <br> And I press the Cancel button <br> The dialog is dismissed <br> the comment is still visible|PASS|
|Delete Someone Else's Comment|As a logged in user <br> When I enter the delete_comment/ url in the search bar with the id of a comment that is not mine <br> an error message saying "Comment Cannot Be Deleted." is shown <br> And I am redirected back to the book detail page|PASS|

## Edit Comment Tests 
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Modal is pre-populated | As a logged in user <br> When I click on the edit button for a comment <br> a modal form appears with my comment text in it.|PASS|
|Comment is updated|As a logged in user <br> When I click on the edit button for a comment <br> And modify the contents <br> and click Update Comment <br> I am redirected to the current book page <br> my updated comment appears|PASS|

## User Likes
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Total likes displayed|As a logged in user <br> the total likes for each book is displayed| PASS|
|Link to unlike| As logged in user <br> If I have liked a book, a link to unlike the book is displayed | PASS|
|Link to like|As logged in user <br> If I have not liked a book, a link to like the book is displayed| PASS|

## Alerts 
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Successfully add book alert| As a logged in user <br> When I successfully add a book <br> An alert is shown under the nav bar telling me. |PASS|
|Successfully edit book alert|As a logged in user <br> When I successfully edit a book <br> An alert is shown under the nav bar telling me.|PASS|
|Successfully add comment alert|As a logged in user <br> When I successfully add a comment <br> An alert is shown under the nav bar telling me.|PASS|
|Successfully sign in alert|As a logged in user <br> When I successfully sign in <br> An alert is shown under the nav bar telling me.|PASS|
|Successfully sign out alert|As a logged in user <br> When I successfully sign out <br> An alert is shown under the nav bar telling me.|PASS|
|Successfully create account alert|As a logged in user <br> When I successfully create an account <br> An alert is shown under the nav bar telling me.|PASS|
|Alert auto dismiss|After the alert is shown <br> The alert dismisses itself.|PASS|


## Search and Filtering Tests
| Test Description              | Test | Result |
|-------------------------------|------------------------------------------|--------|
|Modal Form Loads|As a logged in user <br> when I click on the magnifying glass  <br> a modal form appears. |PASS|
|Modal Form Dismissal|As a logged in user <br> when I load the modal form <br> and click the Close button  <br> the modal form disappears |PASS|
|Filter by Genre|As a logged in user <br> when I select one or several genres <br> and click on the Search button <br> A page showing all books whose genre I have selected loads.|PASS|
|Search by Author|As a logged in user <br> when I enter a name in the Author field <br> and click the Search Button <br> A page listing the books whose author contain any of the entered terms is loaded. |PASS|
|Search by Title|As a logged in user <br> when I enter text in the Title field <br> and click the Search Button <br> A page listing the books whose Title contains any of the entered terms is loaded.|PASS|
|Search by Description|As a logged in user<br> when I enter text in the description field <br> and click the Search Button <br> A page listing the books whose Description contains any of the entered terms is loaded.|PASS|