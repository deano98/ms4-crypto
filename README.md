# Milestone Project 4 - Milestone Crypto Website

This website will be a django based. social application used to track the prices of the top Cryptocurrencies and then have active discussions with fellow investors, helping to make more informed investment decisions.

The app will have up to date prices for the top 10 Cryptocurrencies, as well as recent news and a reddit style chat system to share information with like minded individuals rather than paid influencers. Time is money in the investment game, having all of the information you need, available in one place will help you make smarter investments more quickly, resulting in more fruitful gains.

# Problem Statement

In order to make sensible crypto investments, people need current prices as well as up to date information and advice.
Currently, it is difficult to find all of this information, having to check several different websites or resources. Milestone Crypto will provide an easy solution to get this information and socially interact with fellow investors.

# UX

## User Stories

* As an unregistered User, I can sign up and make a personal account on the website.
* As an unregistered User, I can see up to date Crypto prices so that I can make better decisions on when to buy or sell, without having to register.
* As an unregistered User, I can see other relevant information such as current market cap and price changes, to also help me make better decisions on when to buy or sell.
* As a registered User, I can create posts so that I can share any relevant information I find with fellow investors.
* As a registered User, I can edit and delete my own posts.
* As a registered User, I can upvote and downvote posts and comments so that the most popular posts are easier to find. 

# Entity Relationship Diagram

[ERD](static/wireframes/erd-diagram.PNG)

* The comment model was removed during development as advised by my Mentor.

# Wireframes

### Homepage

* [Desktop](static/wireframes/homepage-desktop.png)
* [Mobile](static/wireframes/homepage-mobile.png)

### Posts Page

* [Desktop](static/wireframes/posts-desktop.png)
* [Mobile](static/wireframes/posts-mobile.png)

# Design

## Typography

* The font the site will use is Nunito, to give the site a clean and modern look.

## Colour Scheme

[Spot-Palette](static/screenshots/spot-palett.PNG)

# Features

* All pages will include a responsive navigation bar at the top, with links to register, log in, log out or return to the homepage. This will collapse down into an offcanvas nav bar when on smaller devices.

## Homepage

* The homepage will have a feed of the current top 10 cryptocurrencies, ranked by marketcap. Each widget will display the currencies logo to make it easily identifiable, all of the current price information and a clickable link to view any posts and comments made about that specific coin.

## Post Pages

* Each cryptocurrency will have it's own specific discussion page, which you can navigate to by clicking on which coin you want to discuss on the home page.
* The discussion page will feature the price information on the top left of the page.
* There will be a form to create posts on the top right of the page.
* Below that will be a feed of every post made about that specific currency.
* Each post will display a title, the posts content, who posted it, the date it was posted and buttons to upvote or downvote the post.
* Users will also be able to edit or delete their own posts.

## Future Features

* Add a news feed with the latest headlines regarding cryptocurrency.

# Technologies Used

### Integrated Development Environment

* Github

### Languages Used

* HTML
* CSS
* Python
* JavaScript

### Database

* PostreSQL

### Storage

* Cloudinary

### Frameworks

* Django
* Bootstrap
* jQuery

### Packages and other Tools

* Lucid Chart - to create ERD diagram
* Balsamiq - Wireframes
* Font Awesome
* Google Fonts
* CoinGecko API - for currency data
* gunicorn
* psycopg2
* django allauth
* django crispy forms
* django ajax

# Testing

### Code Validation

[W3C Markup Validation](https://validator.w3.org/) 

[W3C CSS Validation](https://jigsaw.w3.org/css-validator/)

* For the Python code I used the problems tab in GitPod

### Testing User Stories

* I have applied automated testing to one of my views, but I have opted to use manual testing for the rest of the application.

1. As an unregistered User, I can sign up and make a personal account on the website.
  * If a user isn't registered, they will be able to make an account using the Register link on the navigation bar.
  * Registration is quick and easy, manually testing has uncovered no issues with the process.

2. As an unregistered User, I can see up to date Crypto prices so that I can make better decisions on when to buy or sell, without having to register.
  * Annonymous users are able to see all prices without having to register.
  * No issues were found testing this as an annonymous user.

3. As an unregistered User, I can see other relevant information such as current market cap and price changes, to also help me make better decisions on when to buy or sell.
  * All further information and Posts are viewable as an unregistered user.
  * No issues found.

4. As a registered User, I can create posts so that I can share any relevant information I find with fellow investors.
  * Registered users are able to create posts which are viewable by all users.
  * No issues found

5. As a registered User, I can edit and delete my own posts.
  * Users can edit or delete their own posts, buttons are disabled for Users who did not create the post.
  * No issues found

6. As a registered User, I can upvote and downvote posts and comments so that the most popular posts are easier to find. 
  * Members are able to upvote and downvote posts, the count for each is displayed for all users, but the buttons are disabled for unregistered users.
  * Testing uncovered no issues with this process.

### Testing for Bugs

* I have manually tested the functionality of the site extensively.
* Testing yielded one bug as described below.

### Bug Fixes

* An issue was uncovered with form validation, as the title needs to be unique for all posts, when a duplicate title was used in a post, the page just reloaded with an empty form. The if statement was modified to allow the validation error to display on the form, so the user now has vision of the error.

# Deployment

1. GitPod
  * Migrate changes to database.
  * Change Debug in settings.py to False

2. Heroku
  * Navigate to the apps page on Heroku
  * Click new > Create app
  * Enter a unique name for your app and choose your region
  * Click create app
  * Navigate to the Settings tab and click Reveal Config Vars
  * Add CLOUDINARY_URL and input the Cloudinary URL
  * Add DATABASE_URL and input the postgres URL
  * Add SECRET_KEY and input your secret key
  * Navigate to the Deploy tab
  * Click on Connect to GitHub in the deployment method section
  * Enter your projects repository name in the Connect to GitHub section, then click search.
  * When your repository is displayed, click connect
  * If you wish for your deployed app to be rebuilt each time you push a new change, click Enable Automatic Deploys
  * If you wish to deply manually, click Deploy Branch
  * Once your app has finished building, it is then deployed on Heroku.

# External Resources

* [w3schools](https://www.w3schools.com/) For help with code issues
* [Stack Overflow](https://stackoverflow.com/) For help with code issues
* [Youtube](https://youtube.com/) Code Tutorials
* Django 3 by Example ebook

# Credits

 * Thanks to my mentor Rohit Sharma, for the support with my project.
 * Thanks to everyone on Slack for just being a great source of help and information.

