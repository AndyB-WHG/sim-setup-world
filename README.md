# 'Sports Event Planner' website

## Introduction

This website is aimed at virtual Racing Drivers, who race online via a variety of titles such as iRacing, Gran Turismo Sport and Assetto Corsa.  

Car setup is vital in improving speed, handling and competitiveness. This website acts a respository for users' setups.  Users can view setups submitted by others, or submit their own creations. 

A live website can be found [here]( https://andyb-whg.github.io/....../).

![website preview](documentation-assets/Am-I-ResponsiveDesignScreenshot.PNG)


# Table of Contents
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

The subject of racing car setups is both expansive and complex.  Creating a setup which is both fast and easy to drive can be both time-consuming and immensely frastrating.  For those new to car setups or sim-racing generally, the options can seem overwhelming, and the effects of each setting diffult to understand. 

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


## Scope

All of the features identified above are deemed to be of high or critical importance to the project.  The scope will therefore include all of the features listed.



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
Three variations are provided as examples of differing screen size layouts, namely Mobile, Tablet and Desktop. 'Extended' versions of the mobile and tablet wireframes are provided in order to show the full scrollable content post Stage 3. 

### Wire-frames
Web browser view

![Desktop Wireframe](https://github.com/AndyB-WHG/sports-event-planner/blob/master/documentation-assets/wireframe-images/desktopWireframe.PNG)

Mobile & Tablet browser view

![Mobile & Table Wireframes](https://github.com/AndyB-WHG/sports-event-planner/blob/master/documentation-assets/wireframe-images/mobileTabletExtendedWireFrames.png)



<a name="surface"></a>
## 1.4. Surface
  [Go to the top](#table-of-contents)

### Colours
Colours used are:

- #28a745 (Green) - used on buttons to compliment the grass within the Hero Image.
- #393837 (Charcoal Grey) - implemented within the Table Header to blend with the Filter and Table text and to tie in with the darker section of the Hero Image but with a softer shade to be easier on the eye.  Also provides a clear differentiation between the filter and table sections.


### Typography
- 'Exo' : used on the majority of the site to provide a mordern, positive feel.
- 'Play' : Filter Button font to provide contrast and interest against the Table section.

<a name="features"></a>
# 2. Features
  [Go to the top](#table-of-contents)

### Header Section
- Company Brand - placed prominently at top left.
- Quick Search Input Box - prompts users to search for a team or competition of interest.  Aids first time visitors providing an easy, intuitive first step.
- Quick Search button - highlighted in green for subconscious positive affirmation of use.
- Loading GIF - appears during initial page load whilst suggestions are loaded from the linked API - suggestions then populate the Quick Search Input Box to help the user with potential searches.

### Hero Image Section
- Emotive atmospheric image of a packed sports stadium used to invoke positivity, excitement and urgency.
- 'Call-Out' message both informs the user of the website's purpose whilst promoting immediate action.

### Filter Section

* Seven filter buttons provide the ability to narrow and refine searches between  :
  - Start Date
  - End Date
  - Sport
  - Team / Competitor
  - Competition
  - Country

* 'Start Filter' button - coloured green as per the Quick Search button to indicate positive use. Takes the input from the seven Filter Buttons and feeds the requirements to the 'PredictHQ' external API resource.

### Results Table Section

- Seven Columns provide pertinent information to the user based on the search criteria provided :
  - Event Title 	
  - Start Date 
  - End Date
  - Place Name	
  - Country	
  - Type	
  - Sub Type

- Results are provided 10 rows at a time.
- Pagination buttons are provided where the results yielded number greater than ten.  The user is able to move backwards and forwards as required.
- Each line is highlighted in green as per the previous buttons, both to standardise the colour scheme and, for Developments Stages 2 and 3, to indicate that the line can be clicked to highlight and zoom in on the Google Map location.
- 'Clear Filter' button : provides a simple, quick method to clear the filters ready for a subsequent search.

### Footer / Social Media Section

The bottom of the page provides standard / expected social media links to popular platforms including Youtube, Twitter, Facebook and Instagram.


<a name="technologies-used"></a>
# 3. Technologies Used
  [Go to the top](#table-of-contents)

- [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5), [CSS3](https://en.wikipedia.org/wiki/CSS) and [Boostrap v.4.1](https://getbootstrap.com/docs/4.1/getting-started/introduction/) provide structure, styling and responsiveness to various viewports. 

- [Balsamiq](https://balsamiq.com/) wireframes were used in the design and initial look of the site.

- [Javascript](https://en.wikipedia.org/wiki/JavaScript) and [jQuery](https://en.wikipedia.org/wiki/JQuery) enable the site's user-interactivity functions.

- The [PredictHQ.com](https://www.predicthq.com/?utm_campaign=Brand&utm_term=predicthq&utm_source=adwords&utm_medium=ppc&hsa_net=adwords&hsa_ver=3&hsa_grp=21054631146&hsa_tgt=kwd-922375241988&hsa_kw=predicthq&hsa_cam=339807546&hsa_ad=494263849564&hsa_src=g&hsa_acc=4773278510&hsa_mt=e&gclid=Cj0KCQjw_dWGBhDAARIsAMcYuJwqJuYQFVJoJ-D3d468HtAhRv5UgC78H6AQUcCC39L1yzf9OI8ZV-AaAt6TEALw_wcB) 'Events' and 'Places' API's provide the real-time data powering the Search and Results Table features.

- The [Chrome](https://www.google.com/intl/en_uk/chrome/) web-browser was used to view and test the site through design and implementation.

- The [Gitpod](https://www.gitpod.io/) IDE (integrated development environment) and [Github](https://github.com/Github) repository provided the platforms for developmernt and storage of the site.

- [Google Fonts](https://fonts.google.com/) provided the 'Exo' and 'Play' fonts utilised within the site.







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
# 8. Credits
  [Go to the top](#table-of-contents)

### Code

* https://www.codeinwp.com/blog/fetch-api-tutorial-for-beginners/  :  main resource used whilst writing API Fetch() methods. 
* https://css-tricks.com/using-fetch/  :  General coding advice and specific advice on handling Fetch() errors. 
* https://gomakethings.com/how-to-use-the-fetch-method-to-make-multiple-api-calls-with-vanilla-javascript/  :  further info regarding nesting Fetch methods.
* https://learn.co/lessons/javascript-fetch  :  website suggested by CI tutor on the subject of the Fetch() method.
* https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#body  :  a second website suggested by CI tutor on the subject of the Fetch() method.
* https://www.w3schools.com/ :  general advice regarding JavaScript syntax.
* https://jqueryui.com/autocomplete/  :   for basic coding in relation to the 'Autocomplete' function used to display potential selection options in the 'Quick Search' input box (Nav Bar section).


### Content
* API data :  https://www.predicthq.com/
* Hero image provided by Riciardus from Pexels  :  [Stadium Image](https://www.pexels.com/photo/green-and-white-soccer-field-at-night-time-41257/)
* Header picture of four devices for this README.md document  : [Am I Responsive](http://ami.responsivedesign.is/)
* 'Social Media' icons in the footer section   :  [Font Awesome](https://fontawesome.com/)
* README.md layout/template provided by a fellow student, iKelvvv, via Code Institute Mentor, Marcel Mulders  :  [iKelvvv README](https://github.com/iKelvvv/MS1)