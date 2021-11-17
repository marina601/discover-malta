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
   - [**Manual Testing**](#manual-testing)
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

  - The site is designed with simple and easy to understand content in mind.
  - The title of the site tells the user this site is about Malta.
  - A hero images feature some of Malta's most iconic places
  - A favicon icon is a symbol of the sunny holiday platform

2.	As a first time user, I want to browse through the trips available on site.
  
  - The user can access all the trips via a link in the main navigation
  - The user may access trips that are specific to the category by clicking on the title of the category displayed on the Home page
  - The user may also access all trips via a call to action button at the bottom of the Home page

3.	As a first-time user, I want to see full trip details and trip reviews from other users.

   - When the user lands on the *trips.html* page they can view a short description of each trip, this also includes 
     - Trip Image
     - Trip Name
     - Trip Duration
     - Trip Price
     - Trip Star Rating
     - Call to action button 'More Info'

    - Based on this information a user may choose a specific trip that they want to view
    - They can access trip details in three ways:
      - By clicking on the trip image
      - By clicking on the trip name
      - By clicking on the 'More Info' button
    
    - The user will be directed to the *trip_details* page, where the user may view all the information for this trip
    - If the trip has star rating or reviews, they will be displayed to the user at the bottom of the page
    - The user will see the star rating, who created this review and the date the review has been created or updated.

4.  As a first-time user, I want to understand the benefits of booking my holiday itinerary using this platform.

    - On the *Home Page* the user is presented with a paragraph detailing why they should use this platform to plan their itinerary.
    - The benefits are presented in a visually enticing way, using different colour circles which display on scroll, drawing the user attention
    - The circles use icons and text to give the user a full experience.

5.  As a first-time user, I want to add the trips which I like to my favourites.

    - A user may shortlist trips to their favourites in two ways: 
       - From *trips.html* page
       - From *trip_details page*
    - By clicking on the heart shape icon
    - If the user is not logged in, and they hover over the icon, the message will be displayed telling them they should log in to add this trip to their favourites.
    - If they click on the icon, they will be redirected to the *login page*, where they can choose to log in or register
    - Once the user is logged-in, they may add trips to their favourite list by clicking on the heart icon.
    - A message will be displayed at the top of the screen letting them which trip they have added to their favourite list 
    - Hear icon in the menu will change colour to red and the trip count will be amended letting the user know how many trips they have added to their favourites.

6.  As a first-time user, I want to find a variety of experiences suited for different ages and requirements.

    - User may choose to search for a specific keyword in the search bar provided on *trips.html* at the top of the page.
    - The search bar will display the number of the results found with their keyword and all the related trips
    - The user may narrow down their search by clicking on the specific category, the dropdown menu is available in the navbar across the whole site
    - On the *trips.html* under "Refine you search", they have an option to choose their category as well
    - The user may sort the trips available by price, rating, duration or whether or not the trip is family-friendly on the *trips.html*

7.  As a first-time user, I want to navigate the site easily and view the site on different screen sizes.

    - The site has been designed with user experience and a mobile-first approach in mind. The site has adopted a fully responsive design across all screen sizes.



#### Returning User 

1.	As a returning user, I want to be able to login into my account

    - Once the user is registered and has gone through verification steps, the user may log in to their account by pressing on the user icon in the navigation bar.
    - A dropdown menu will open and give 2 options to the user, either to log in or register.
    - Once the user is logged in, they will be greeted with a friendly message welcoming them to the site, using their name
    - The user icon will change into the default user avatar or custom if selected.

2.	As a returning time user, I want to view my favourites and check their availability

    - A logged-in user may access their favourites by clicking on the heart icon in the navigation bar
    - The icon will display the number of trips the user has in their favourites list
    - A logged-in user may navigate to their profile page and click on the link "View Favourites", to access their favourites page
    - On this page, the user can see how many favourites they have in their list, by clicking on the trip image, name or "More Info" button they will be directed to the *trip details* page.
    - They may add a trip to their shopping bag by clicking on the "Book Now" button and selecting the number of tickets and booking date.
    - If the trip does not have enough tickets for the user requirements, the message will display letting the user know how many tickets are left for a specific trip.
    - If the trip does not have any tickets left, the "Book Now" button will display "Sold Out" and the button will be disabled.

3.	As a returning user, I want to search for a specific trip or filter trips by category.

     - By now the user is familiar with the site and will be able to navigate easily throughout it.
     - Can view the trips by category from the *Home page*, *navigation menu* or *trips.html*
     - They can sort the trips from the *trips.html* using the *Sort By* dropdown menu

4.	As a returning user, I want to learn more about the site.

    - A user may find a link to the about page in the footer.
    - The link will take them to the *About Page*, where the user can find out the core mission behind the site
    - A user has two options at the bottom of the page to "Go Back" which will take the user to the *Home Page* or to *Get in Touch* which will take the user to the contact page.

5.	As a returning user, I want to purchase the trip with secure checkout.

    - A user may access the checkout from their shopping bag page, the link "Proceed to Secure Checkout" is located at the bottom of the page
    - Once the user is on the checkout page, they are presented with short information about the trip they are about to purchase
    - They have an option to view full details of the trip by clicking on *trip name*
    - The user is asked to fill in the form with their details
    - A user navigates to *login page* or *registration page* if they would like to save their details for next time and view their order history.
    - If the user is logged in, the form will be pre-filled with user details stored in a user profile
    - The user may click a box to save or update their personal information during the checkout process
    - Once the user enters a card number, Stripe will act as a secure payment platform and check that all required details are correct.
    - On successful checkout, the user will be redirected to the *complete checkcout* view, where the ticket summary will be displayed.
    - A message at the top of the screen will let the user know that a confirmation email has been sent to their email address.
    - The user will receive a confirmation email which will display their order number, which they will need to present to the trip provider on the day of the trip
    - A logged in user may also view their order history on their profile page.
    - User card details are not stored in the database.

6.	As a returning user, I want to get an instant email confirmation of my transaction.
    
    - During successful checkout, the user will receive a confirmation email which will display their order number
    - They will need to present their order number to the trip provider on the day of the trip
    - This email will contain full details of the trips booked and personal details entered.

7.	As a returning user, I want to have feedback provided to me every step of the way.

    - The site is designed to provide and guide the user during their time on the site.
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

## Manual Testing

### Device compatibility table


| Pages    |<strong>Laptop</strong>|<strong>Ipad</strong>|<strong>IphoneX</strong> | <strong>Nokia2.4</strong> | <strong>Sumsung</strong> |
|----------|:---------------------:|--------------------:|------------------------:|-----------------------:|-----------------------:|
| Home     | &check; | &check;| &check;| &check;| &check;|
| Trips  | &check; | &check;| &check;| &check;| &check;|   
| Trip Details    | &check; | &check;| &check;| &check;| &check;|
| Add Trip | &check; | &check;| &check;| &check;| &check;|
| Update Trip | &check; | &check;| &check;| &check;| &check;|
| About | &check; | &check;| &check;| &check;| &check;|
| Contact | &check; | &check;| &check;| &check;| &check;|
| Checkout Complete | &check; | &check;| &check;| &check;| &check;|
| Checkout | &check; | &check;| &check;| &check;| &check;|
| Bag | &check; | &check;| &check;| &check;| &check;|
| Edit Profile | &check; | &check;| &check;| &check;| &check;|
| Edit Review | &check; | &check;| &check;| &check;| &check;|
| Favourites | &check; | &check;| &check;| &check;| &check;|
| Forgot Password | &check; | &check;| &check;| &check;| &check;|
| Login | &check; | &check;| &check;| &check;| &check;|
| Profile | &check; | &check;| &check;| &check;| &check;|
| Register | &check; | &check;| &check;| &check;| &check;|
| Reset Password | &check; | &check;| &check;| &check;| &check;|
| View Reviews | &check; | &check;| &check;| &check;| &check;|
| 400.html | &check; | &check;| &check;| &check;| &check;|
    
##### back to [content](#table-of-content)

### Elements on Every Page

- All steps on the desktop were repeated on mobile, tablet and laptop screen sizes.

1. Navigation

- Hover over each link, confirm the hover effect works as expected.
- Click each link in the navbar to confirm that it leads to the correct page.
- Click each link in the "Categories" dropdown menu and confirm each category displays the correct trips.
- Confirm that when logged out the options "Login" and "Register" are visible and that "Profile" and "Logout" are not.
- Click on heart icon and confirm it takes user to the "Login" page.
- Add a trip to your shopping bag, confirm the suitcase icon changes colour and total value of the trips is updated.
- Remove all the trips from your shopping bag, confirm the icon changes colour to white and the value displayed is 0.00.

- Log in to the site, confirm that options "Profile" and "Logout" are visible and that "Login" and "Register" are not.
        - Confirm the user icon chages either to default user image or selected user image is changed by the user.
        - Add some trips to your favourites and confirm the heart icon changes colour and displays the number of trips added.
        - Click on the favourites link and confirm it takes the user to "Favourites Page"
        - Remove all the trips from your favourite list and confirm the heart icon changes the colour back to white and displays 0 number of trips in your favourite

- Go to the bottom of the page to make sure the navigation bar is sticky.

- Mobile and Tablet view:

  - Confirm burger button appears on the left-hand side of the navbar.
  - Confirm the user, suitcase and heart icons apper next to the burger button.
  - Click on the burger button, confirm the background colour and the colour of the bars are changing.
  - Click on the burger button, confirm the drop down menu display links: "Home", "All Trips" and "Categories"
  - Click on the "Categories" dropdown menu and confirm all the category link are displayed.
  - Confirm the site heading/logo "Discover Malta" is no longer visible.
  - Followed the same steps as above to determine all the links are working.
  - Flip the tablet and mobile devices to check responsiveness.

2. Footer
  - Hovered over each link, confirmed background colour changed as expected.
  - Confrim "Follow Us" is disabled, therefore no animation is present on hover.
  - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
  - Click the social icons, confirm that they open a new tab and takes the user to correct social media platform.
  - The footer is responsive on all window view sizes.
  - Check date of copyright information, confirm year displayed matches the current year.

3. Favicon
  - View the site on different devices and confirm the favicon image is present

4. Title
  - Click on each page, view the tap of each page and confirm each page contains custom title

##### back to [content](#table-of-content)

### Home Page

1. Hero Slider
   - Confrim the carousel images fade within 5 seconds
   - Confirm the carousel is touch compatible by sliding the fingers to the left and right
   - Open dev tools in Google Chrome confim each image contains `alt` attribute

2. Welcome Message 
   - View the welcome message on all devices, confirm the message appears in the centre of the page.

2. Benefits
   - Scroll up and confirm no benefits are displayed on the page
   - Confirm each element is displayed to the user within 2 seconds interval
   - Confirm responsive layout of the elements accross all screen sizes
   - Confrim each element contains `box-shadow: -3px 8px 27px -2px rgb(180 179 179 / 51%);` which makes them stand out.
   - Inspect the page in the Google Dev Tools and confirm each icon contains `aria-hidden="True"` attribute. This will make the icon hidden from the screen reader, giving the user a better accessability to the page.


![benefits](readme-files/images/benefits.png)

4. Categories 
   - Confrim the categories divs are displayed in the grid format and responsive across all screen views:
            - Large screen - 4 category cards per row
            - Medium screen - 3 category cards per row
            - Small screen - 1 category card per row
   - Each category card contains a border and box-shadow property to make them stand out and create a 3D look
   - Hover over each card and confirm the `box-shadow` property is changing
   - Hover over each title of the category and confirm background colour is changing as expected
   - Click on each category title and confirm it takes you to the page which displays trips only under a specific category. The trip cound displays the correct number of results returned.
   - Click on the 'last minute deals' category and confirm the no trips are displayed, the trip count is showing 0 and a message displayed to the user. 

5. Call to Action 
  - View all trips call to action button appears at the bottom of the page.
  - Hover over the link, confirm background colour is changing as expected.
  - Click on the link, confirm it takes the user to the *trips.html* page.

  - Above tests have been repeated on tablet and mobile devices.
    

### All Trips

1. Search

  - Click inside the search input and confirm the placeholder displays the text "Search our site"
  - Search by a key word, confirm the page displays all the trips which contain the key word and the number of results is updated.
  - Type a key word which deos not exists like "kitty" and confirm no trips are displayed, the rusult count displays 0 and a message displayed to the user telling then "We do not have any trips with your search criteria, please try again."
  - Click on the search button with an empty input field and confirm all trips are displayed again.

2. Filter

  - Click on the dropdown menu "Categories" and confirm all the categories are displayed which exists in the database, plus a link to all trips is also present.
  - Hover over each link and confirm the background colour is changing and transitions are present, as expected.
  - Click on each link and confirm the page displays the trips under each cagegory, the total trip count updates and represents the number of trips under each category.
  - Click on the "All trips" link and confirm all the trips are displayed on the page.

3. Sort
   - Select sort by price and sort by duration confirm the results are returned in acsending order
   - Select sort by rating, confrim the results returned are in descending order
   - Select sort by family friendly, confirm the results returned display the trips which have value `family_friendly` set to `True`
   - Confirm each time the sort functionality is selected the total number of trips is returned in the `trip_count`

- Hover over the search, choose your category and sort by buttons and confirm the backgourn colour is changing

4. Trip-card

   - Confirm the cards are displayed 3 in the row on the large screen, 2 in the row on the medium screen and a single card in each row on the small screen.
   - Hover over each card and confirm the box-shadow property is changing, making each card-trip stand out to the user
   - Hover over heart icon, confirm the background colour changes as expected. 
   - For not logged in user:
            - Tooltip displays the message "Login to add this trip to your favourites".
            - Click on the hear icon, confirm the it re-directs the user to login page.
   - If the user is logged in:
            - Hover over the heart icon, tooltip displays the message "Add to favourites"
            - Click on the icon, confirm the the icon dissapears and instead the trash icon appears
            - Hover overthe trash icon, tooltip disiplays the message "Remove from favourites"
            - Heart icon in the navbar changes colour to red and displays the number of trips added to the favourite list.
            - Toast message notifies the user which trip they have added to their favourites
            - Click on the trash icon, confirm the number of trips in the navbar updates
            - If no trips in the favourite list the heart icon displays 0 and background colour goes back to default white
            - The trip's heart icon which has been removed from the favourites list reverts to its original state.
            - Toast message notifies the user which trip they have removed from their favourites

   ![favourites](readme-files/images/trips-favourites.png)

   - Hover over the trip image, confirm the `cursor` is set to `pointer`
   - Click on the trip image, confrim it takes the user to the "Trip Details Page"
   - Hover over the trip name, confirm the background and tex colour changes as expected
   - Click onthe trip name, confirm it teaks the user to the "Trip Detail Page"
   - Trip card contains a short description of the trip, if the text lenght is longer than height property set to the card, it displays `overflow: auto;` property set in css file
   - 4 icons at the middle of the card set out the most important information the user might look out for:
            - Duration
            - Price
            - Rating
            - Family Friendly
    - If the trip has star rating, the star icon changes colour to yellow and display the average star rating for the trip calculated in the trips.models.py using Avg function from Django:

              - `def averageRating(self):
              -      """Calculate average trip review"""
              -      reviews = ReviewRating.objects.filter(trip=self,
              -                                           status=True).aggregate(
              -                                               average=Avg('rating'))
              -     avg = 0
              -      if reviews['average'] is not None:
              -          avg = float(reviews['average'])
              -     return avg`
    - If there is no star rating for this trip, the star icon is set to default black colour and message displays there is "no rating yet"
    - If the trip is family friendly a child icon is displayed, if the trip is not set to be family friendly no icon is displayed.
    - Call to action button "More Info", on hover changes colour and when clicked directs the user to trip details page.
    - Open dev tools in Google Chrome and inspect each card image, confirm each image contains an `alt` attribute

![trip-card](readme-files/images/trip-card.png)

6. Admin User
   - If the user is logged in as Admin user, they have 2 extra button at the bottom of each card.
           -Update
           -Delete
  - Click on update button, confirm it redirects the user to "Update Trip Page" for the current trip.
  - Try to access update_trip url as a non logged in user, confirm it redirects the user to login page.
  - Try to acces update_trip url as a logged in user, confrim the message is displayed telling the user they do not have access to this page and link is in the form of button is displayed "Go back to all Trips"
  - Click on delete button, confirm a modal is dipslayed asking the user to confirm their decision.
  - Click delete button in the modal, confirm the toast message appears telling the user which trip has been deleted and redirects the user back to *trips.html*
  - Try to access delete_trip url as a non logged in user, confirm it redirects the user to login page.
  - Try to access delete_trip url as a logged in user, confirm toast notification appears letting the user know they do not have admin previlagies to delete this trip
  - Confirm the Update and Delete buttons only visible to Admin user

![delete-modal](readme-files/images/delete-modal.png)

7. Pagination
  - Go to the bottom of the page and check the pagiantion is working as expected
  - 8 Trips per page will display on the first page
  - Then the number of pages will be dynamically generated based on `trip_count` results
  - If on page 1, previous button will be disabled 
  - If on the last page, the next button will be disabled.
  - Current page number is displayed to the user and the page number's background colour is changed when active.

## Trip Detail

1. Favourites
  -  Confirm favourtites functionality works in the same way as described in "All Trips Page".

2. Book Now
   - Book Now button appears in the top right hand corner
   - Scroll down and confirm the button is fixed to the top of the page at all times, giving the user an easy access to add this trip to their bag and check availability
   - If the trip's number of tickets is 0, confirm the "Sold Out" is displayed instead, which is not fixed to the top of the page
   - Confirm the button is disabled and the user is not able to click on it
   - Click on the "Book Now" button confirm modal is appearing asking the user to enter the numer of tickets and booking date
   - Confirm if the trip is not family_friendly, the modal displays an input field only for adult tickets
   - Click on "Add to Suitcase" button without entering any details, confirm the message is displayed "At least 1 adult ticket required to purchase this trip"
   - Try to type a letter in the input field, confirm nothing is displayed, as input field expects a number.
   - Enter an adult number of tickets and click on "Add to Suitcase" button, confirm the message displayed "Select the date for your trip"

   3. Datepicker

            - Click on the input field to select the date confirm, datepicker is displayed
            - Confirm the first available date is available is tomorrow, the user will not be able to book a trip for the current or past date.
            - Confirm tomorrow's date is highlighted.
            - Click on any disabled dates, confirm it cannot be selected.
            - Click on the next button, next to the current month, confirm the month is changing, the current year is displayed.
            - Select any date in the furture and confirm the datepicker is closing once the date is selected, the date selected is displayed inside the input field.
            - Open the datepicker again, confirm the datepicker highlights the date selected.
    
    - Add the trip to the bag with children tickets set to 0, confirm the operation did display any errors, as the children tickets are allowed not to be selected
    - Once all the input fields are valid. Click "Add to suitcase" confirm the toast notification is displayed telling the user which trip they have added to their bag.
    
   

4. Trip Details
   - Hover over a trip image and confirm `alt` attribut is present
   - Check that all the information from the database is present
   - Check average rating logic is the same as described in the "All Trips Page"
   - If the trip has any reviews, the review count is displayed
   - If there is not reviews for the trip, "No Reviews" message is displayed next to the icon.

4. Cancellation Policy
   - Check that cancellation policy contains a link to the "Contact Page"
   - Click on the link, confirm it takes the user to the *contact.html*

4. Review Rating

5. Customer Reviews

6. Call to Action 





## Bugs

- Navbar dropdown menu is not working 
 - Added data-bs-toggle="dropdown" to the trigger button 
 - Added link to the js popper 
 - https://www.studytonight.com/bootstrap/solvedbootstrap-dropdown-not-working
 - Because bootstrap 5 stopped supporting old browsers

- Average rating not sorting 
  - solved it by importing F function from Django which accepts null values
  - from [django documentations](https://docs.djangoproject.com/en/3.2/ref/models/expressions/#using-f-to-sort-null-values)

- Book Now modal
   - During testing found a console error, when the trip was sold out and the modal was replaced with "Sold Out" button.
   - Fix: by adding a condition to check if the element exists in `modal.js`

- Pagination not working during search and sort function