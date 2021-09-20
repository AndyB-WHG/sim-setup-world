# 'Sim Setup World' website

## Introduction

This website is aimed at virtual Racing Drivers, who race online via a variety of titles such as iRacing, Gran Turismo Sport and Assetto Corsa.  

Car setup is vital in improving speed, handling and competitiveness. This website acts a respository for users' setups.  Users can view setups submitted by others, or submit their own creations. 

A live website can be found [here]( https://andyb-whg.github.io/....../).

![website preview](documentation-assets/Am-I-ResponsiveDesignScreenshot.PNG)


## Table of Contents

- [1. UX](#ux)
  * [1.1. Strategy](#strategy)
    - [Project Goals](#project-goals)
    - [User Stories:](#user-stories)
    - [Strategy Table](#strategy-table)
  * [1.2. Structure](#structure)
  * [1.3. Skeleton](#skeleton)
  * [1.4. Surface](#surface)
- [2. Features](#features)
- [3. Technologies Used](#technologies-used)
- [4. Testing](#testing)
- [5. Development Cycle](#development-cycle)
- [6. Deployment](#deployment)
- [7. Known Bugs](#known-bugs)
- [8. Credits](#credits)

<a name="ux"></a>
# 1. UX
  [Go to the top](#table-of-contents)

<a name="strategy"></a>
## 1.1. Strategy
  [Go to the top](#table-of-contents)

### Project Goal

The subject of racing car setups is both expansive and complex.  Creating a setup which is both fast and easy to drive can be both time-consuming and frastrating.  For those new to car setups or sim-racing generally, the options can seem overwhelming, and the effects of each setting difficult to understand. 

The main aim of the site is to give users a quick and efficient way to find pre-made, fast and easy-to-handle car setups for the game and car of their choice.  Users can also submit their own setups for use by other racers.

And for those wanting to learn more, a `'tutorials'` section is included, with links to various YouTube videos submitted by fellow sim-racers.

### User Stories:

 * As a first-time user I want the site to be intuitive and easy to navigate and understand.  

 * As a user I want a simple, quick method of finding a good setup for my car. 

 * As a user I want the site to be elegant and easy on the eye.

 * As a user I want the site to be responsive to different screen sizes so that I can still use the site whether I’m using my mobile phone, tablet or PC.

 * As an experienced sim-racer I want an easy way to submit setups I've created.

 * As an experienced sim-racer I want a way to edit setups I've created previosuly.  
 
 * As a returning user I want my setups to be protected from interference by other users.

 * As a user new to sim-racing I'm interested in learning how to set up my own cars. A`'setup-guide'`section would therefore be very valuable.  

### Strategy Table
Features| Importance| Viability/Feasibility
------------ | -------------------------|---------
Provide a list of pre-made setups for the user to view | 5 | 5
Quick Search function to enable users to filter setups by Sim, Car and Track  | 5| 5
Responsive design | 5 | 5
Simple 'submit setup' process for experienced racers | 5 | 5
Tutorial Section for users looking to learn how to setup a car | 4 | 3
Rating feature to enable users to rate each other's setups | 3 | 3


## Scope

Most of the features identified above are deemed to be of high or critical importance to the project, with the exception of the rating system which is to be added in a later update.  The scope will therefore include all of the first five features listed.


<a name="structure"></a>
## 1.2. Structure
  [Go to the top](#table-of-contents)

 - Site to be responsive on all Screen Sizes with information selectively added / removed dependent upon the screen size in use.
 - `Nav Bar` section placed prominently at the top of the page to inform user options.
 - Four Home Page 'cards' provide user with access to main site features (Find, Submit, Edit setups, Tutorials)
 - `'Filter' section` placed prominently at top of `Find`, `Submit` and `Edit` pages to speed user searches.
 - Complete list of all setups initially provided beneath the filter section of the 'Find Setups' page.
 - Complete list of all the user's previously submitted setups provided beneath the filter section of the `'Edit/Delete/My Setups'` page
 - 'Collapsible' `tutorials` section gives users intuitive access to setup videos provided by experienced sim racers via YouTube.
 - Footer section at bottom of page displaying social media links to various websites including Twitter, Youtube, Instagram and Facebook.
- `Admin` option appears in the Nav Bar when a user with Admin Rights logs in to the site. Admin rights give users the ability to edit and delete other user's setups and login details.

<a name="skeleton"></a>
## 1.3. Skeleton
  [Go to the top](#table-of-contents)

[Balsamiq](https://balsamiq.com/) was used to create the following wireframes.  
Three variations are provided as examples of differing screen size layouts, namely Mobile, Tablet and Desktop. 'Extended' versions of some of the mobile and tablet wireframes are provided in order to show the full scrollable content. 

## Wire-frames

[Link to all wireframes created for this project]()

**'Home' page (Mobile version)**

![Mobile Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/10.%20Home%20Page%20-%20wireframe%20-%20Mobile%20version.PNG)

**'Home' page (Tablet version)**

![Tablet Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/10.%20Home%20Page%20-%20wireframe%20-%20Tablet%20version.PNG)

**'Home' page (Desktop version)**

![Desktop Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/10.%20Home%20Page%20-%20wireframe%20-%20Desktop%20version.PNG)


**'Find A Setup' page 1 - Initial search (Tablet Version)**

![Tablet Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/30.%20'Find%20a%20Setup'%20Part%201%20-%20Initial%20Search%20Choices%20-%20wireframe%20-%20Tablet%20version.PNG)

**'Find A Setup' page 2 - Results list (Tablet Version)**

![Tablet Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/30.%20'Find%20a%20Setup'%20Part%202%20-%20The%20Results%20Table%20-%20wireframe%20-%20Tablet%20version.PNG)

**'Find A Setup' page 3 - Viewing the setup parameters (Tablet Version)**

![Tablet Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/30.%20'Find%20a%20Setup'%20Part%203%20-%20Viewing%20the%20Setup%20-%20wireframe%20-%20Tablet%20version.PNG)

**'Tutorials' page (Mobile Version)**

![Mobile Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/20.%20Tutorials%20page%20-%20wireframe%20-%20Mobile%20version.PNG)

**'Tutorials' page (Tablet Version)**

![Tablet Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/20.%20Tutorials%20page%20-%20wireframe%20-%20Tablet%20version.PNG)

**'Tutorials' page (Desktop Version)**

![Tablet Wireframe](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Wireframes/20.%20Tutorials%20page%20-%20wireframe%20-%20Desktop%20version.PNG)

<a name="surface"></a>
## 1.4. Surface
  [Go to the top](#table-of-contents)

### Colours
Colours used are:

- #f57c00 (Orange) - main colour scheme of the site - used in headers and on various icons within the site.  Colour is part of the standard ['Materialize.com'](https://materializecss.com/) colour set.
- #e65100 (Dark Orange) - used as a contrast within various pages to highlight 'action' buttons.  Also used within the footers of each page as using the same colour as the Header section produced an odd result in which the footer looked distinctly lighter than the header.


### Typography
- 'Exo' : used throughout the site to provide a mordern, positive feel.

<a name="features"></a>
# 2. Features
  [Go to the top](#table-of-contents)

### 'Header' Section
- Company Brand - placed prominently at top middle (Mobile and Tablet) and top left (Desktop).
- Brand logo can be clicked from any page to return the user to the 'Home' page.
- 'Burger' icon placed top right on Mobile and Tablet screens to simplify the look and feel of the menu section.  Links flow in from right hand side once clicked.
- Standard 'Nav Bar' links are placed across the top right of the page on larger screen sizes for immediate access.
- Links within the Nav Bar increase or decrease dependent upon whether the user is logged in or out, and, if logged in, whether the user is an 'Admin' super-user.

### 'Footer / Social Media' Section

The bottom of the page provides standard / expected social media links to popular platforms including Youtube, Twitter, Facebook and Instagram.

### 'Home' Page

* Split into five sections, each with a link to the main user sections of the site:

  - 'Callout' section : welcomes the user to the site and explains the aims of the site and benefits for the user.

  - Find a Setup  :  allows users to search for setups generally or for specific car/track combinations (login not required).

  - Submit a Setup : allows users to submit their own setups for use by other users or as a database for personal use (login required).

  - Edit / Delete a Setup : allows users to change or delete their own setups (log in required).

  - Setup Tutorials : allows users to navigate to specific YouTube videos to study a wide variety of car setup topics (login not required).

### 'Find a Setup' page

* Split into three sections:
  
  - 'Instruction' section : guides the user as to how to search for a relevant setup.

  - 'Filter' section : allows users to target specific setups based on : 
  
    - 'Sim'  -  user must choose one of four 'Sims' provided within a drop-down list (sims stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    - 'Car'  - user is provided with an appropriate list of cars for the sim chosen within a drop down list (cars stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    - 'Track'  - user is provided with an appropriate list of tracks for the sim chosen within a drop down list (tracks stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    

  - 'Results' section : initially lists all setups in the database on page load.  Results are filtered accordingly should the user choose to enter parameters into the 'filter' section.

    - Results are displayed with varying numbers of columns dependent upon screen size. 

    - A 'View' button is given for each setup listed. Clicking the button takes the user to the setup display screen listing all the parameters and values the user will need to setup their chosen car.

### 'Submit a Setup' page

* Split into two sections:
  
  - 'Instruction' section : guides the user as to how to submit a setup.

  - 'Filter' section : users are required to enter three necessary parameters in order to create the relevant 'Parameter Entry' page : 
  
    - 'Sim'  -  user must choose one of four 'Sims' provided within a drop-down list (sims stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    - 'Car'  - user is provided with an appropriate list of cars for the sim chosen within a drop down list (cars stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    - 'Track'  - user is provided with an appropriate list of tracks for the sim chosen within a drop down list (tracks stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).

  - Once the parameters are entered the user is presented with buttons to either Enter Settings, Restart or Cancel the Submission process.

### 'My Setups' page

* Split into three sections:
  
  - 'Instruction' section : guides the user as to how to search for a relevant setup.

  - 'Filter' section : allows users to target specific setups based on : 
  
    - 'Sim'  -  user must choose one of four 'Sims' provided within a drop-down list (sims stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    - 'Car'  - user is provided with an appropriate list of cars for the sim chosen within a drop down list (cars stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    - 'Track'  - user is provided with an appropriate list of tracks for the sim chosen within a drop down list (tracks stored within a database - in this case [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE)).
    

  - 'Results' section : initially lists all of the `user's setups` in the database on page load.  Results are filtered accordingly should the user choose to enter parameters into the 'filter' section.

    - Results are displayed with varying numbers of columns dependent upon screen size. 

    - 'View', 'Edit' and 'Delete' button are provided for each setup listed. 

### 'Tutorials' page

- Split into two sections:

  - Explanatory section at top guiding the user to click on a drop-down option.

  - 'Collapsble' drop down section, split into two subsections:

    - Full Setup Guides (By Coach) : leads to sub-sections for coaches and, in turn, to specific topics.  

    - Guides by Component : leads to sub-sections for each car component and, in turn, to specific videos for each of those topics.
  
  Clicking on the video link opens a new tab and loads the related YouTube video for immediate viewing.

### 'View Setup' Parameter page:

After entering the necessary Sim, Car and Track requirements on the initial 'Find a Setup' page, the user is presented with a 'Setup Parameters' page. Here the user can view the parameters and their values for the chosen setup.  The fields displayed are dependent upon the 'Sim' in question, each sim having a different parameter set, contained within different 'heading sections'.  The Heading and Parameter reuirements being held within the MongoDB database.

### 'Submit Setup' Parameter Entry page:

After entering the necessary Sim, Car and Track requirements on the initial 'Submit a Setup' page, the user is presented with a 'Parameter Entry' page. Here the user enters the necessary parameter values in oder for the setup to be submitted.  The fields displayed are dependent upon the 'Sim' chosen by the user, each sim having a different parameter set, contained within different 'heading sections'.  The Heading and Parameter requirements being held within the MongoDB database.

### 'Edit Setup' Parameter page:

After entering the necessary Sim, Car and Track requirements on the initial 'My Setups' page, the user is presented with a 'Parameter Values' page. Here the user is presented with the current parameter values of the setup.  The user has the option to change any or all of the values displayed before either Saving, Restarting or Exiting (without saving) the setup. 

### 'Admin Tasks' page:

If the user has 'Admin Rights' he/she will have the option to click the 'Admin Tasks' click within the Navbar.

The link takes the user to the 'Admin Tasks' page. The page is split into three section:

  - Information section at top of page (beneath Navbar) confirming the user is an Admin Rights holder, plus a confirmation title of the current displayed page.

  - 'Manage Setups' section : with an associated 'Start' button.

  - 'Manage Users' page : with associated 'Edit' and 'Delete' buttons.

  ### 'Manage Setups' page:

  Users with Admin Rights have the option here to 'Edit', 'View' or 'Delete' setups for all users in the same way that Users may edit, view or delete their own setups.  (See 'My Setups' page info).

  ### 'Edit Users' page:

  Users with Admin Rights have the option to 'Edit' user account information. Namely:

    - Change user's username
    - Change user's password
    - Change user's Admin Rights access

  The users 'username' must first be enetered in the relevant field, together with the Admin's password to verify security clearance.

  A second page is displayed once verfied, allowing the Admin to change the necessary details and save the new details to the database.

  ### 'Delete Users' page:

  Users with Admin Rights have the option to 'Delete' user accounts as required. 

  The users 'username' must first be enetered in the relevant field, together with the Admin's password to verify security clearance.

  Clicking the 'Delete' button will delete the user from the database should the username exist and the Admin password be correct.


<a name="technologies-used"></a>
# 3. Technologies Used
  [Go to the top](#table-of-contents)

- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5), [CSS3](https://en.wikipedia.org/wiki/CSS) and [Materialize.com](https://materializecss.com/) provide structure, styling and responsiveness to various viewports. 

- [Balsamiq](https://balsamiq.com/) wireframes were used in the design and initial look of the site.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript) and [jQuery](https://en.wikipedia.org/wiki/JQuery) enable the site's user-interactivity functions.

- The [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/lp/try2?utm_content=controlhterms&utm_source=google&utm_campaign=gs_emea_united_kingdom_search_core_brand_atlas_desktop&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624581&gclid=CjwKCAjw4qCKBhAVEiwAkTYsPPyEA76002qoMMPs1qMTTsGG4VWaeYOYpSQsFvWjNRipRQgTBoTBDRoClVMQAvD_BwE) website is used to store the following information:
  - User setups 
  - Sim data 
  - Track data
  - Parameter names 
  - Parameter section headings
  - Tutorial 'Coach' names
  - Tutorial 'Component' data
  - Tutorial 'Youtube links' data

- The [Chrome](https://www.google.com/intl/en_uk/chrome/) web-browser was used to view and test the site through design and implementation.

- The [Gitpod](https://www.gitpod.io/) IDE (integrated development environment) and [Github](https://github.com/Github) repository provided the platforms for developmernt and storage of the site.

- [Google Fonts](https://fonts.google.com/) provided the 'Exo' font utilised within the site.

- [Font Awesome](https://fontawesome.com/) provided the various icons used within the site.

<a name="testing"></a>

# 4. Testing
  [Go to the top](#table-of-contents)

## Automated testing

Screen responsiveness testing was carried out using Google Chrome's Developer Tools to ensure correct page loading on multiple devices including various mobile phone and tablet sizes.

### W3C Validator Tools

[W3C HTML Validator](https://validator.w3.org/) tool used to validate HTML code.

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/) tool used to validate CSS style code.

[JS Hint](https://jshint.com/) used to verify Javascript coding (is unable to verfiy jQuery sections however).

## Manual Testing

* Site loads as expected on both Motorola and Sony mobile phone devices utilising the Android operating system, running the Chrome browser. 

* Site loads as expected on a PC utilising the Windows operating system.  Tested using Chrome, Firefox and Edge.  All load correctly and function identically.  On the Edge browser, however, the final column renders without any outline styling on those lines where the content is empty.  Does not affect functionality in any but doesn't look quite as nice as the Chrome/Firefox rendering.

* Site loads as ecpected on an 2016 iPad Mini utilitsing the Safari browser. The table results do not highlight green when tapped as per newer devices however. This may be due to the age of the operating system so needs investigation.

* Responsiveness :
  - The site is responsive to all break points and works as expected.
  
* Quick Search Input Box : 
  - 'Loading' message is replaced with prompt to type a team or competition as expected.  
  - Box loads with 250 event suggestions as expected. User can type as required, and either select from the filtered/remaining options or ignore as desired.

* Quick Search button :
  - Button works as expected. Results are retrieved from the API and displayed in a table between the filter and footer sections of the page.

* Filter buttons :
  - 'Start Date' button - tested and works as expected.
  - 'End Date' button - tested and works as expected.
  - 'Filter by Sport' button - when tested, this button works when used in conjunction with other search criteria but does not work by itself.  Time constraints have left the bug unresolved for the time being.  The button does load preset sport options as designed, from which the user can select/ignore/type their own input.
  - 'Team/Competitor' button - tested and and is not working at present. Time constraints have left the bug unresolved for the time being. Bug is suspected to be related to the 'search' string submitted to the API and is likely to be the same bug affecting the 'Filter by Competition' and 'Filter by City' buttons.
  - 'Filter by Competition' button - tested and is not working at present. Time constraints have left the bug unresolved for the time being.
  - 'Filter by Country' - tested and works as expected.  Preset country options load as designed, from which the user can select/ignore/type their own input.
  - 'Filter by City' - tested and is not working at present. Bug is suspected to be related to the 'search' string submitted to the API and is likely to be the same bug affecting the 'Team/Competition' and 'Filter by Competition' buttons.
  - 'Start Filter' - functions as expected. When clicked, the working search parameters are retrieved from the API and dsplayed in a table below the filter buttons.

- Table rows
  - Individual events highlight in green when selected on a touch screen or hovered over using a mouse.  Tested on a 2016 Apple iPad mini but this functionality was not present - possibly due to the age of the platform.

* Footer Links :
  
    - Facebook - When selecting the Facebook icon, a new tab opens and redirects to the Facebook website. It worked as expected.
    - Twitter -  When selecting the Twitter icon, a new tab opens and redirects to the Twitter website. It worked as expected.
    - YouTube - When selecting the YouTube icon, a new tab opens and redirects to the YouTube website. It worked as expected.
    - Instagram -  When selecting the Instagram icon, a new tab opens and redirects to the Instagram website. It worked as expected.

<a name="development-cycle"></a>
# 5. Development Cycle
  [Go to the top](#table-of-contents)

- HTML  : Basic HTML framework was implemented first, following the layout created using the Wireframes. 

- CSS  : The Wireframes were used as a guide for the styling. Changes were made as development continued as it became apparent that some of the colours selected were too 'loud' and varied and therefore needed toning down a little.  

- Javascript : The Javascript segment has been by far the most challenging part of the development.  

  - API connectivty : it took some time to choose an appropriate API from which to export the data required.  Connecting to the API and understanding it's Endpoints was also a serious challange.  Roughly 10 days were spend experimenting with this process before an understading how to make things work became apparent.  The next challenge was to use Javascript to connect to the API.  I contacted the college (Code Institute) who advised to use a more modern method (Fetch) to connect with the data.  Again, it took several days to get this working, having first had to research the method using the educational web links provided by the college.  Perseverence won out and eventually got it working but at the cost of considerable time.

  - Quick Search' input box pre-load:  Retrieving multiple data results in order to pre-populate the 'Quick Search' box was, again, a considerable challange.  I needed the Javascript to both render a Table of Results as soon as the page loaded whilst simultaneously calling on the API on multiple occasions to load a large selection of potential events into the Quick Search box for users to choose from if required.  Getting the code to run without errors presented a number of problems which took many days and hours to iron out.  Taking the input from the box to produce a result was reletively straightforward thankfully.

  - Filter Buttons: The filter button inputs are used to generate a search string for submission to the API.  The time required to make previous features function properly left little time for resolving bugs and as a result a number of the buttons do not yet provide the required filtered results.  A Results Table is still generated, but is not norrowed down as much as is required.  

<a name="deployment"></a>
# 6. Deployment
  [Go to the top](#table-of-contents)

GitHub pages was used to deploy the project. The following process was followed:

1. Create a repository on GitHub.
2. Create a workspace in Gitpod.
3. Add/create files in Gitpod and push to Github following successive additions.
4. Go to Github respository, click on Github Pages and create a live website

<a name="known-bugs"></a>
# 7. Known Bugs
  [Go to the top](#table-of-contents)

  - 'Team/Competitor', 'Filter by Competition' and 'Filter by City' buttons do not work at the present time.  

  - 'Results Table' does not always load first time. Page refresh resolves this issue and does not happen again after that.

  - Searching for a partial word/name in the Quick Search box does not yield any results. This is due to API constraints and requirements. A message advising as such to be added in a later update.

  - Table rows do not highlight in green on older Apple products.

<a name="credits"></a>

# 8. End Product

The following images are a selection of live screen shots taken directly from the site.  A larger collection of screen shots can be seen [here](https://github.com/AndyB-WHG/sim-setup-world/tree/main/documentation-assets/Live%20Screenshots).

`'Home' page (Tablet Version)`

![Home Page](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/1.%20Home%20Page%20-%20Tablet%20version.PNG)

`'Find a Setup' page (Mobile Version)`

![Find a Setup Page](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/2.%20Find%20Setups%20Page%20-%20Mobile%20version.PNG)

`'Find a Setup' page - 'Results' section (Tablet Version)`

![Find a Setup - Results Section](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/2.%20Find%20Setups%20Page%20-%20bottom%20section%20-%20Tablet%20version.PNG)

`'View Setup' page - showing Headings and Parameter values (Desktop Version)`

![View a Setup](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/6.%20View%20Setup%20Page%20-%20Desktop%20version.PNG)

`'Tutorials' page (Mobile Version)`

![Tutorials page](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/3.%20Tutorials%20Page%20-%20Mobile%20version.PNG)

`'Tutorials' page (Tablet Version)`

![Tutorials page](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/3.%20Tutorials%20Page%20-%20Tablet%20version.PNG)

`'Login' page (Desktop Version)`

![Tutorials page](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/7.%20Login%20Page%20-%20Desktop.PNG)

`'Register' page (Mobile Version)`

![Register page](https://github.com/AndyB-WHG/sim-setup-world/blob/main/documentation-assets/Live%20Screenshots/7.%20Register%20Page%20-%20Mobile.PNG)




# 9. Credits
  [Go to the top](#table-of-contents)

### Code
* "https://thispointer.com/python-how-to-convert-datetime-object-to-string-using-datetime-strftime/"



* https://www.codeinwp.com/blog/fetch-api-tutorial-for-beginners/  :  main resource used whilst writing API Fetch() methods. 
* https://css-tricks.com/using-fetch/  :  General coding advice and specific advice on handling Fetch() errors. 
* https://gomakethings.com/how-to-use-the-fetch-method-to-make-multiple-api-calls-with-vanilla-javascript/  :  further info regarding nesting Fetch methods.
* https://learn.co/lessons/javascript-fetch  :  website suggested by CI tutor on the subject of the Fetch() method.
* https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#body  :  a second website suggested by CI tutor on the subject of the Fetch() method.
* https://www.w3schools.com/ :  general advice regarding JavaScript syntax.
* https://jqueryui.com/autocomplete/  :   for basic coding in relation to the 'Autocomplete' function used to display potential selection options in the 'Quick Search' input box (Nav Bar section).


### Content
* Hero image provided by Riciardus from Pexels  :  [Stadium Image](https://www.pexels.com/photo/green-and-white-soccer-field-at-night-time-41257/)
* Header picture of four devices for this README.md document  : [Am I Responsive](http://ami.responsivedesign.is/)
* 'Social Media' icons in the footer section   :  [Font Awesome](https://fontawesome.com/)
* README.md layout/template provided by a fellow student, iKelvvv, via Code Institute Mentor, Marcel Mulders  :  [iKelvvv README](https://github.com/iKelvvv/MS1)