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
   - [**Registration Page**](#registration-page)
   - [**Login Page**](#login-page)
   - [**Profile Page**](#profile-page)
   - [**Edit Review**](#edit-review)
   - [**Products Page**](#products-page)
   - [**View Product**](#view-product) 
   - [**Add Product**](#add-product) 
   - [**Edit Product**](#edit-product) 
   - [**Contact Page**](#contact-page) 
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

I have used [Lucid Chart](https://www.lucidchart.com/) to create a database model



##### back to [content](#table-of-content)

## Features 

### Features Implemented 

- Based on the user stories and expectations, the following features have been implemented:

### All pages 

#### Navbar

- Dynamic navigation menu collapses on the mobile screen view. The navigation links contain a logo image which is linked to the Home Page. 
- Main Navigation is centred on the desktop and tablet view with links to Home, Trips and Shop. This navigation collapses into the burger button on the mobile view and remains centred. 
- Trips link contains a link to different categories of the Trips 
- Icon links for User, Bag and Favourites are in the form of icons and appear on the right-hand side of the header. 
- User icon contains a dropdown for non-logged in user to Login and Register
- User icon contains a dropdown for logged in user to Profile and Logout
- A logged in user will be able to add their chosen trips to their favourites, the number will increment, and the colour of the hart will change. 
- If a non-logged in user will try to add trips to favourites, they will be prompted to login or create an account.
- The colour of the footer and navbar remain consistent throughout the site.


#### Footer

- Footer is available to all users at all times.
- The footer contains 2 main links: 
- Contact 
- About 
- Also call to action “Follow Us” with social media icons displayed at the bottom of the page. 
- Copyright information


#### General Features
  
- The website has a responsive design based on the screen view.  
- All pages have call-to-action buttons to give the user easy access to the next page.
- Favicon Icon is present for windows and apple devices to improve user experience. 



#### Buttons


 
##### back to [content](#table-of-content)

### Home Page

#### Hero Image

-	The hero carousel consists of 4 images of Malta island to showcase to the user the beautify of the island and what they can discover.
-	The carousel has a time delay function


#### Introduction 
-	Consists of a brief paragraph about Maltese history 
-	The second paragraph consists of the a pitch and the benefits why user should use the site to book their trips with Discover Malta

#### Categories 
-	At the bottom of the page there is a list of categories which we offer for the user to explore.
-	When the user clicks on the category it will display the trips only by that category.

#### Call-to-Action
-	Call to action button “view all trips” displayed at the bottom of the page which will lead the user to explore all the trips available on the site.

##### back to [content](#table-of-content)






### Registration Page

![registration page](wireframes/images/registration-page.png)



##### back to [content](#table-of-content)

### Login Page 


##### back to [content](#table-of-content)
 
### Profile Page

#### Not logged in user
-	If the user is clicking on the user icon at the top of the page, they will see a drop down option for “login” or “register” links
#### Logged in user 
-	Once logged the user can click on the user icon to access their profile page
-	They will be greeted with a welcome message which will user their username for authentication
-	Default avitor icon will be displayed, if the user chooses to update the avitor icon they can do so by clicking on “Edit” button 
-	Not to clutter the page, I have chosen to display 3  button to tell the user what they can do on the page 
-	“View Booked Trips”
-	A div will be displayed to the user shoving them booking ref numbers, trip name and date. 
-	If the user decides to expand this they will see their ticket will all the information required for the trip 
-	The user may also add a review for the trip which has already passed
-	“View Your Favourites”
-	The user will be able to see their favourite list of trips in the form of cards here
-	If the user clicks on a particular one it will directed to the “Trip by <id>” page where they can proceed to book their selected trip
-	“Update Your Details”
-	The user will be presented with a form where they can update their personal details and save them to the database.

#### Admin User 
-	Will be able to add products to the database



##### back to [content](#table-of-content)

### Trips Page
-	Trips page consists of a heading 
-	Search bar using text content
-	Filter drop down option for categories which user may choose instead of the search 

-	Trip Cards – which contains image of the trips, small description, user rating and ‘view more button’ which will lead the user to the full trip detail page
-	Trip Cards also have add to favourite hart icon which will add the trips to the user profile once they are logged in or will redirect a non-loged in user to login/register page
-	Pagination has been implemented to limit the number of trips to 9 per page

##### back to [content](#table-of-content)

### Trip Details Page 
-	Consits of the trip name at the top 
-	Followed by 3/4 images to give the user an overview what they will experience on the trip
-	Add to favourite hart icon appears on the left hand side of the image
-	On the right hand side of the image there is a floating “book now” button which will be fixed to the top of the page at all times, giving the user an easy access to the booking page, without the need to scroll up.
-	Features part of the page contain all the main features of the trip, to enchance user experience the icons. 
-	On the right hand side there are Google Maps which show the trip overview to the user 
-	Full Description 
-	What is Included
-	What to Bring 
-	Link to the shop for holiday essential (maybe)
-	Customer reviews also appear on the page. 
-	This page loads only 3 reviews, latest reviews first and has button to display more reviews if the user would like to read some more 
-	Two buttons at the bottom of the page which lead the user to go back to all trips page or explore latest deals


##### back to [content](#table-of-content)

### Booking Page
-	Consists of the booking form hidden from the user and only the icons are displayed. 
-	The user needs to pick their booking date
-	The number of people 
-	The user may also check the weather for the day of their booked trip
#### Trip Description 
-	A card which shows overview of the selected trip
#### Cancellation Policy 
-	In a form of the button, when the user pressed on the button a modal will display the cancellation policy to the user  with a checkbox to agree 
-	Which will be added to the ticket confirmation
#### Subtotal 
-	Once the user chooses the date and the number of people this form will be self populated with and display the total cost of the trip 
#### Call to Action Buttons 
-	One button “Cancel” which will redirect the user to the all trips page
-	The other button “Add to Basket” which will add the trip to basket 
-	Display the message to the user to tell them that their trip has been added to the busket
-	The user needs to be logged in to add their trip to the basket, if the user is not authenticated the user will be redirected to loggin/register page
##### back to [content](#table-of-content)

### Shop Page (maybe yes or not yet)

##### back to [content](#table-of-content)


### Basket  Page
-	The  user is greeted with a heading identifying the page clearly
-	The user is able to see a picture pre-view of their chosen trip 
-	Small description of their trip 
-	The user is able to modify the date and the number of people selected for the trip
-	The user can update their choice by pressing the button “Update”
-	The user is able to see the total cost of their trip on this page 
-	Two button at the bottom of the page “Continue Shopping” which will redirect the user to the trips page or “Checkout” which will take the user to the next page “Checkout”
-	The user will have access to their basket by clicking on the basket icon in the main navbar 

##### back to [content](#table-of-content)


#### Checkout Page
-	Once the user decides to checkout, they will be asked to complete a form and fill out the relevant details to complete a card transaction
-	The user will be able to save their details for next time by clicking on check box, which will store their information in their profile page. 
-	The user will be able to amend this information at any time 
-	The user will be asked for their card details 
-	Images of the credit and debit cards displayed to let the user know which payment methods they are able to use
-	A message at the bottom of the page will tell the user how much is being charged on their card
-	The user has two options at this point, press “Submit” button and the payment will be made to Stripe or “Cancel” button and the user will be redirected to the “Home” page.

##### back to [content](#table-of-content)


#### Checkout Success Page
  -  Checkout success page will be displayed once the payment has been successfully completed.
- Trip Description will be displayed and booking reference number will be randomly generated, which will act as a ticket number for the trip 
- The user will able to access this number in their profile page and present as a proof of purchase to the trip organizer
- The user will receive an email with the same details as a confirmation of their booking 
- The trip organizer will receive the same email to let them know the number of people booked for which date and booking ref number, which will be accepted as a proof of purchase on the day of the trip
- A short paragraph at the bottom of  the ticket will tell the user that they will receive a confirmation email and they are also able to view the ticket in their profile page.

##### back to [content](#table-of-content)

### About Page
-	About page will tell the user more information about the site, how it started and the mission of the site
-	This page will also tell the potential client why they might want to collaborate with the site and the benefits they will receive once they sign the contract. 
-	About page has two buttons at the bottom of the page “Home” which will redirect the user to the home page and “Contact” which will redirect the user to the contact page

### Contact Page
-	The contact page consists of a simple form, which user needs to fill out to submit  their query. 
-	The user is presentec with a select box to choose their subject, which will act as a subject send to the Admin email address. As the business grows there might be different people who would deal with general or business enquiries.
-	The user may choose to press “Clear” button to clear the form or “Submit” button to submit the form 
-	A message will tell the user their form has been submitted and somebody from the team will be in touch with them shortly.
-	On successful submission of the form the user will be redirected to the home page.



### 404 Error Page

 

##### back to [content](#table-of-content)

### 500 Error Page



##### back to [content](#table-of-content)

### Features Left to Implement 

-	Shop page which will allow the business owner to earn affiliate income 
-	Client profile page, where the vendor of the trip will be able to see all their trips 
-	Check the availability of the trips
-	Check the bookings for a specific date 
-	Maybe even print their schedule for the date of the trip, with booking reference numbers, number of people and full names of attendies.
-	Booking form, should have a textarea element where the user is able to add notes to their booking and the vendor will be able to see them
-	Weather API
-	Google Maps API
-	Privacy Policy




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