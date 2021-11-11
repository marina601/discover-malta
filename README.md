# Discover Malta

![Discover Malta](readme-files/images/responsive-img.png "Am I Responsive Image")

[View the deployed project here](https://discover-malta.herokuapp.com/)

I have created this e-commerce/booking site as part of my final Milestone 4 project for Code Institute, 
focusing on Full Stack Web Development using HTML, CSS, JavaScript, jQuery, Python, Django and Postgresql.

Discover Malta site offers the user the ability to discover the beautiful island of Malta and plan their holiday antinary on one platform. The site offers the user quick and easy checkout, instant ticket confirmation, a gallery of trips and some useful information which they need during their stay. 

The main objective of this site is to support local tour operators by reducing their wage cost, offering custom page design for each trip and easy online transactions. Taking the hustle of marketing and organization away, letting the business owners focus on delivering an outstanding experience to our clients.



# Table of Content

1 [**Project Goals**](#project-goals)

2 [**UX**](#ux)
   - [**User Goals**](#user-goals)
   - [**Scope**](#scope)

3 [**Structure of the app**](#structure-of-the-app)
   - [**View for a guest user**](#view-for-a-guest-user)
   - [**View for logged in user**](#view-for-logged-in-user) 
   - [**View for admin**](#view-for-admin)
   - [**User Stories**](#user-stories)
   - [**Business goals**](#business-goals)

4 [**User Requirements and Expectations**](#user-requirements-and-expectations)
   - [**Requirements**](#requirements)
   - [**Expectations**](#expectations)

5 [**Design**](#design)
   - [**Colour Scheme**](#colour-scheme)
   - [**Typography**](#typography)
   - [**Imagery**](#imagery)
   - [**Icons**](#icons)
   - [**Style**](#style)

6 [**Wireframes Flowchart and Data Model**](#wireframes-flowchart-and-data-model)
   - [**Wireframes**](#wireframes)
   - [**Database model**](#database-model)
   - [**Flow Chart**](#flow-chart)

7 [**Features**](#features)
   - [**All Pages**](#all-pages)
   - [**Home Page**](#home-page)
   - [**All Trips Page**](#all-page)
   - [**Trip Details Page**](#trip-details-page)
   - [**Add Trip Page**](#add-trip-page)
   - [**Update Trip Page**](#update-trip-page)
   - [**Delete Trip**](#delete-trip)
   - [**Login Page**](#login-page)
   - [**Registration Page**](#registration-page)
   - [**Forgot Password Page**](#forgot-password-page)
   - [**Reset Password Page**](#reset-password-page)
   - [**Logout**](#logout)
   - [**Profile Page**](#profile-page)
   - [**Edit Profile Page**](#edit-profile-page)
   - [**View Review Page**](#view-review-page)
   - [**Edit Review Page**](#edit-review-page)
   - [**Favourites Page**](#favourites-page) 
   - [**View Bag Page**](#view-bag-page) 
   - [**Checkout Page**](#checkout-page) 
   - [**Checkout Success Page**](#checkout-success-page) 
   - [**Contact Page**](#contact-page)
   - [**About Page**](#about-page)
   - [**404 Error Page**](#404-error-page)
   - [**500 Error Page**](#500-error-page)
   - [**Features Left to Implement**](#features-left-to-implement)

8 [**Technology Used**](#technology-used)
   - [**Languages Used**](#language-used)
   - [**Frameworks and Libraries**](#frameworks-and-libraries)
   - [**Tools**](#tools) 

9 [**Testing**](#testing)
   - [TESTING.md file](TESTING.md)

10 [**Deployment**](#deployment)
   - [**Local Deployment**](#local-deployment)
   - [**Clone this project**](#clone-this-project)
   
11 [**Credits**](#credits)
   - [**Content**](#content)
   - [**Code**](#code)
   - [**Media**](#media)
   - [**Acknowledgement**](#acknowledgement)

12 [**Disclaimer**](#disclaimer)

## Project Goals 

This a e-commerce/trip-booking website especially focused on Maltese tourist market. Malta is a nation of just under 450,000 people, yet its infrastructure is required to support over 1.1 million tourists every year.

#### The main target audience of Discover Malta are: 
-	 Inbound tourists aged 25 to 44 years comprised the largest age group of tourists arriving in - Malta in 2020. In that year, roughly 273 thousand international travelers within this age    group visited the country.
-	Families who are looking for children friendly activities
-	Couples who are looking to explore different parts of the island
-	People looking for unique experiences during their holidays
-   Tourists looking to book and organize their holiday before arriving to their destination
-   Tourists and locals looking for last minute deals
 

##### back to [content](#table-of-content)

## UX

### User Goals:

-	Explore different trips which are available during their stay
-	Shortlist their favourite trips
-	Browse through different trips and experiences
-	Be able to navigate the site easily, find what they need and make a safe and secure purchase.
-	Easy and quick checkout
-	Instant email confirmation
-	The website has to be easy to navigate and be responsive across all screen size devices
-	Login procedure should be simple and feedback should be given when appropriate

####  Discover Malta travel site is a great way to meet these needs because: 
-	The site has been designed with the user experience in mind, from easy navigation, responsive design to user feedback guiding them every step of the way.
-	Discover Malta trips can be searched by key words or categories giving the user freedom to explore their desired destination
-   The user is also able to sort trips by different cretirias like (price, reviews, family friendly and duration)
-   Once the user is logged in, they will be able to shorlist trips and view them in their profile
-	Easy and quick checkout process with instant email confirmation
-	User may access their tickets via Profile portal
-   Login procedure is designed with user goals in mind, allowing the user to login with their email address, reset password and update their profile.


### Client Goals
A potential client which chooses to collaborate with Discover Malta might want to 
-	Advertise their trips on the web
-	Showcase their experience to the potential clients 
-	Sell their tickets on the web 
-	Increase their business demand 
-	Reduce their overheads

#### Discover Malta travel site is a great way to meet these needs because: 
-	A potential client can easily request more information by filling in the contact form.
-	Discover Malta offers low commission rates, custom design and availability.
-	The client may also increase or decrease their trip availability at any time. 


### Business Goals
•	Provide a professional online booking platform that helps the user to feel safe that they are buying from a trustworthy source.
•	Build brand awareness by including all the branding photographs, colours, fonts and logo associated with Discover Malta brand.
•	Connect with users of the platform via social media channels
•	Keep track of sales data to inform future trip choices.
•	Make sales of products easy for buyers to increase sales conversion.
•	Engage with users by asking them to supply their trip reviews
•	Drive traffic and create awareness by advertising on social media channels 
•	Supply a platform for small business owners to advertise and increase their sales

##### back to [content](#table-of-content)

### User Stories 

#### First Time User

1.	As a first time user, I want to understand what this site is about.
2.	As a first time user, I want to browse through the trips available on site.
3.	As a first-time user, I want to see full trip details and trip reviews from other users.
4.  As a first-time user, I want understand the benefits of booking my holiday itinerary with the provider.
5.  As a first-time user, I want to add the trips which I like to my favourites.
6.  As a first-time user, I want to find a variety of experiences suited for different ages and requirements.
7.  As a first-time user, I want to navigate the site easily and view side on different screen sizes.
8.  As a first-time user, I want have a good overview of what site has to offer and then click on the button to view more information about a specific trip if interested.

#### Returning User 

1.	As a returning user, I want to be able to login into my account
2.	As a returning time user, I want to view my favourites and check their availability
3.	As a returning user, I want search for a specific trip or filter trips by category.
4.	As a returning user, I want to learn more about the site.
5.	As a returning user, I want to purchase the trip with secure checkout.
6.	As a returning user, I want to get an instant email confirmation of my transaction.
7.	As a rerurning user, I want to have feedback provided to me every step of the way.
8.	As a returning user, I want to view my ticket in my profile page.
9.  As a returning user, I want to be able to save my information to my profile for quick and easy checkout next time.



#### Frequent User

1.	As a frequent user, I want to customize my profile page
2.	As a frequent user, I want to view my previous orders
3.	As a frequent user, I want to review the trips which I have been on. 
4.	As a frequent user, I want to be able to update and delete my reviews.
5.	As a frequent user, I want to follow the site on social media.
6.	As a frequent user, I want to be able to contact the site owners if I have an enquire.
7.  As a frequent user, I want to explore latest deals
8.  As a frequent user, I want my information to be pre-filled on the checkout page.


##### back to [content](#table-of-content)

### A Potential Client
1.	As a potential client I want to see sample of trips to get an overview of what my product might look like
2.	As a potential client I want to learn what benefits are available to me
3.	As a potential client I want to easily get in touch with the site owners to request further information or book a call

### Business goals

1.	As a business owner, I want to provide a platform for users where they explore what Malta has to offer and book their trips during their stay on the island.
2.	As a business owner, I want the user to be able to register with secure login details.
3.	As a business owner, I want the client to be able to use the site easily on any device.
4.	As a business owner, I want to provide useful links to users where they can purchase products and earn an affiliate commission. (shop)
5.	As a business owner, I want to be able to delete any reviews which I consider to be inappropriate or out of content.
6.	As a business owner, I want to be able to add additional new trips to the site. 
7.  As a business owner, I want to be able to edit or delete trips.
8.  As a business owner, I want to provide the user with search and filter functionality for products to enable easy access to the database.



##### back to [content](#table-of-content)

## User Requirements and Expectations

### Requirements:

-	Easy to navigate the site by using buttons
-	Appealing profile page with a functional overview
-	Easy way to view other users reviews 
-	Easy way to add own review 
-	Ability to edit and delete their entities 
-   Secure checkout procedure 
-   Able to save the details for next time  
-   Short list trips
-   For the site to give feedback on interaction


##### back to [content](#table-of-content)

### Expectations: 
 
-	Full trip description
-	Ability to filter trips by category 
-	Ability to search the database for a specific trips by key words
-	Ability to read other users reviews and add their own 
-	Ability to contact the site owner
-   Ability to cancel a trip within given period of time 


##### back to [content](#table-of-content)

## Design 

### Colour Scheme 
![Color Pallete](readme-files/images/luzzu-boat.png)

-	The colour palette inspiration has come from Luzzu, they date back to the time of the ancient Phoenicians. This gives the site an authentic look and feel
-   The colour codes used on the site:

| Colour:  | Blue    | Orange  | Red     | Green   | White    | Black   |
| :------: | :-----: | :-----: | :-----: |:------: | :------: | :------:|
| Code:    | #2576da | #da8925 | #ef1018 | #039b2b | #fafafa  | #000000 |


##### back to [content](#table-of-content)

### Typography
      
 [Google Fonts](https://fonts.google.com/) have been used on this page 
    - To give consistency to the users, consistent fonts have been used throughout the site:

      - All the headings are displayed in font-family: 'Acme', sans-serif;

      - All other elements are displayed in font-family: 'Oxygen', sans-seri;
    

##### back to [content](#table-of-content)

### Imagery

- Carousel images in the index.htm have been sorced from [Pixabay](https://pixabay.com/):

  - Catamaral image [by dimitrisvetsikas1969](https://pixabay.com/photos/catamaran-sea-boat-tourism-blue-2329770/)
  - Gozo image [by waldomiguez](https://pixabay.com/photos/gozo-island-port-malta-water-sea-1139812/)
  - Marsallok [by John Hoefer](https://pixabay.com/photos/boats-port-sea-town-village-5946304/)

- Category Images:

  - Last minute deals [by veerasantinithi](https://pixabay.com/photos/summer-travel-vacation-holiday-2880261/)
  - Fishing [by dimitrisvetsikas1969](https://pixabay.com/photos/fishing-boat-fisherman-sea-fishing-5736839/)
  - Adventures [by Pixels](https://pixabay.com/photos/woman-jump-backpack-jumping-leap-1868817/)
  - Water activies [by Pixels](https://pixabay.com/photos/woman-kayaking-boat-canoe-canoeing-1867074/)
  - Boat trips [by dimitrisvetsikas1969](https://pixabay.com/photos/sea-water-boat-ship-travel-3703094/)
  - Food and Wine [by atanaspaskalev](https://pixabay.com/photos/luxury-food-wine-rose-starter-4330593/)


- Trip Images:

   - Walking food tasting trail in Valetta from [malta.com](https://www.malta.com/media/en/dining/restaurant/mosta/ta-marija/maltese-platter-at-ta-marija-mosta.jpg)
   - Ta'Mena Wine Tours [by bedrck](https://pixabay.com/photos/wine-napa-valley-vineyard-napa-1938924/)
   - Blue Grotto and Marsallock half day tour from Valetta [by PICNIC-Foto-Soest](https://pixabay.com/photos/market-fish-fish-market-food-fresh-897990/)
   - Fishing Day Charter [by scottgardner](https://pixabay.com/photos/key-west-florida-fishing-angling-848209/)
   - Fishing Trip Malta and Gozo [by photo-graphe](https://pixabay.com/photos/fish-fishing-fishermen-food-water-1544819/)
   - St Paul's Bay [by kmarius](https://pixabay.com/photos/snorkeling-sea-water-snorkel-ocean-5222196/)
   - Malta: Gozo, Camino and Blue Lagoon Trip [by Marrit1991](https://pixabay.com/photos/crete-boat-sea-fishing-boat-2152796/)
   - Gozo Full Day Jeep Tour with Lunch [by dimitrisvetsikas1969](https://pixabay.com/photos/jeep-vehicle-off-road-adventure-1461830/)
   - Harbour Cruise [by user32212](https://pixabay.com/photos/lighthouse-harbor-port-bay-sky-2482778/)
   - Segway [by Republica](https://pixabay.com/photos/segway-people-ride-sunset-group-88961/)
   - Stand up paddle board yoga [by Trex7875](https://pixabay.com/photos/yoga-on-water-lake-woman-1362019/)
   - Kayak Gozo and Camino [by dimitrisvetsikas1969](https://pixabay.com/photos/canoe-kayak-sport-water-sport-1405961/)

- Default User Profile Image:
   
    - Defaul User Image [by Peggy Marco](https://pixabay.com/illustrations/key-access-password-code-1013662/)

- 404.html Background Image:

   - Winter Tree Image [by EvgeniT](https://pixabay.com/photos/winter-tree-bench-field-snow-field-3974511/)


- 500.html Background Image:

    - Lightnening Image [by Felix Mittermeier](https://pixabay.com/photos/lightning-thunderstorm-super-cell-2568381/)

- Favicon:
     
     - Sun in sunglasses [by OpenClippart_Vectors](https://pixabay.com/vectors/sun-cool-sunshine-glossy-smile-151763/)



##### back to [content](#table-of-content)

### Icons

- All the icons on site have been imported from 
[fontawesome](https://fontawesome.com/) library

##### back to [content](#table-of-content)

### Style 

- Subtale box shadow has been applied elements which needed emphasis like, cards, forms.

- In case where an area is clickable, for example links or call to action buttons, the shadow size in increased and animated when the user hovers over the element, this was done to make the area more tempting to click.

- Curved coners styling has chosen for its friendly feel, and as it is common stylistic choice of bootstrap it blends well with style used from that library.

- Call to action buttons and cards all have a black border around them to make them stand out against a nutural background.

- <em>Bootstrap Carousel</em> has been implemented on the home page to display the images of Malta.

- <em>Bootstrap Card</em> was utilized to display a short description of each trip. The card has been also used to display trip reviews with custom sizing of the card.

- <em>Bootstrap Modal</em> has been used for defensive programming when the user is trying to delete a review or a trip to alert the user of their action and ask to confirm their choice. Also modal is used to add trip to the basket by selecting the number of tickets and the date.


##### back to [content](#table-of-content)

## Wireframes Flowchart and Data Model

### Wireframes 

- I have used [Balsamiq](https://balsamiq.com/) to create wireframes for Discover Malta.
- You can view my wireframes [here](https://github.com/marina601/discover-malta/tree/master/readme-files/wireframes)

- I have diverted from my wireframes during the development process to create a better user experience:

- <em>Home Page</em>

- Instead of listing the reasons why the user should use this site to shop for thier holiday antinary, I have created a simple animation using JavaScript to give the user a good visual effect and overview of the benefits they will get whilest using the site.

- <em>Trip Detail Page</em>

- In the original design I wanted to implement a google map which will show to the user the route overview of their trip, due to tight schedule, this feature is still left to be implemented

- I have added a form which lets the user to rate and submit a trip review, based on 2 conditions. One - the user mast be logged in and the other the user mast purchase the trip before they review it.


##### back to [content](#table-of-content)

### Database model

I have used (django extentions)[https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16] to generate a database model diagram

![Database model](readme-files/images/database-model.png)


##### back to [content](#table-of-content)

### Flow Chart




##### back to [content](#table-of-content)

## Features 

### Features Implemented 

- Based on the user stories and expectations, the following features have been implemented:

### All Pages 

#### Navbar

- Dynamic navigation menu collapses on the mobile and tablet screen view. The navigation links contain site name which is linked to the Home Page. 

![Descktop-navigation](readme-files/images/main-nav-desktop.png)

- Main Navigation is centred on the desktop with links to Home, Trips and Categories. This navigation collapses into the burger button on the mobile view.
- Trips link contains a link to all trips
- Category link is a dropdown menu which is dynamically generated based on all the categories in the database and links to each category page.

     - {% for category in links %} <li><a class="dropdown-item"href="{{ category.get_url }}">{{ category.category_name|capfirst }}</a></li>{% endfor %}

- Navigation features 3 icons for user avitor, suicase for their trips and a hart icon for trips which user can add to their favourite list. 
- User icon contains a dropdown menu for non-logged user to Login and Register
- For Registered Users, user icons turns into a default user image or if updated by the user, user profile image
- Registered user-image contains a dropdown menu to Profile page and Logout.
- A logged in user will be able to add their chosen trips to their favourites, the number will increment, and the colour of the hart will change. 
- If a non-logged in user will try to add trips to favourites, they will be prompted to login or create an account.

![tablet-navigation](readme-files/images/navigation-ipad.png)

- Suitcase icon - once a user will add any trips to their suitcase(bag) the colour will change to orange and the total value of their suitcase will be displayed accross all the pages.
- Navbar is fixed to the top of the page accross all screen sizes.


#### Footer

- Footer is available to all users at all times.
- The design is simple and manimalistic, not to distract the user experience. 
- The footer contains 2 main links: 
    - Contact 
    - About 
- Also call to action “Follow Us” with social media icons displayed at the bottom of the page. 
- Social icons are linked to social platforms as an external link.
- The footer features the copyright information for Discover Malta, which is generated and updated automatically using JavaScript 


#### General Features
  
- The website has a responsive design based on the screen view.
- Nav bar and footer background colour is black to give the user a cle
- All pages have call-to-action buttons to give the user easy access to the next page.
- Favicon Icon is present for windows and apple devices to improve user experience. 
- Page title to each page has been added dynamically through Django template in the base.html
     - `<title>Discover Malta {% block extra_title %}{% endblock %}</title>`
- Each page has its own title added using this block.

#### Buttons

- There are two main classes for the buttons:

     - `class="btn-next"`

- Has been added to all call to action buttons when the user is viewing all pages related trips.

    - `class="btn-dropdown"`

- Has been added to buttons to give a sence of security, once the user is proceeding to checkout page and also when viewing user profile pages.

- Hover effect remained the same for all the buttons.

- Only if the user is updating somethins like a trip or a review the colour of the button is green
- Only when the user is deleting somethins the colour of the button is red

#### Logo

- When the user hover over the logo 'Discover' changes colour to blue.


#### Links Hover effect

- To keep the style consistant throught the site, I have added the same hover effect to footer and navbar links:
    
     -` background-color: rgba(97, 95, 95, 0.6);
        border-radius: 5%;
        padding: 0.5rem !important;
        transition: ease-in-out all .2s;
        -moz-transition: ease-in-out all .2s;
        -webkit-transition: ease-in-out all .2s;`

### Forms

- All forms contain `text-shadow` property to make them stand out to the user.

### Icons

- All icons contain `aria-hidden="true"` elements and `<span class="sr-only">` where appropriate to make the site more accessible for screen readers


#### Toast

- <em>Bootstrap Toasts</em> has been implemented across the whole side to give feedback to the user when an action is performed. 
- This feature assures the user that when an action is taken it is recoreded. 
- The user may dismiss the toast by clicking on the button or the toast notification will be dismissed with 5 seconds.

 
##### back to [content](#table-of-content)

### Home Page

![Index.html](readme-files/images/index.html-image.png)

#### Hero Image

-	The hero carousel consists of 3 images of Malta island to showcase to the user the beautify of the island and what they can discover.
-	The carousel has a time delay function, added `carousel-fade` class to fade each image instead of the traditional slide effect
-   The carousel had `data-bs-touch="true"` which let's the user control the images on touch.


#### Introduction 
-	Consists of a brief paragraph about Maltese history 

#### Benefits
-	The second paragraph consists of the a pitch, why user should book the trip with Discover Malta
-   The benefits are displayed in the form of different colour circles using the colour scheme of the site and `box-shadow` property to make them stand out.
-   The benefits are not visible to the user initialy, on scroll they slide into the page, this was achieved using jQuery `show` function with time delay interval between each element.

#### Categories 
-	At the bottom of the page there is a list of categories which we offer for the user to explore.
-   The categories on the page are displayed dynamicaly from the database.
-   Each category is displayed in the form of a card, with its own image and title.
-   User may click on the category title to view all the trips under that category.
-	Category title contains the same `:hover` effect as link in the navbar and footer

#### Call-to-Action
-	Call to action button “view all trips” displayed at the bottom of the page which will lead the user to explore all the trips available on the site.

##### back to [content](#table-of-content)

### All Trips Page

![trips.html](readme-files/images/all-trips-image.png)

- All trips page features a heading which tells the user they will be able to view all the Trips here

##### Search bar

- Search bar feature is implemeneted which lets the user search for trips by keywords
- If keyword does not exist then a message is displayed to the user telling them to try again.

#### Sort functionality

- Dropdown menu lets the user sort trips by price, rating, duration and if the trip is family friendly
- This features lets user narrow down their search cretiria to their specific needs
- The user also may choose to filter their trips by categories, the categories are generated dynamicaly based on the database entries. They display all the trips belonging to each category by category_slug
- The url has been modifyed using `category_slug` to give the user a better experience and user-friendly appearance.

#### Trip Count

- Once the user lands on trips.html the total number of trips availabe in the database are displayed
- When the user uses search bar or filters the trips by category, the total number of trips dynamically generates the total number of results found.

#### Trip Card 

- Each trip is displayed using <em>Bootstrap Card</em>
- Card-header features add to favourite <em>tooltip</em> hart-icon, which on hover lets the user know they can add the trip to their favourites.
   - Non-logged in users:
      - If the user is not logged in they tooltip displays:
          - "Login to add this trip to your favourites"
      - If the user clicks on the button they will be redirected to the login page

   - Logged in users:
      - Tooltip features a different text on hover:
         - "Add to favourite"
      - When the user clicks on the hart the toast message is displayed letting the user know they have added the trip to their favourite list.
      - The hart-icon in the navbar changes colour to red and displays the total number to favourite trips the user has added to their list.

- Each trip contain an image, trip name, short description and friendly icons are displayed to let the user know the durations, price, star rating and if the trip is suitable for families.

- Image and Trip name both are links to a trip_detail.html for an individual trip.
- Short description gives the user a brief overview of the trip
- Star rating displays to the user average rating for the trip, if there is star rating for the trip, the star icon turns yellow.
- If there is no rating available for the trip, the star icon is balck and message is displayed to the user. 
- If the trip is family friendly, a child icon appears in the card and message is displayed. 
- If the trip is not family friendly, no icon and no message is displayed.
- At the bottom of the card there is a "More Info" button which leads the user to trip_detail page.

- If the user is admin:
    - 2 addition buttons are added to the bottom of the card: "Delete" and "Update" trip.
    - If the delete button is pressed the modal appears to inform the user of their actions and to confirm their decition
    - Update button leads the user to update_trip.html

#### Paginations
    - Pagination buttons are provided depending on the number of results returned from the database with options next_page and previous_page, as well as the page number the user is currently on.



##### back to [content](#table-of-content)

### Trips Detail Page
![trip_details](readme-files/images/trip-details-image.png)

- The user is greeted with trip name and an image of the trip.

#### Add to Favourites Icon
    - In the left hand coner of the image the user has a tooltip like button.
    - The conditions remain the same as trips.html for logged in users and not logged in users
    - If the user is logged in and added the trip to their favourites the icon changes from hart to trash.
    - Tooltip message displayed on hover "Remove this trip from your favourites", letting the user remove the trip by clicking the same button
    - The toast message displays a messages "The trip.name has been removed from your favourites"

- In the right-hand corner the user is presented with a stiky "Book Now" button, this feature has been implemented on purpose to give the user access to the booking modal at any stage, without scrolling upwards to find it.

#### Book Now

- When the user presses the button, a modal with a form appears.
- The user may select the number of adults, children and the date which they would like to go on a trip.
- In the modal header the trip name selected is displayed, to let the user know which trip they are booking the tickets for.
- The price per single ticket is shown to the user.
- The user has the option not to specify the number of children for the trip, however the number of adults has to be selected.
- If only children tickets are selected, the custom validation message appears, letting the user know that at least 1 adult ticket is required to purchase this trip.
- If the trip is not family friendly, the form does not display an input for number of children tickets.
- On form submittions, total number of tickets is calculated and checked against the databse trip.num_tickets. The trip.num_tickets is being reduced.
- If there are not enought tickets in the database available, an error toast message is appearing letting the user know how many tickets are available.
- The user may dismiss the datepicke by pressing close button or a cross located on the right hand side of the modal.

    - ![book-now-modal](readme-files/images/book-now-modal.png)

#### Datepicker:
    - Datepicker widget has been implemented from jQuery library
    - The datepicker has been modified to display the date format django accepts, does not allow the user to pick any past dates and it displays the first day of the week:
          - `$( ".calendar" ).datepicker({
               dateFormat : 'yy-mm-dd',
               minDate : new Date(),
               firstDay: 1,
           });`
     - Datepicker colour scheme has been modifyed to suit the colour scheme of the site 

- This page also features full informatio for selected trip
- Icons are used on this page, similaly to all trips.html page, to display:
        - Duration
        - Start Time
        - Reviews
        - Rating
        - Adult Price
        - Child Price  (if applicable)
        - Family Friendly (if applicable) 

- A paragraph detailing cancellation policy procedure to the users is also displayed

- If the user is admin user:
        - Two buttons are displayed to Update and Delete the Trip

#### Review/Rating

- If the user is logged in:
        - A form is presented to the user letting them easily add the review to this trip.
        - The user may only add the review to a specific trip once this trip has been purchased by the user
        - Otherwise the toast message is displayed to the user, letting them know they must purchase the trip first
        - User must rate the trip and add the review title in order to submit the review
        - Rating is accepted in decimal values with minimum of 0.5 and maximum of 5 star rating
        - Star rating are displayed in the form via radio input fields, which are hidden and their labels are being transformed into font awesome stars.
        - The stars are highlighted on hover using css styling
        - Custom validation message is added to review title and displayed to the user if not entered.
        - Once the form is valid and submited, there are two checks:
            - If the user has already submitted the review for this trip, the review gets updated
            - If this is a new review, a review gets created
            - A function in the "trips.models.py" calculateds the average rating and total number of review if applicable.
        - The page refreshes, the total number of review is updated and average star rating.
        - User reveiw is displayed.

- If user is not logged in:
        - The form is not displayed.
        - A message displayed to the user instead prompting them to login and rate their experience.

- Review field is not required, as many users do not like to write a long review, by simplifying the process the site would gaine more reviews from users.

    - ![review-form](readme-files/images/add-review-img.png) 

#### Reviews

- Reviews are displayed for a specific trip in form of the bootstrap cards
- To keep the card styling consistant they benefit from the same box shadow property as the card-trip
- Min-height property is added to the card to keep the elements the same heigh and consistant
- Total number of review also displayed to the user to let them know how many reviews are there for this trip
- The reviews are displayed in descending order, newest one first
- The review card consist of review title, star rating which is displayed in form of the star icons and value condition to give colour to the stars:
        - `<i class="fas fa-star{% if review.rating == 0.5 %}-half{% elif review.rating < 1 %}-o{%endif%}" aria-hidden="true"></i>`
- If there is an actual review it will be displayed.
- In the footer of the reveiw card, user icon is displayed together with user.first_name.
- The date is formated in the template to give the user a better visual effect:
        - `{{ review.created_at|date:"M d, Y" }}`
- It also let's the user know if this review has been updated or just created, as it tracks user updates in the databae

- If the user is logged in and created a review:
        - They are able to see Edit and Delete button in their review card
        - The user may click Update button which will lead then to pre populated form with their review 
        - The user may click Delete button which will display a modal asking them to confirm their decition
        - If Review is deleted the quantities are being updated and toast message is displayed to the user 

- If there are no review for this trip, a message is displayed letting the user know this trip has not been reviewed yet.

- ![reviews](readme-files/images/reviews-images.png)

##### back to [content](#table-of-content)


### Add Trip Page
    - This feature is available only for admin users
    - They can access this page from their profile page, where the link is displayed
    - The page contains a form and asks the user to fill in the required information
    - If the form is valid the data is stored in the database and the user is redirected to trip_details page, where they can reveiw the trip created
    - Toast message also displayed letting the user know they trip has been added to the database.
    - Admin user may choose to edit or delete the trip from this page.
    - If a not logged in user tries to acces this page, they will be redirected to the login page.
    - If a user is logged in, but not admin tries to access this page they will see the message displayed that they do not have permission to access this page.

##### back to [content](#table-of-content)

### Update Trip Page
    - This feature is available for admin users only
    - They can access this page from trips.html or trip_detail.html pages, where update button is displayed
    - The link takes the admin user to the pre-populated form with the trip they choose to edit.
    - Alert in the form of toast appears on the page letting them know which trip they are editing
    - Form erros are displayed to the user if the information entered is incorrect
    - Once the form is submitted, the admin user is being redirected to the trip_detail.html to check the information entered.
    - Admin user may choose to edit or delete the trip from this page.
    - If a not logged in user tries to acces this page, they will be redirected to the login page.
    - If a user is logged in, but not admin tries to access this page they will see the message displayed that they do not have permission to access this page.
 

### Delete Trip
   - This feature is available for admin user only
   - The admin user may delete a specific trip from trips.html or trip_detail.html, where the buttons are located
   - When the button is triggered, a modal appear asking the user to confirm their decision.
   - Once the trip is deleted the alert message in form of toast appears letting the user know the trip has been deleted.
   - Once the 'delete' button is pressed the trip is being deleted from the database

- ![delete-trip-modal](readme-files/images/delete-trip-modal.png)

##### back to [content](#table-of-content)

### Login Page 

![login-page](readme-files/images/login-page-img.png)

- The login page features a standard login form asking user for their email address and password.
- Validation is handled in the back end and relevant information is provided to the user on validation.
- Once the user is logged in, they are being re-directed to "Home Page", toast notification welcomes the user and user icon in the navbar changes to default user image or logged in user image. 
- If the user forgot their password, they have an option to click on the link 'click here to reset your password', which will take them to the reset_password.html
- If the user is not regitered, they have a link which they can click and it will take them to the register.html


##### back to [content](#table-of-content)

### Registration Page

![registraion-page](readme-files/images/registration-page.html.png)

- A non logged in user may access this page by pressing on the user icon at the top of the nav bar
- A simple form is presented to the user , with text helpers to guide the user through the registraion process
- The use needs to provide, first name, last name, email address, phone number and password
- Validation is handled by django forms and relevant feedback is provided along the way to the user.
- On successfull submittion of the form, a user will be redirected to login page, where a condition is checked:
     - `{% if request.GET.command == 'verification' %}`
- And the message is displayed to the user telling them the verification email has been send to their email address.
- Verification email is being sent using <em>Gmail</em> account settings.
- User gets a unique link sent to their email address generated by `uid` code and django default `token` generator.
    - `message = render_to_string(
                'accounts/emails/account_activation.html', {
                    'user': user,
                    'domain': current_site,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                }
            )` 
- If they have already activated their account they can click on 'Login' button to login
- If the email already exists in the database, the registration will fail
- If the user has already registered, they can access login page by clicking on the link below
- If a logged in user tries to access the profile page, they will be redirected to their profile page and info toast message will appear, letting them know they have already registered.

##### back to [content](#table-of-content)

### Forgot Password Page

- If the user has forggotten thier password they may click on the link which is located on the login page
- A simple form will ask the user to enter their email address
- A check is completed in the back end to identify the email address in the database
- If the email address exists, an email is generated and send out to the email address entered
- A toast notification lets the user know the email with a link has been sent to their email address
- If the email address does not exist in the database, the user is notified via toast notification.

##### back to [content](#table-of-content)

### Reset Password Page

- When the user clicks on their reset password link, they are being redirected to reset password page
- Where the form is asking them to create a new password and confirm password
- Validation for the form is done in the back end, ensuring the 2 passwords match, and front end, setting the min-lenght for the password, which matches the orginal registration form.
- If the passwords do not match the toast notification will display the error to the user
- Once the form has been successfully submitted, toast notification will inform the user and redirect them to login page, where they can login to their account with their newly created password

##### back to [content](#table-of-content)

### Logout

- Any userwho clicks on "Logout" link from the navigation bar is automatically logged out and their session data cleared. They are taken to a "Home" page, toast notification informs the user they have been logged out.

##### back to [content](#table-of-content)

### Profile Page

![profile-page](readme-files/images/profile-page.png)

-  User profile page can only be accessed by a logged in user. Any user not logged in who tries to access this page will be redirected to the login page.

#### Logged in user 
-	Once logged the user can click on the user icon to access their profile page
-	They will be greeted with a welcome message which will user their username for authentication
-	Default avitor/ or user profile image will be displayed.
-	Not to clutter the page, I have chosen to display 4  button to tell the user what they can do on the page 
-	Each button takes them to the relevant information they wish to view.
-   Ancor link in the form of the button take the user to the order history, which is displaye at the bottom of the page.
-   I have decided to keep the order history on their profile page, as the user most likely to need this information more than any other.
-   Past order history is presented in the table format, displaying order number, date, items purchased and order total amount.
-   The orders are displayed in descending order
-   The user may click on the order number to view full order.
-   The user will be notified via toast notification, that they are viewing a past order and confirmation email has been send on the date of purchase.

#### Admin User 
-	An admin user will be have an extra option "Add Trip" which will lead them to a add-trip.htm where they will be able to add a new trip to the database.

##### back to [content](#table-of-content)

### Edit Profile Page

- Edit Profile Page features a message letting the user know that they can edit their information here
- User Profile image/ defaul image displayed in the middle 
- The form is pre-filled with user information
- They user has the ability to edit their information and update their profile image
- When the form is submitted, toast message displayed letting the user know their info has been updated and the user is being redirected back to the "Edit Profile Page" which shows their updated information.
- The button in the end of the page lets user easily go back to their profile

##### back to [content](#table-of-content)

### View Reviews Page

![manage-reviews](readme-files/images/manage-reviews-page.png)

- Navigating from the user profile page by clicking on the button "Manage Reviews", the user is able to view all their reviews in the form of cards
- Here the user may choose to edit their review by clicking on "Edit" button 
- Or delete their reveiw by clicking on "Delete" button
- If pressed on "Delete" button it will trigger a delete-review-modal which will ask the user to confirm their request.
- If the user has not reviewed any trips yet, the appropriate message will be displayed notifying the user that they do not have any reviews yet.

##### back to [content](#table-of-content)

### Edit Review Page

![edit-review](readme-files/images/edit-review-page.png)

- Navigating from "View Reviews Page" by clicking "Edit" button the user is being redirected to "Edit Review Page"
- Toast notification lets the user know which trip review they are editing
- Message at the top of the page lets the user know what action they can perform
- Current star rating is displayed in the form of numbers
- The user may update their star rating by clicking on the relevan star
- The user may update their review title and review.
- Once the form is valid and submitted the user is being redirected to "View Reviews Page" where they can view their updated review.
- Updated review date also automatically changes to the current date.

##### back to [content](#table-of-content)

### Favourites Page

- A logged in user may access their favourites page by clicking on the hart icon in the navigation or from their profile page
- If the user has favourites the list of the favourite trips displayed in the same format as trips.html
- If the user does not have any favourites added to their list yet, the page displayes a relevant message with a link for the user to go to "All Trips Page"
- On this page, instead of the hart icon the trash icon is displayed on top of each trip-card, which is a tooltip feature and on hover lets the user know they can remove this trip by clicking on the icon
- The user may view "Trip Detail Page" for a selected trip by clicking on the trip image, name or "More Info" button
- Conviniently the user has an option at the bottom of the page to go back to thier Profile Page by clicking on the link supplied.

##### back to [content](#table-of-content)

### View Bag Page

![view-bag-1](readme-files/images/view-bag-1.png) | ![view-bag-2](readme-files/images/view-bag-2.png)

-	The user will have access to their bag by clicking on the basket icon in the main navbar 
-   If there is not items in the bag, a relevant message is displayed on the page with a link to "All Trips Page"
-	The  user is greeted with a heading identifying the page clearly
-   The Travel Bag Page features a summary of all the trips the user has added their suitcase
-	Each list item icludes trip image, duration, star time, departure location, rating(if applicable), number of tickets selected, price for a specific number of tickets based on their category (adults/children), total ticket quantity, selected booking date and sub total.
-   If the user clicks on the title of the trip, they can have a link to go to "Trip Details Page" to view more information
-	The user is able to modify the date and the number of people selected for the trip
-	The user can update their choice by pressing the button “Update”
-   If the user sets the number of adult tickets to 0, the trip will be automatically deleted from the bag
-   If the user sets the nubmer of adult tickest into negative value, a JavaScript alert is displayed letting the user know they need to have at least 1 adult selected for this trip.
-   The user is able to set the amount of children tickets to 0, however if the value is going into a negative value, the minus button fades out for 5 seconds.
-   The minus button fades out for 5 seconds
-   If the user selects more than 8 adult or children tickets, JavaScript alert appears to let the user know they need to get in touch with the site owner for large group bookings.
-   The plus button fades out for 5 seconds
-   The user is able to update the trip date by clicking on their selected date, jQuery date picker opens with current date highlighted and their selected date highlighted in blue.
-   Once the user pressed on "Update" the page refreshes and the new totals are calculated and displayed.
-   Once the user presses on "Delete" button, modal is triggered, on the confirmation is recieved the trip is removed from the bag.
-   The number of tickets which have been deleted goes back to the total trip number of tickets available to purchase.
-   Toast notification provides feedback to user on update and delete functionality.
-	The user is able to see the grand total of their order on this page and below the icon of suitcase in the navigation menu. 
-	Two button at the bottom of the page “Keep Shopping” which will redirect the user to the trips page or “Proceed To Secure Checkout” which will take the user to the next page “Checkout”
-   On the mobile screen view the "Checkout Button" is positioned at the top of the page and has `position: stiky`, this feature has been added as the trip summary can get quite big and the user may not want to scroll to the bottom of the page to find a checkout button.


##### back to [content](#table-of-content)


#### Checkout Page

![checkout-page](readme-files/images/checkout-1.png) | ![chekout-page-2](readme-files/images/checkout-2.png)
-  Each checkout pagefeatures an order summary, which lists all the items in the users suitcase, image, trip name, number of tickets, adult price, child price (if applicable), booking date and total price.
-  User will be able to click on trip name which will take them to "Trip Detail Page" if they would like to view more information about the trip.
-	Once the user decides to checkout, they will be asked to complete a form and fill out the relevant details to complete a card transaction

#### If the user is logged in 
      - If the user is logged in and has their profile details the checkout form will be pre-filled
      - If the user does not have their details saved to their profile, they will be asked to fill in the relevant information in the form.
      - The user will be able to save their details for next time by clicking on check box, which will store their information in their profile page.
   
#### If the user is not logged in
      - The check box to save user info will not be available, instead they will be asked to Login or Register to save their information for easy checkout next time and view their order history in their profile page.
   
   
-   A user may use this page as an annonimouse user for one of checkout, or as a existing logged in user who will be able to view their order history in their profile page.
-   The form is devided in 3 parts, one for user personal info, another one for their card registered address and the last one for their card number
-   Each form element has a placeholder to guide the user during the form submition
-   All the required input fields have added * to their placeholders
-   Auto focus attribute is set to user first name field
-   When the user selects the Country field, a nice feature from django fields 'CountryField' has been imported, which displays all the countried and lets them select the country from the list.

#### Stripe
-	The user will be asked for their card details, which will be authenticated by Stripe.
-	Stripe detects what card is it and displays the relevant icon (like visa or mastercard)
-   Stripe will display errors on the page for the user if there are any
-   Using JavaScript I have modifyed default stripe input field and have hidden the zip code part, as it is mainly used in US and it is not applicable to the European market.


-	A message at the bottom of the page will tell the user how much is being charged on their card
-	The user has two options at this point, press “Complete Order” button and the payment will be made to Stripe or “Adjust Order” button and the user will be redirected to the “View Bag Page” page, where they will be able to amend their order.
-  Once the "Complete Order" button is pressed, a ovelay will cover the whole page and the user will see a loading spinner which will tell them the payment is being proccessed.
-  On successfull payment submittion the user will be redirected to "Checkout Complete Page"

##### back to [content](#table-of-content)


#### Checkout Success Page

![checkout-ipad](readme-files/images/checkout-complete.png) | ![checkout-mobile](readme-files/images/checkout-complete-mobile.png)
  -  Checkout success page will be displayed once the payment has been successfully completed.
  -  Toast notifications will let the user know the email has been send to the email address provided during the checkout process.
  -  At this stage, an email has been automatically generated and send to the user with their full order details.
  - Order summary is displayed and ticket number is randomly generated, which will act as a ticket number for the trip.
  - The user will able to access this number in their profile page and present it as a proof of purchase to the trip organizer.
  - The user will be able to view all the personal information which they have entered in the contact form on this page as well, to give them a chance to check if all the information is correct.
  - A button at the bottom of the page links to "All Trips Page"


##### back to [content](#table-of-content)

### Contact Page
![contact-page](readme-files/images/contact-page.png)
-   The user may access contact page via 'Contact' link located in the footer
-	The contact page consists of a simple form, which user needs to fill out to submit their query. 
-	The user is presentec with a select box to choose their subject, which will act as a subject send to the Admin email address.
-	Custom HTML validation has been written for this page, to guide the user through the required input fields.
-   If the user is logged in, their email address and full name will be pre-filled.
-   If the user wants to leave the page, they may press the button at the bottom of the page which will take them to "Home Page"
-	A toast notification will tell the user their form has been submitted and somebody from the team will be in touch with them shortly.
-	On successful submission of the form the user will be redirected to the home page.
-   Two emails will be send one to the user, letting them know their enquiry has been recieved and one to the admin, which will contain user name, subject, message and email address.
-   Contact form is a simple HTML form, django sends confirmation emails using GMAIL settings.


##### back to [content](#table-of-content)

### About Page
-	About page will tell the user more information about the site, how it started and the mission of the site
-	This page will also tell the potential client why they might want to collaborate with the site and the benefits they will receive once they sign the contract. 
-	About page has two buttons at the bottom of the page “Home” which will redirect the user to the home page and “Contact” which will redirect the user to the contact page

##### back to [content](#table-of-content)

### 404 Error Page

- Custom 404.html has been designed with a picture of the winter day, letting the user know they are off course.
- Message is telling the user "This page does not exists"
- A link "Go Back" will take the user to the "Home Page"
 

##### back to [content](#table-of-content)

### 500 Error Page

- Custom 500.html has been designed with a picture of the lightnening, letting the user something has gone wrong.
- Message is telling the user "There is a problem, while we are looking in to it.."
- A link "Go Back" will take the user to the "Home Page"


##### back to [content](#table-of-content)

### Features Left to Implement 

-	Shop page which will allow the business owner to earn affiliate income 
-	Client profile page, where the vendor of the trip will be able to see all their trips 
-	Checkout page, should have a textarea element where the user is able to add notes to their booking and the vendor will be    able to see them
-	Privacy Policy
-   Google map route overview for each trip on the trip_detail page
-   Weather API to let the user check the weather when they are booking a trip
-   Give the user option to login with their social media accounts
-   About Page
-   Fuctionality to give a specific trip the number of tickets available for a specific day.
-   Set specific days for a trip to be available
-   Implement last-minute category functionality, which would work on the condition whether a provider would like to sell more tickets on a specific day and give the user a specific % of the discount.
-   Subscrition to a newsletter, where the user will be able to recieve an email with weekly offers
-   Availability for user to add tickets to their personal calendar




##### back to [content](#table-of-content)

## Technology Used

### Language Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

##### back to [content](#table-of-content)

### Frameworks and Libraries

1. [Bootstrap]()
 - Mainly for responsive grid layout. Components from this library have been used to structure the website and speed up the build process.

2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Montserrat and Nunito' fonts into the style.css file which is used on all pages throughout the project.

3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

4. [jQuery](https://api.jquery.com/)
    - jQuery library has been used to target HTML elements and assign event listeners throughout JavaScript files.   

5. [Python Templating Language]()
    - Templating language for Python, to simply display data from backend to front end

6. [Django]()
    - As a Python web framework for rapid development and clean design

7. [Stripe]()
- As a payment platform to validate and accept credit card payments securely

8. [AWS S3 Bucket]()
- To host the static files for this project

9. [Django Crispy Forms]()
- To style Django Forms 

10. [Gunicorn]()
- WSGI HTTP Server for UNIX to aid in deployment of the Django project to Heroku

11. [Psychopg2]()
- As PostgreSQL database adapter for Python

12. [PostgreSQL] ()
- Database used for production, provided by Heroku

13. [SQlite3]()
- Database used for development, provided by Django

##### back to [content](#table-of-content)

### Tools  

1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.

2. [GitHub:](https://github.com/)
    - GitHub is used to store the project's code after being pushed from Git.

3. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.

4. [TinyPng:](https://tinypng.com/)
   - TinyPng was used to compress the size of the images and improve loading time.

5. [Lucid Chart](https://www.lucidchart.com/)
  - To create a flow chart and database structure 

6. 

7. [Grammarly](https://www.grammarly.com/)
    - Used to fix the grammar errors across the project.

8. [Gitpod](https://www.gitpod.io/)
    - Used as the development enviroment.

9. [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
    - Used as a primary method of fixing spacing issues, finding bugs, and testing responsiveness during the project development.

10. [Befunky](https://www.befunky.com/)
    - Online platform used to resize and crop images.

11. [Heroku](https://heroku.com/login)
   - A cloud platform as a service enabling the deployment of the site

12. [PEP8](http://pep8online.com/)
   - Validate Python code

13. [W3C HTML Validation Service](https://validator.w3.org/)
    - Validating HTML code

14. [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - Validating CSS code

15. [JSHints](https://jshint.com/)
    - Validate JavaScript Code

15. [Am I Responsive](http://ami.responsivedesign.is/)
   - Used to view the project on different screen sizes and determine the responsiveness of the site. Also used it for screenshots in Readme.md file

16. [Link Checker](https://validator.w3.org/checklink)
   - To validate all the links of the site

17. [Secure Password Generated](https://randomkeygen.com/)
  - To generate a secure password for my **SECRET_KEY** in *env.py* file

18. [Extendclass](https://extendsclass.com/python-tester.html)
  - To check syntax errors in **Python** code.

19. [HTML5 Closing Tag Checker](https://www.aliciaramirez.com/closing-tags-checker/)
  - Used this tool to find missing tags

20. [Lampada Test](https://app.lambdatest.com/console/realtime)
  - Used this tool to help with cross-browser compatibility test 


    
##### back to [content](#table-of-content)


## Testing

You can find testing information in [TESTING.md](TESTING.md)

##### back to [content](#table-of-content)

## Deployment

### GitHub
- Create GitHub Repository using the CI Full Template.
- Create a development branch (master + development).
- Configure Visual Studio Code environment
- New Window.

### Clone Repository -> GitHub -> Discover Malta.
- Select development branch.
- Create a virtual Python environment - Terminal: python3 -m venv .venv
- Activate virtual Python environment - Terminal: source .venv/bin/activate
- Install Django 3.1 - Terminal: pip3 install Django
- Upgrade pip - Terminal: pip3 install pip --upgrade
- Check Django version - Terminal: python3 -m django --version = 3.1.7
- Update .gitignore to include .venv and /Snippets(my local test and fail code directory).

### Create the Initial Django Project
- Create a Django Project called "discover-malta" - Terminal: django-admin startproject discover-malta . (created in the current folder)
- Verify that the initial Django project works - Terminal: python3 manage.py runserver 8000, [url]
- Django Migrations (Version Control System for the Database Schema)
migrate, which is responsible for applying and unapplying migrations.

- makemigrations, which is responsible for creating new migrations based on the changes you have made to your models.

- sqlmigrate, which displays the SQL statements for a migration.

- showmigrations, which lists a project’s migrations and their status.

[Link](https://docs.djangoproject.com/en/3.1/topics/migrations/)

- Apply the initial Django migrations: python3 manage.py migrate, add --planto validate before commit.
- Create Django Admin superuser account: python3 manage.py createsuperuser, gaff, naoise.gaff.gaffney@gmail.com, `password...
- Configure static and media for Django
- Create the media folder in the Project root.
- Create the static folder with the following sub-folders: scripts (js), scripts/vendors (vendor js), styles (css).
- Configure 'settings.py' and 'urls.py' to accommodate the static and media folders.
- Install django-environ to read a '.env' file with both confidential and useful variables -> Heroku Variables and - PyTest Variables
- [Link](https://django-environ.readthedocs.io/en/latest/)
- Install: pip3 install django-environ.
- Configure settings.py to use django-environ and copy .env file from previous Django Project.

###  Heroku Platform Configuration and Deployment
- Install gunicorn: pip3 install gunicorn, create requirements.txt using pip3 freeze > requirements.txt, and create the Procfile: web: gunicorn myshop.wsgi:application.
- Create .slugignorewith /Documentation and README.md as we don't want the documentation to upload to Heroku.
Heroku.

#### VS Code Source Control: Stage All Changes -> Commit All -> Push.
- Create a new Pipeline: discover-malta and connect to GitHub Repository [github url]
- Enable Review Apps: Create new review apps for new pull requests automatically and region: Europe -> GitHub. New App -> GitHub development branch. Name: training-and-development-<random sequence>
- Add app to Heroku Staging (GitHub). Create new app: Create new review apps for new pull requests automatically and region: Europe -> GitHub. New App -> GitHub master branch. Name: training-and-development.
- Add app to Heroku Production: Europe -> GitHub. Name: training-and-development-prod.
- Add DISABLE_COLLECTSTATIC = 1 to Review App, Staging App, and Production App Configuration Variables (temporary until AWS S3 Bucket configured).

### Herokue Config Vars (minus DISABLE_COLLECTSTATIC=1 which is a temporary variable)
- Heroku Config Vars
- Create a table here of config vars

#### PostgreSQL Configuration
- Install PostgreSQL support: pip3 install psycopg2-binary and pip3 install dj-database-url.
- Update the Heroku requirements file: pip3 freeze > requirements.txt
- Add PostgreSQL add-on on Heroku under Application -> Resources -> Add-ons: Heroku Postgres (free / hobby tier). - - Heroku adds a DATABASE_URL variable under Application -> Settings -> Config Vars. Copy this URL.
- Add the URL to the '.env' file: DATABASE_URL=<Database URL>. Update 'settings.py':
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

#### Migrate the Django Models to the PostgreSQL Database:
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py createsuperuser

#### Update the allowed hosts in 'settings.py': ALLOWED_HOSTS = [os.environ.get('ALLOWED_HOSTS')].
- VS Code: Create the commit message. Changes -> Stage All Changes, Commit -> Commit All, Push.

#### AWS S3 Bucket Configuration
- Create an account on AWS.
- Add and configure the AWS S3 Bucket: trainingdjango, All public access. ACL: Everyone Objects -> List.
- Create the Bucket Policy.
- Create the Cross-Origin Resource Sharing (CORS)
- Access AWS IAM and create a user for the Training Project. Create a group, with the user attached. Download the - - CSV file with the credentials and save it in a safe place. Updated the '.env' file with the relevant variables.
- Execute python3 manage.py collectstatic to upload static files to the AWS S3 Bucket.
- Upload the 'media' folder and files manually.
- Remove DISABLE_COLLECTSTATIC variable from Heroku Config Vars.


### Local Deployment

- I have created Discover Malta using Github, from there I used Gitpod to write my code. Then I used commits to git followed by "git push" to my GitHub repository. I've deployed this project to Heroku and used "git push Heroku master" to make sure my pushes to GitHub were also made to Heroku.

- This project can be run locally by following the following steps: ( I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE. You can find more information about installing packages using pip and virtual environments [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

##### back to [content](#table-of-content)


## Credits

### Content



##### back to [content](#table-of-content)

### Code




### Media



##### back to [content](#table-of-content)

### Acknowledgement 



##### back to [content](#table-of-content)

## Disclaimer 

- This website has been created for educational purposes only 

##### back to [content](#table-of-content)