[Link to the live project](https://ip-flask-easy-cooking-project.herokuapp.com/)


# Easy Cooking - Third Milestone Project

Easy cooking is an app that allows its users to save, edit and share recipes with other users.


## User Experience (UX)

### Project Goals

The primary Project Goal is to create an online cookbook.

The target audience are people who want to store their recipes online or are just looking for cooking ideas.

### User Stories

* As a user I want to be able to
    * to easily navigate throughout the site to find content.
    * view all recipes without the need to login to get new cooking ideas.
    * view detailed description of each recipe item I select.
    * create a user account and be able to use my username and password to login into the application.
    * create, edit, view or delete my recipes on loging in to the application.

* As admin user I want to be able to
    * create, edit, view or delete categories on loging in to the application.

### Design choices

I used [Materialize](https://materializecss.com) UI component library created and designed by Google to construct the web page. 

### Wireframes

Wireframes are available [here ](https://github.com/ip69719/ms-project-3-v2/tree/main/documents/wireframes)

## Features

### All pages

* All pages have **Navigation Bar** which was created using [Materialize](https://materializecss.com) nav bar component. 
* The **Mobile Collapse Button** will appear on smaller screens. The navigation bar will show as a sidebar when the button is clicked.

### login.html
* The login page has an input form where the users will be required to enter their username and password.
* New users can click on the link "Register here" to get redirected to the register page.

### register.html
* New users will have to register using the input form to be able to save their recipes.
* User passwords are hashed to be store them securely in MongoDB.
* Already registered users can click on the link "Login here" to get redirected to the login page.

### Logout
* The user can log out of the application by clicking on logout link on the navigation bar.

### recipes.html
* This is the home page where the carousel with all the recipes is displayed.
* By clicking on the image or on the "Review Recipe" link the user will be redirected to the "recipe details" page where all the details of the recipe can be found.

### recipe_details.html
* This page will display the main attributes for the selected recipe.
* If the recipe belongs to the user then there will be delete or edit the recipe buttons available on the page.
    * Delete Recipe button will only be visible if the recipe belongs to the user. The user will be able to remove the recipe from the database.
    * Edit Recipe button will only be visible if the recipe belongs to the user. The user to The user will be redirected the edit recipe page.

### add_recipe.html/edit_recipe.html
* Add Recipe and Edit Recipe pages are used by the user to enter a new recipe or to edit an existing one.
* The page contains a form with different input types. This **Text Inputs** form was taken from [Materialize](https://materializecss.com).
* By clicking Add Recipe button the form on the add recipe page will be submitted and the recipe will be inserted into the database. The user is then redirected to the home page.
* By clicking Edit Recipe button the user is redirected to the edit recipe page where an existing recipe can be updated.
* The form on the edit recipe page will be submitted by clicking on Save Change button and the recipe will be updated on the database.
* By clicking Cancel button on the edit recipe page the user is redirected to the home page. No changes will be saved.

### Manage categories
* Manage categories page is where meal types can be maintained. This option on the main menu is only visible to the admin user.
* By clicking Add Category button the admin user will redirected to add category form.
* The form will be submitted by clicking the Add Category button and the new category will be inserted into the database.
* The admin user will also be able to update or delete an existing category by clicking on the respective buttons on the manage categories page.

## Features Left to Implement
* User's profile page to display recipes that have been aded by the user
* Adding filter options on the homepage to only display the recipes that meet selected criteria.

## Technologies used

### Database

* [MongoDB](https://www.mongodb.com/) is used to store data.

### Languages used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) used to create the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) used to style the website
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) used to created logic of the website.
* [Jinja](https://en.wikipedia.org/wiki/Jinja_(template_engine)) used for template inheritance, loops and if statements in the html files.


### Frameworks, Libraries & Programs Used

* [Google Developer Tools](https://developer.chrome.com/docs/devtools/) was used for testing responsiveness of the website.

* [Git](https://git-scm.com/) was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

* [GitHub](https://github.com/) is used to store the projects code after being pushed from Git.

* [jQuery](https://jquery.com/) is required for the Materialize JavaScript components to function.

* This project was created using [Flask](https://en.wikipedia.org/wiki/Flask_(web_framework)) web framework.

* [Materialize](https://materializecss.com/getting-started.html)

* [Balsamiq Wireframes](https://balsamiq.com/) was used to create wireframes for the project.


## Testing

### Code Validation

* The W3C Markup Validator and W3C CSS Validator Services were used to validate the project to ensure there were no syntax errors.

    * W3C Markup Validator - [Results](https://github.com/ip69719/ms-project-3-v2/tree/main/templates/documents/testing/w3c_markup_validator)

    * W3C CSS Validator - [Results](https://github.com/ip69719/ms-project-3-v2/tree/main/templates/documents/testing/w3c_css_validation)

### User Story testing

* **As a user I want to be able to easily navigate throughout the site to find content.**
    * All pages have navigation bar allowing the User to easily get access to relevant section of the page. The navigation bar on smaller devices show as a sidebar when the Mobile Collapse Button button is clicked.
    * Navigation and other internal links were tested to confirm that User is directed to the relevent pages when any of the links is clicked.

* **As a user I want to be able to view all recipes without the need to login to get new cooking ideas.**
    * All the recipes are displayed on the carousel on the home page.

* **As a user I want to be able to view detailed description of each recipe item I select.**
    * By clicking on the image or on the "Review Recipe" link on the home page the user is redirected to the "recipe details" page where all the details of the recipe are found.

* **As a user I want to be able to create a user account and be able to use my username and password to login into the application.**
    * By clicking on the login navbar link the user is presented with a log in form where the user can enter their username and password.
    * New users can register by clicking on the link "Register here" on the login page. Alternatively, the user can click on the Register navbar link on the main manu.
    * Confirmed that a new User can successfully register, Flash message is displayed confirming the sucessfull registration and a new record is created in the database
    * Confirmed that an existing User can successfully log in to application by clicking on the login button after inputting credentials into username and password fields.

* **As a user I want to be able to create, edit, view or delete my recipes on loging in to the application.**
    * Confirmed that a User can fill out the "Add Recipe" form and submit data inputs. Validated that a new record was successfully inserted to database.
    * Confirmed that a User can fill out the "Edit Recipe" form and submit data inputs. Validated that the existing record was successfully updated in the database.
    * Confirmed that a User can delete own recipe. Validated that the existing record was successfully removed from the database.

* **As admin user I want to be able to create, edit, view or delete categories on loging in to the application**
    * Confirmed that the manage category option on the main menu is only visible to the admin user.
    * Confirmed that admin User can fill out the "Add category" form and submit data inputs. Validated that a new record was successfully inserted to database.
    * Confirmed that admin User can fill out the "Edit category" form and submit data inputs. Validated that the existing record was successfully updated in the database.
    * Confirmed that admin User can delete a category item. Validated that the existing record is successfully removed from the database.

* Known Bugs
    * Add recipe and Edit recipe pages do not display properly on smaller screens. Changes to html structure of both pages are required in order to resolve this.
    * Ingredients and cooking Method are not displayed properly as unordered/ordered list items. 
    * There is no cancel button available to the admin on the manage categories page. If the user wants to exit the form then the user needs to use the navigation link.


## Deployment

### Heroku

The project was deployed to Heroku using the following steps:

1. Log in to Heroku
1. Click New in the top right corner and select "Create a New App"
1. Gave the app a name and select the closest region, then click 'Create App
1. Setup Automatic Deployment from GitHub repository:
    1. Go to "Deploy" tab and scroll to the “Deployment method” section
    1. Click on "GitHub"
    1. Ensure the correct GitHub profile is displayed
    1. Locate the [GitHub Repository](https://github.com/ip69719/ms_project_3) then click "Connect"
    1. Go to "Settings" tab, then click on "Reveal Config Vars"
    1. Configure variables for IP, PORT, SECRET_KEY and MONGO_URI and MONGO_DBNAME
    1. Go back to the "Deploy" tab, scroll down to "Automatic deploys" section and click on "Enable Automatic Deploys"
1. In "Deploy" tab scroll down to "Manual deploy" section, select main branch and click on "Deploy Branch"
1. Click "View" to launch the app.

## Credits

### Content

* Content of READ.md was written with reference to [Example README.md template](https://github.com/Code-Institute-Solutions/SampleREADME).

### Media

* Images were sourced from [Shutterstock](https://www.shutterstock.com/home) and [Imgur](https://imgur.com/).

### Code

* Used Code Institute Backend Development Mini Project tutorial as a reference to implement project idea.
* Learned about CSS visibility property from this [W3 schools](https://www.w3schools.com/CSSref/pr_class_visibility.asp) post.

### Acknowledgements

* Special thanks to my Mentor for support and guidance and to Code Institute for exellent leaning materials.