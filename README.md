# Kitchen Genie

Kitchen Genie is an online tool, bringing friends together to support each other to cook smarter with the goal of saving in in food costs. During the recent Covid-19 pandemic, the average price in food has increased by [3.7% in last 12 months in 2021](https://www.usinflationcalculator.com/inflation/food-inflation-in-the-united-states/). Kitchen Genie makes saving money fun and delicious. Enjoy!

## User Experience (UX)

- ### User stories


  - #### First Time User Goals

  The target audience for this application is for anyone who wants to team up with their friends to save in food costs so they can do something else with their money. 

  User Goals are:

  1. As a First Time User, I want to easily grasp the User Interface. 
  2. As a First Time User, I want to know if this application works before investing my time into it.
  3. As a First Time User, I want to save money in food costs.
  4. As a First Time User, I want to easily share recipes with my friends.
  5. As a First Time User, I want to resolve pandemic isolation and strengthen my friendship bonds.
  6. As a First Time User, I want to feel safe that my user credentials are secure.

  Kitchen Genie is a great way for the First Time User to meet their user goals because:

  1. The application used Bootstrap front-end framework to provide an intuitive design with the user experience as central importance, creating a mobile first design.
  2. The home page provides proof that the application works, displaying user testimonials regarding what they were able to do with the money they saved using Kitchen Genie. 
  3. The user profile page has a personal financial goal option to fill out, to incentivize the User to regular use Kitchen Genie.
  4. The user can tally up food savings cost after reaching their finincial food savings goal then post a testimonial to the site to encourage their comunnity of thrifty friends.
  5. The group recipes page displays all recipes posted by your friends. The user simply logs in and has access to group recipes page and in addition has access to add recipe page consisting mostly of dropdown selection input boxes for the user to enter their own recipe. This dropdown inputs minimize user typing to speed u the process of adding a recipe to the group. 
  6. The app serves as a basis for an online group meetup for making delicious low cost reciptes. Each recipe will inspire more conversation and expand reach within the user's friends group. 
  7. The login and registration data is secure using encryption to store the user's sensitive login credentials.

  ---

  ## Design

  This application has a modern design with subtle splashes of warm fall colors. The site's design simplicity is distraction free, allowing an ease-of-use user experience and promote cheerful social interaction between friends. The following design choices were made with this in mind:

  - ### Fonts

    - The primary font [&#39;Open Sans&#39;](https://fonts.google.com/specimen/Open+Sans#standard-styles) by [Google Fonts](https://fonts.google.com/) was chosen for the main title, subtitle, testimonial posts, and large login/register buttons for it's neutral, friendly, and simple design.
    - The secondary font [&#39;generic Sans-serif&#39;](https://fonts.google.com/?category=Sans+Serif) by [Google Fonts](https://fonts.google.com/) was chosen for the menu buttons, 'about' text, testimonial post dates and names, and login, register and add recipe input field description text because of its wide availability in all browsers and simple design complementing the primary 'Open Sans' font.

  - ### Colors

    - The primary colors are a deep tomatoe red for the background theme color and a gentle gold for the add recipe card. In contrast to the soft red and gold, the primary submit user data buttons are in default bootstrap primary blue color to make it a no brainer for the user to submit their data and to allow the user to jump into using the app as quick as possible.

  - ### Backgrounds

    - The background color was color matched to the deep red color of the tomatoes in the main header photo of warm muted colors of a country French style food serving tray surrounded by popular savory cooking staples of ripe tomatoes, spicy peppers and savory yellow beans. The warm gold and red colors help create a friendly inviting user experience filled with a warm color palette to help increase the user's appetite. 

  - ### Wireframes

    These wireframes were created using [Balsamiq](https://balsamiq.com/) to facilitate a mobile first responsive site design. There are some features in the wireframes that were not included in this first version and are noted in the 'Addtional Features" section within the readme. 

    - Mobile Wire Frame - [View](https://github.com/kashinak/kitchen-genie/blob/main/static/wireframes/Kitchen_Genie_Mobile_wireframes.pdf)
    - Tablet Wire Frame - [View](https://github.com/kashinak/kitchen-genie/blob/main/static/wireframes/Kitchen_Genie_Tablet_Wireframes.pdf)
    - Desktop Wire Frame - [View](https://github.com/kashinak/kitchen-genie/blob/main/static/wireframes/Kitchen_Genie_Desktop_Wireframes.pdf)

  ## Features

  - Basic CRUD mechanisms and MongoDB database access functionality
  - Responsive on all device sizes
  - Mobile collapsible navigation bar button
  - Visually Appealing interactive elements
  - Flash messages to alert the user that their input data is successful such as when they register, log in, log out and add recipes.
  - Flash messages to alert the user that their input data is unsuccessful such as when a user name or passwrod does not exist. 
  - Dropdown menus to speed up and facilitate user data input experience. 
  - Used Font Awesome icon prefixes for better user experience and intuitive layout.
  - Links provided underneath Register and Login submit buttons to easily guide the user to the correct page depending on whether or not they are a registered user.
  - Defensive programming applied to register page using RegEx and minlength, maxlength and required attributes to create secure basic user registration requirements.
  ## Technologies Used

  ---

  - ### Languages Used
  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/CSS)
  - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - [Python3](https://en.wikipedia.org/wiki/Python_%28programming_language%29)
  - [Jinja Template Language](https://en.wikipedia.org/wiki/Jinja_%28template_engine%29)
  

  ### Frameworks, Libraries & Programs Used

  1. [Bootstrap 4.2.1:](https://getbootstrap.com/docs/4.2/getting-started/introduction/)

     - Bootstrap was used to facilitate responsiveness and styling of the application site.
  2. [Start Bootstrap Clean Blog Template:](https://startbootstrap.com/theme/clean-blog)

     - This open source library of free Bootstrap templates and themes; facilitated a mobile first responsive design base. The 'clean-blog' template provided a simplistic modern design. It provided a clean header footer foundation; perfect for applying Flask Jinja templates for all pages of the application. Custom CSS, HTML and Python were later applied to this template; converting a blog site into a cooking recipe site. 
   
  3. [Google Fonts:](https://fonts.google.com/)

     - Google fonts,'Open Sans' and generic 'Sans-serif' fonts were used on the home page title, subtitle, buttons, input field description text, user testimonials, menu items and content description text.
  4. [Font Awesome](https://fontawesome.com/)

     - Font Awesome plus symbol 'fas fa-plus' and minus symbol 'fas fa-minus' were used to design buttons that add and delete user input field within the add_recipe.html page. Icon 'fas fa-plus-square' was used for the submit button for all the user input for add_recipe.html page. Icons for social media links. Also user plus and user lock icons were used for adding username and password to register and log in forms. The icons elevate user input experience by reducing amount of text instructions and guide the user with icons instead. 
  5. [jQuery:](https://jquery.com/)

     - jQuery came with Bootstrap to make the header responsive.
  6. [Git](https://git-scm.com/)

     - Git was used for version control through commits to Git and pushes to Github through the Gitpod terminal.
  7. [GitHub:](https://github.com/)

     - GitHub was used to store the project's code after being pushed from Git.
  8. [Flask](https://flask.palletsprojects.com/en/2.0.x/)

     - Installed this web framework to add functionality of making CRUD calls from Flask app to MongoDB database. 
  9. [Flask-Pymongo](https://flask-pymongo.readthedocs.io/en/latest/)
      
      - Installed this third-party library to get Flask to communicate with Mongo.

  10. [Python's OS Module](https://www.pythonforbeginners.com/os/pythons-os-module)

     - OS allows Python Flask application to set environment variables to store sensitive data and boost security.
  11. [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)

     - This dependency was necessary for Flask to run and used to securely store user credentials. One of the benefits of using Werkzeug with Flask is that it comes with 
     simple to use security features. The two main security helpers used for this apllication are "generate_password_hash" and "check_password_hash".
  12. [Balsamiq](https://balsamiq.com/)

     - Balsamiq was used to create the [wireframes](https://github.com/kashinak/whale-song-memory-game/tree/main/assets/wireframes) during the design process.
  13. [PyMongo](https://pypi.org/project/pymongo/)

  - This package is a native Python driver for MongoDB and contains tools for interacting with MongoDB database from Python. NOTE: DO I need to list this in README.MD? It is just listed in requirements.txt but I never installed it like I did with pip3 for Flask-Pymongo. do I ned to list all the dependencies from requirements.txt in README.md? 
  14. [Dnspython](https://www.dnspython.org/)

     - This package allows for the use of the Mongo SRV connection string.
  15. [BSON](https://en.wikipedia.org/wiki/BSON)

     - This JSON like format is used by MongoDB to store data. For this application, user credentials and recipes is stored in BSON format in MongoDB document based database. In order to find documents within the MongoDB database we need to render the ObjectId.

  16. [Heroku](https://www.heroku.com/)

     - It's necessary that this app is deployed on Heroku because it runs on Python3. The Heroku toolbelt along with the CLI is used to easily deploy and maintain this Flask application.

  17. [MongoDB Atlas](https://www.mongodb.com/)

     - MongoDB Atlas is used to connect Kitchen Genie application and document based database system within MongoDB using a database URL. 

  18. [SASS](https://en.wikipedia.org/wiki/Sass_%28stylesheet_language%29)

     - SASS files included in Start Bootstrap 'clean blog' template for deeper customization options.
  19. [SCSS](https://w3codemasters.in/how-to-use-scss-in-html/)

     - SCSS files included in Start Bootstrap 'clean blog' template for deeper customization options.
  20. [SB Forms](https://startbootstrap.com/solution/contact-forms)

     - SB Forms included in Start Bootstrap 'clean blog' template for easy form setup with the option to add API link 
     to the form which will send all contact messages to Kitchen Genie's central email address.
  21. [Cacoo](https://cacoo.com/)

     - Cacoo was used to draw a simple flow chart to map out the order of Python Flask functionality.
  
   

  ## Testing

  The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

  - [W3C Markup Validator](https://validator.w3.org/nu/#textarea) - [Results](https://github.com/kashinak/whale-song-memory-game/blob/main/assets/validator%20results/nu_html_checker_results.pdf)
  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) - [Results](https://github.com/kashinak/whale-song-memory-game/blob/main/assets/validator%20results/w3c_css_validator_results.pdf)

  ### Testing User Stories from User Experience (UX) Section

  1. Game Controls

     1. The large 'start game' button shown in wireframes was tested but tossed because it was redundant in functionality similar to 'game restart' button developed later. The latter was converted to a 'game start' button and positioned beneath the game board. The new button is highlighted in orange yellow to grab the player's attention to begin the game. This clears up original confusion for the first time player, by the use of only one button to start and restart the game when necessary. The game board design is now cleaner without the original large 'game start' button overlayed on top as originally shown in wireframes.
     2. The 'how-to-play' button was a dropdown card with game instructions and was originally located at the top of the game area beneath the header but the location and design confused the player because it looked like part of the header and not an actual game button. To remedy the player confusion, the game instructions was reduced in size and positioned to the right of the 'start game' button beneath the game board for easy access. It's design is identical to the 'start game' button so the player knows to click on it to show a nifty popover message displaying a short list of game instructions. A dim blue outline was added to the 'how-to-play button so that its design does not compete with the more important 'start game' yellow/orange outlined button.
  2. Game Board

     1. When tested, the first time player encountered game visibilty issues in mobile view. The bootstrap grid applied to the game board, wrapped the game tiles in one single column in mobile view. This type of responsiveness detracted from the quality of the game experience because of having to use scroll bars to play the game on a mobile device. The initial wireframe design of using the identical game layout for all screen types was key to making the game fully functional on mobile, tablet and desktops. Media Queries were added to css to maintain the square game board layout on all device screen sizes.
     2. Original whale sounds were varying length and overlapped while playing, making it confusing for the first time player to identify a singular whale sound unique to each whale. To remedy the audio overlap, whale call raw files were edited down and audio mixed in Adobe Premiere Pro to 1-second durations to help simplify and build momentum during the audio playback game experience.
  3. Score Board

     1. The orignal score board also updated in real time, diplaying the round the player was on and also displyed text indicating whether the player won or lost the game. It was very basic and the player wasn't clear if they had won or lost the game. To make the game more fun and dynamic by notifying the player in a bolder way if they won or lost, a visually beautiful popup results diplay was added and solved this issue. Adding sound effects, a cute whale icon, an animated wave and different messages to notify the player if they had won or lost the game made a huge difference in the player having fun with the game. A third 'great!' button was added so the user can click it to make the results popup window disappear and return to the game board. The orignal score board remains below the game control buttons and still updates in real-time, the round the player is on but now it does no longer display's' a win or lose message.  These feature updates, sound effects, beautiful animation improves user interaction and creates a more engaging user game experience.

  ### Further Testing

  - The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
  - The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
  - Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

  ### Known Bugs

  - Title font:'FishOutOfWater'by [Font Bros](https://www.fontbros.com/) would not load after adding link: @font-face with url for Font Bros to style.css.

    - Bug was squashed by adding WOFF files to Whale Song game site repository directory and update the css code to:

      ```css

       @font-face {
          font-family: 'FishOutOfWater';
          font-weight: normal;
          font-style: normal;
          font-display: swap;
          url("/fonts/FishOutOfWater-Regular.woff") format("woff");
      }

      @font-face {
          font-family: 'FishOutOfWater';
          font-weight: bold;
          font-style: normal;
          font-display: swap;
          url("/fonts/FishOutOfWater-Bold.woff") format("woff");
      }

      @font-face {
          font-family: 'FishOutOfWaterDemiBold';
          font-weight: normal;
          font-style: normal;
          font-display: swap;
          url("/fonts/FishOutOfWater-Demibold.woff") format("woff");
      }



      ```

    #### Bugs to fix in the next version


    - When the site reloads, the game results popup screen covers the game board.
    - Sometimes the game plays several game tiles at the same time after clicking on the 'start game' button.
    - When one game tile is to be played more than once in succession, the game tile only highlights once. Nonetheless it is still easy to play the game.
    - The yellow orange game tile border needs style improvements so that the border is more solid.
    - The win and lose game sound effects do not play on Safari mobile view.
    - Animated wave background will not load when played on Safari, Chrome and Firefox tablet view. It also jerks during playback on desktop device.
    - Player is able to push game board tile buttons prior to hitting 'start game' button and while the game is playing back a sequence.
    - Sometimes whale sounds and flashing tiles play out of synch when playing on tablet devices.

  ### Additional Features to add in the next version

  - Add validation helpers to log in and register input fields such as adding a red outline to inout field when a user has overlooked a required inout field or entered wrong data. 
  - Ability for users to post their experiences and comments using other people's recipes. 
  - Functionality to upload profile photo.
  - 'Forget Password and/or username?" retrieval functionality.

  ## Deployment

  ### Heroku Deployment

  The project was deployed to Heroku using the following steps...

  1. Log in to [GitPodRepository](https://gitpod.com/)
  2. Within oyur repository, create a requirements.txt file using the terminal command pip freeze > requirements.txt.
  3. Create a Procfile with the terminal command echo web: python app.py > Procfile.
  4. git add and git commit the new requirements and Procfile and then git push the project to GitHub.
  5. Create a new app on the [Heroku website](https://www.heroku.com/) by clicking the "New" button in your dashboard. Give it a name and set the region that corresponds to your location.
  6. From the Heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.
  7. Confirm the linking of the Heroku app to the correct GitHub repository.
  8. In the Heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".
  9. Set the following config vars:
  ![heroku_config_vars](https://user-images.githubusercontent.com/61304684/138800234-f5f46a0e-b878-49c1-a3d6-983d178ac87c.png)
  10. To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.mongodb.com/manual/reference/connection-string/#std-label-mongodb-uri)
  11. In Heroku dashboard, click "Deploy"
  12. In the "Manual Deployment" section of this page, made sure the master branch is selected and then click "Deploy Branch".
  13. The site is now successfully deployed.
  
  ### Forking the GitHub Repository

  By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

  1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
  2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
  3. You should now have a copy of the original repository in your GitHub account.

  ### Making a Local Clone

  1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
  2. Under the repository name, click "Clone or download".
  3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
  4. Open Git Bash
  5. Change the current working directory to the location where you want the cloned directory to be made.
  6. Type `git clone`, and then paste the URL you copied in Step 3.

  ```
  $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
  ```

  7. Press Enter. Your local clone will be created.

  ```
  $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
  > Cloning into `CI-Clone`...
  > remote: Counting objects: 10, done.
  > remote: Compressing objects: 100% (8/8), done.
  > remove: Total 10 (delta 1), reused 10 (delta 1)
  > Unpacking objects: 100% (10/10), done.
  ```

  Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

  ## Credits

  ### Code

  - [Code Institute - &#39;Backend Development | Mini Project | Putting It All Together&#39;](https://codeinstitute.net/): Used Python Flask code from this excellent Code Institute tutorial on building a Flask Task application in Python.
  - [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System. also used Bootstrap to build basis of input fields and menu dropdown options for user input sections: login, register and add recipes sections. 
  - [Copyright 2013-2021 Start Bootstrap LLC - &#39;Clean-Blog template&#39;](https://startbootstrap.com/theme/clean-blog) [Code released under the MIT license](https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE): used the Start Bootstrap template to facilitate a simple setup of a clean header and footer for all pages of the app and a collapsible menu bar shown in mobile viewports. 
  - [Copyright 2013-2021 Start Bootstrap LLC - &#39;SB Forms Contact Forms&#39;](https://startbootstrap.com/solution/contact-forms): Code was used for the user contact form for the contact.html page. 
  - [Mr. Web Developer - &#39;Complete Responsive Food/Restaurant using HTML/CSS/JQuery/Bootstrap - Step By Step&#39;](https://www.youtube.com/watch?v=ajtLKcOF7RM): Code was used as a basis to develop group_recipes.html page and css styles to create individual responsive clickable food cards for each recipe for all users of the site. 
  - [Coding Addict and freecodecamp.org - &#39;HTML & CSS Project Tutorial - Build a Recipes Website&#39;](https://www.youtube.com/watch?v=-8LTPIJBGwQ): Code was used to facilitate development of the single_recipe.html page for this app.
  - [&#39;Box Shadow Styles&#39; W3schools tutorial](https://www.w3schools.com/css/css3_shadows_box.asp): used code to guide development of a beautiful box shadow surrounding the card background for the user input fields and drop down menus for the add_recipe.html page.


  ### Content

  - All content was written by the web developer, Kashina Kessler but some code snippets may be very similar and partially identical to code snippets, mentioned above under the 'Credits: Code' section. The developer has added comments to JS CSS and HTML adding credit and links to these particular code snippets. All code was customized by the developer to create a new application.

  ### Media

  - #### Photos

  1. [Pepper and Tomatoes surrounding Wooden Food Tray](https://elements.envato.com/different-vegetables-on-wooden-background-PHTVFJE): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  2. [Plums](https://elements.envato.com/concept-of-tasty-food-with-plums-on-a-wooden-table-64U3W5F): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  3. [Tomatoes in Jar](https://elements.envato.com/food-R37NRBG): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  4. [Lasagna](https://elements.envato.com/food-844L2PT): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  5. [Vegetables on Wooden Background](https://elements.envato.com/food-538D26T): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  6. [Italian Food Ingredients](https://elements.envato.com/italian-food-background-with-food-3RJR57Z): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  7. [Meat Soup](https://elements.envato.com/food-W3HT2BH): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  8. [Ravioli](https://elements.envato.com/food-JFNDSY9): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  9. [Pan Pizza](https://elements.envato.com/food-ZFT9QMS): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  10. [Vegetarian Chili](https://elements.envato.com/vegetarian-chili-with-cilantro-PM2TWL4): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  11. [Russian Cabbage Soup](https://elements.envato.com/traditional-russian-soup-with-cabbage-sauerkraut-s-9CHD24Us): [Commercial License](https://elements.envato.com/license-terms), [Envato Elements](https://elements.envato.com/)

  12. [Avocado Toast](https://www.pexels.com/photo/basil-leaves-and-avocado-on-sliced-bread-on-white-ceramic-plate-1351238/): [Free stock Photo License](https://www.pexels.com/license/), Photo by [Lisa](https://www.pexels.com/@fotios-photos?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels) from [Pexels](https://www.pexels.com/photo/basil-leaves-and-avocado-on-sliced-bread-on-white-ceramic-plate-1351238/?utm_content=attributionCopyText&utm_medium=referral&utm_source=pexels)

  - #### Fonts

  1. [&#39;Open Sans&#39;, Google Fonts](https://fonts.google.com/specimen/Open+Sans?category=Sans+Serif&query=open+sans#standard-styles): [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0), [Steve Matteson](https://mattesontypographics.com/)

  2. [&#39;generic Sans-serif&#39;, Google Fonts](https://fonts.google.com/?category=Sans+Serif): [Open Font License](https://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=OFL)

  ### Acknowledgements

  - My Mentor, [Moosa Hassan](https://moosahassanx.github.io/Personal-Website/) for his dedication and time for helpful project feedback.
  - [Code Institute](https://codeinstitute.net/) for their support and education.
 
