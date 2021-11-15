# Discover Malta - Testing details

[Main README.md file](README.md)

[View deployed site here](https://discover-malta.herokuapp.com/)

# Table of Content

[**Testing**](#testing)
   - [**Validation Results**](#validation-results)
   - [**Testing User Stories**](#user-stories-testing)
        - [**First Time User**](#first-time-user)
        - [**Returning User**](#returning-user)
        - [**Frequent User**](#frequent-user)
        - [**Potential Client**](#potential-client)
        - [**Business Goals**](#business-goals)
   - [**Further Testing**](#further-testing)
      - [**Device Compatibility Table**](#device-compatibility-table)
      - [**Elements on Every Page**](#elements-on-every-page)
      - [**Home Page**](#home-page)
      - [**Registration Page**](#registration-page)
      - [**Login Page**](#login-page)
      - [**Profile Page**](#profile-page)
      - [**Edit Review**](#edit-review)
      - [**Products Page**](#products-page)
      - [**View Product**](#view-product) 
      - [**Add Product**](#add-product) 
      - [**Edit Product**](#edit-product) 
      - [**Contact Page**](#contact-page) 
      - [**404 Page**](#404-page)
      - [**500 Page**](#500-page)
   - [**Google Lighthouse Testing**](#google-lighthouse-testing)
   - [**Cross Browser Compatibility Table**](#cross-browser-compatibility-table)
   - [**Bugs**](#bugs)

## Validation Results

- The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.
- I have also used JSHints for JavaScript and jQuery code.
- PEP8 has been used to ensure Python code is fully compliant.

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/)

   | Files    |       Validation      |  Errors        |
   |----------|:---------------------:|:---------------:|
   |*checkout.css*|      &check; | removed `-webkit-transition` which was throwing a warning during validation |
   |*home.css* |      &check; | removed `-moz-transition` and `-webkit-transition` which was throwing a warning during validation|
   |*star-rating.css*  |      &check; | no errors |
   |*trips.css* |  &check; | removed `-moz-transition` and `-webkit-transition` which was throwing a warning during validation and dublicate background colour property |

 - Final check has been completed for all pages, no errors or warnings have been found.

- [W3C Markup Validation](https://validator.w3.org/)
   - HTML code pass validation without major errors.
   - Label element had `for` attribute invalid due to using form input elements from Django Forms, checked using the dev tools to find the correct `id` for the input element. Altered the `label` element to match the input `id`.


       | Pages    |       Validation      |
       |----------|:---------------------:|
       |*edit_profile.html*|      &check; |
       |*edit_review.html* |      &check; |
       |*favourites.html*  |      &check; |
       |*forgot_password.html* |  &check; |
       |*login.html* |            &check; |
       |*profile.html* |          &check; |
       |*regiseter.html* |         &check;|
       |*reset_password.html* |   &check; |
       |*view_reviews.html* |     &check; |
       |*bag.html* |              &check; |
       |*checkout_complete.html* | &check;|
       |*checkout.html* |          &check;|
       |*about.html* |             &check;|
       |*contact.html* |           &check;|
       |*index.html* |             &check;|
       |*add_trip.html* |          &check;|
       |*trip_detail.html* |       &check;|
       |*trips.html* |             &check;|
       |*update_trip.html* |       &check;|

  - Final check has been completed for all pages, no errors or warnings have been found.


- [Broken link check](https://www.brokenlinkcheck.com/broken-links.php#status)
   - All pages have passed without issues, no broken links have been detected
  

- [JSHint](https://jshint.com/)
   
   | Files    |       Validation      |  Errors        |
   |----------|:---------------------:|:---------------:|
   |*quantity.js*|      &check; | removed bad assignment `$(input).val() = 8` due to bad assignment warning |
   |*stripe.js* |      &check; | one undefined variable `Stripe` which is coming directly from *Stripe API* |
   |*home-script.js*  |      &check; | no errors |
   |*dateoucjer.js* |  &check; | no errors |
   |*main_script.js* |  &check; | one undefined variable `bootstrap` coming from Bootstrap library |
   |*modal.js* |   &check; |  no errors |

 - Final check has been completed for all pages, no errors or warnings have been found.

- [PEP8](http://pep8online.com/)
   
   | Apps    |       Validation      |  Errors        |
   |----------|:---------------------:|:---------------:|
   |*Accounts*|      &check; | forms.py - white space on line 21 |
   |*Bag* |      &check; | vies.py - line 124 indentation error |
   |*Checkout*  |      &check; | no errors  |
   |*Contact* |  &check; | no errors|
   |*Discover_Malta* |  &check; | settings.py - lines 123, 126, 129, 132 displayed an error of being too long, this was left unfirxed as they were provided by default by Django|
   |*Home* |   &check; |  no errrors |
   |*Trips* |   &check; | no errors  |
   |*custom_storages.py* |   &check; | no errors  |

- [Extendclass](https://extendsclass.com/python-tester.html)

   | Apps    |       Validation      |  Errors        |
   |----------|:---------------------:|:---------------:|
   |*Accounts*|      &check; | forms.py and views.py throwing a syntax error for `f string` |
   |*Bag* |      &check; | views.py - throwing a syntax error for `f string` |
   |*Checkout*  |      &check; | forms.py, models.py, views.py, webhook_handler.py throwing a syntax error for `f string` |
   |*Contact* |  &check; | views.py - throwing a syntax error for `f string` |
   |*Discover_Malta* |  &check; | settings.py - throwing a syntax error for `f string`|
   |*Home* |   &check; | no errors   |
   |*Trips* |   &check; | views.py - throwing a syntax error for `f string`  |
   |*custom_storages.py* |   &check; | no errors  |


##### back to [content](#table-of-content)


## User stories testing

### Testing user stories from UX section of [README.md](README.md)

#### First Time User

1.	As a first time user, I want to understand what this site is about.

  - The site is designed with simple and easy to understant content in mind.
  - The title of the site tells the user this site is about Malta.
  - A hero images feature some of the Malta's most iconic places
  - A favicon icon is a symble of the sunny holiday platform

2.	As a first time user, I want to browse through the trips available on site.
  
  - The user can access all the trips via a link in the main navigation
  - The user may access trips which are spesific to the category by clicking on the title of the category displayed on the Home page
  - The user may also access all trips via a call to action button at the bottom of the Home page

3.	As a first-time user, I want to see full trip details and trip reviews from other users.

   - When the user lands on the *trips.html* page they are able to view a short description of each trip, this also includes 
     - Trip Image
     - Trip Name
     - Trip Duration
     - Trip Price
     - Trip Star Rating
     - Call to action button 'More Info'

    - Based on this information a user may choose a specific trip which they want to view
    - They can access trip details in three ways:
      - By clicking on the trip image
      - By clicking on the trip name
      - By clicking on the 'More Info' button
    
    - The user will be directed to the *trip_details* page, where the user may view all the information for this trip
    - If the trip has star rating or reviews, they will be displayed to the user at the bottom of the page
    - The user will see the star rating, who created this review and the date the review has been created or updated.

4.  As a first-time user, I want to understand the benefits of booking my holiday itinerary using this platform.

    - On the *Home Page* the user is presented with a paragraph detailing why they should use this platform to plan their itinerary.
    - The benefits are presented in the visualy intising way, using different colour circles which display on scroll, drawing the user attention
    - The circles use icons and text to give user a full experience.

5.  As a first-time user, I want to add the trips which I like to my favourites.

    - A user may shortlist trips to their favourites in two ways: 
       - From *trips.html* page
       - From *trip_details page*
    - By clicking on the heart shape icon
    - If the user is not logged in, and they hover over the icon, the message will be displayed telling them they should login to add this trip to their favourites.
    - If they click on the icon, they will be redirected to *login page*, where they can choose to login or register
    - Once the user is logged-in, they may add trips to their favourite list by clicking on the heart icon.
    - A message will be displayed at the top of the screen letting them which trip they have added to their favourite list 
    - Hear icon in the menu will change colour to red and the trip count will be amended letting the user know how many trips they have added to their favourites.

6.  As a first-time user, I want to find a variety of experiences suited for different ages and requirements.

    - User may choose to search for a specific keyword in the search bar profided on *trips.html* at he top of the page.
    - The search bar will display the number of the results found with their keyword and all the related trips
    - The user may narrow down their search by clicking on the specific category, dropdown menu is available in the navbar across the whole site
    - On the *trips.html* under "Refine you search", they have an option to choose their category as well
    - The user may sort the trips available by price, rating, duration or whether or not the trip is family-friendly on the *trips.html*

7.  As a first-time user, I want to navigate the site easily and view site on different screen sizes.

    - The site has been designed with user experience and mobile first approach in mind. The site has adopted a fully resposive design across all screen sizes.



#### Returning User 

1.	As a returning user, I want to be able to login into my account

    - Once the user is registered and has gone through verification steps, the user may login into their account by pressing on the user icon in the navigation bar.
    - A dropdown menu will open and give 2 options to the user, either to login or register.
    - Once the user is logged in, they will be greeted with a friendly message welcoming them to the site, using their name
    - The user icon will change into default user avator or cutom if selected.

2.	As a returning time user, I want to view my favourites and check their availability

    - A logged-in user may access their favourites by clicking on the heart icon in the navigation bar
    - The icon will display the number of trips the user has in their favourites list
    - A logged-in user may navigate to their profile page and click on the link "View Favourites", to access their favourites page
    - On this page the user is able to see how many favourites they have in their list, by clicking on the trip imag, name or "More Info" button they will be directed to the *trip details* page.
    - They may add a trip to their shopping bag by clicking on "Book Now" button and select the number of tickets and booking date.
    - If the trip does not have enough tickets for the user requirements, the message will display letting the user know how many tickets are left for a specific trip.
    - If the trip does not have any tickets left, "Book Now" button will display "Sold Out" and the button will be disabled.

3.	As a returning user, I want to search for a specific trip or filter trips by category.

     - By now the user is familiar with the site and will be able to navigate easily throughout it.
     - Can view the trips by category from the *Home page*, *navigation menu* or *trips.html*
     - They can sort the trips from the *trips.html* using *Sort By* dropdown menu

4.	As a returning user, I want to learn more about the site.

    - A user may find a link to the about page in the footer.
    - The link will take them to the *About Page*, where the user can find out the core mission behind the site
    - A user has two options at the bottom of the page to "Go Back" which will take the user to the *Home Page* or to *Get in Touch* which will take the user to the contact page.

5.	As a returning user, I want to purchase the trip with secure checkout.

    - A user may access the checkout from their shopping bag page, the link "Proceed to Secure Checkout" is locate at the bottom of the page
    - Once the user is on the checkout page, they are presented with a short information about the trip they are about to purchase
    - They have an option to view full details of the trip by clicking on *trip name*
    - The user is asked to fill in form with their personal details
    - A user navigate to *login page* or *registration page* if they would like to save their details for next time and view their order history.
    - If the user is logged in, the form will be pre-filled with user details stored in user profile
    - The user may click a box to save or update their personal information during the checkout process
    - Once the user enters a card number, strip will act as a secure payment platform and check that all required details are correct.
    - On successful checkout, the user will be redirected to the *complete chekcoout* view, where the ticket summary will be displayed.
    - A message at the top of the screen will let the user know that a confirmation email has been send to their email address.
    - The user will recieve confirmation email which will display their order number, which they will need to present to the trip provider on the day of the trip
    - A looged in user may also view their order history on their profile page.
    - User card details are not stored in the database.

6.	As a returning user, I want to get an instant email confirmation of my transaction.
    
    - During successful checkout, the user will recieve confirmation email which will display their order numbe
    - They will need to present their order number to the trip provider on the day of the trip
    - This email will contain full details of the trips booked and personal details entered.

7.	As a returning user, I want to have feedback provided to me every step of the way.

    - The site is desigened to provide and guide user during their time on the site.
    - The feedback is provided to the user in the form of notifications pop ups at the top of the screen
    - Warnings, Alerts, Info and Success messages
    - When the user is deleting their review, a modal will apper asking to confirm their decition.
    - Automated emails have been set up as a confirmation to the user of their actions during purchase, regestraion, reseting passowrd and contacting the site owners. 

8.	As a returning user, I want to view my ticket on my profile page.

    - If the user has regestered on the site, prior to purchasing, their order history will be displayed on their profile page

9.  As a returning user, I want to be able to save my information to my profile for quick and easy checkout next time.
    
    - This functionality is restricted to regestered and logged in users.
    - The user is able to click on the checkbox during the checkout process to save or update their personal information
    - The user will be able to view this information in their profile
    - The user will have their information pre-filled during the checkout next time and in case they deside to user a contanct form to contact the site owner



#### Frequent User

1.	As a frequent user, I want to customize my profile page

    - A logged-in user may navigate to their profile page.
    - Profile page displays a number of options available to the user 
    - By clicking on the linkg "Edit Your Profile" user will be directed to the page where they can view and update their personal information, including their avatar.

2.	As a frequent user, I want to review the trips which I have been on.

    - A logged in user, who has purchased a specific trip may navigato to trip detail page where a review form will be available to them
    - They may choose to give star rating, review title and their review of their experience
    - The form will be submitted and they will be able to view their review straight away on the same page
    - If the user has not purchased the trip yet, a message will be displayed to them nofifying them they have to purchase the trip first

3.	As a frequent user, I want to be able to update and delete my reviews.

    - If the user is logged-in and has reviews, they can edit or delete thier reviews from:
       - *Trip Detali Page* by clicking on the appropriate buttons
       - If the user submits another review for the same trip, their original review will be updated
       - *Profile Page* - click on the link "Manage Reviews" which will take the user to *view_review.html* page. All the user reviews are displayed on this page
       - User may choose to "Edit" their review which will take the user to pre-filled form with their review and alert will appear letting the user know which review they are editing
       - User may choodse to "Delete" their review, in that case a modal will appear asking the user to confirm their decision. 

4.	As a frequent user, I want to follow the site on social media.

       - The user may click on the social media icons at the bottom of the page which will take them to their prefered site.

5.	As a frequent user, I want to be able to contact the site owners if I have an enquire.
       
        - Any user may click on the contact link located in the footer of the site.
        - It will take them to the *contact.html*, if the user is logged in they will have their information pre-filled for a quicker form submittion
        - Otherwise the user will be asked to fill in the form and choose a subject from the dropdown menu
        - The user is redirected to the *home page* and a message will appear on the screen letting them know they should have recieved a confirmation email
        - A user will recieve automated email letting them know the site owners have recieved their enquire and will be in touch shortly.
        - An email will be generated to the admin user, with a client enquire and client details.

6.  As a frequent user, I want to the explore latest deals
        
        - Last minute deals category is positioned in the category dropdown menu, if there are any trips under this category the user will be able to view a list of trips by clicking on this category link.



##### back to [content](#table-of-content)

### Potential Client
1.	As a potential client I want to see a sample of trips to get an overview of what my product might look like

     - A potential client may browse throgh the site to get the feel of the design and style of the site
     - Each trip has the same style and design, therefore a potential client may have a good overview of what their product may 
     look like on the site

2.	As a potential client I want to learn what benefits are available to me
    
    - A potential client may navigate to *About Page*
    - The information presented there is let the user know about the core mission of the site and what benefits are availalbe to the potential clients
    - Call to action button, promps the potential client to get in touch and request more information.

3.	As a potential client I want to easily get in touch with the site owners to request further information or book a call

    - A potential client may get in touch with the site owners by completing a contact form 
    - A subject option "Collaboration" has been created especially for this in mind. 
    - Once the message is recieved a relevent person from the team will be in touch

### Business goals

1.	As a business owner, I want to provide a platform for users where they explore what Malta has to offer and book their trips during their stay on the island.

    - The site has been designed to showcase what Malta has to offer
    - Provide the user with the range of activities
    - Enable the user to easily narrow down their search specific to their requirements

2.	As a business owner, I want the user to be able to register with secure login details.

    - Discover Malta has been designed to simplify the registration process for the user and ensure the user details are   stored  securely.
    - For the user to register they have to provide their full name, telephone number, email address and password.
    - A secure link is generated and sent to the user upon their registration
    - Once the link is clicked from the user email address the user is activated
    - User details and hashed password is stored in the database.
    - User is able to reset their password by clicking on the `click here to reset your password` link 
    - In that case another email is generated and send to the user email address to create a new password
    - The user is able to login when two conditions are met, user email address and password
    - The site owner who will have access to the database, will be able to see the username, however, will not be able to see the user password which is stored securely.
    - The user may choose to update their personal details in their profile page by clicking on the link `edit your profile`
 
3.	As a business owner, I want the user to be able to use the site easily on any device.

     - The site has been designed to be fully responsive with mobile first approach in mind.

4.	As a business owner, I want to provide useful links to users where they can purchase products and earn an affiliate commission.

     - The shop feature is yet to be implemented
     - The site owner will be able to earn commission on sale of the tickets, once term and conditions have been agreed with provider

5.	As a business owner, I want to be able to delete any reviews which I consider to be inappropriate or out of content.

     - An admin user may set any review status to False inside their Django admin panel. 
     - The condition for reveiw to display on site has been set as default to True.

6.	As a business owner, I want to be able to add additional new trips to the site. 

     - An admin user, once logged-in, can navigate to their profile page, where they will see a link to *add trip* page.
     - Once on the page, admin user is able to add new triip to the database once all the conditions have been met
     - Once added a new trip, the admin user will be redirected to the *trip_detail* page where they will be able to view the trip which they have just created.

7.  As a business owner, I want to be able to edit or delete trips.

    - An admin user may delete or update each trip from 2 pages:
        - Trips.html
        - Trip Details page
    
    - Once *Update* button has been pressed the user will be redirected to `update_trip.html` page
    - Alert will tell the user which trip they are updating
    - Once the trip has been ameded and form requirements are satified, the updated information will be saved to the database
    - The user will be redirected to the *trip details* page
    - Alert will be displayed letting the user know the information has been saved

    - Once *Delete* button has been pressed, an alert in the form of modal will appear asking the user to confirm their decision.
    - If this is an intentional action, the trip will be deleted from the database.
 
8.  As a business owner, I want to provide the user with search and filter functionality for products to enable easy access to the database.
     
     - Users may search the site using a search bar
     - Users may filter the trips by category
     - Users my sort the trips by a condition