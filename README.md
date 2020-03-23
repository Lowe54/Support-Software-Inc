# Support Software Inc

![PyPI - Django Version](https://img.shields.io/badge/Django-3.0.1-green)
![Build Status](https://travis-ci.org/Lowe54/Support-Software-Inc.svg?branch=master)

## Introduction

Welcome to the next generation in service desk software,

## Table of Contents

- [Support Software Inc](#support-software-inc)
  - [Introduction](#introduction)
  - [Table of Contents](#table-of-contents)
  - [UX/UI Design](#uxui-design)
    - [Wireframes](#wireframes)
  - [Database Design](#database-design)
    - [Versions](#versions)
    - [Database Models](#database-models)
      - [User](#user)
      - [Organisation](#organisation)
      - [Tickets](#tickets)
      - [Comments](#comments)
      - [Purchase](#purchase)
      - [Ticket Files](#ticket-files)
  - [Github Branches](#github-branches)
    - [Master](#master)
    - [3.1-testing](#31-testing)
    - [Organisation-module](#organisation-module)
    - [Feature/Emails](#featureemails)
    - [Feature/user-import](#featureuser-import)
  - [Testing](#testing)
    - [Code Testing](#code-testing)
      - [HTML](#html)
      - [Javascript](#javascript)
        - [Core.js](#corejs)
        - [Profile.js](#profilejs)
        - [Organisation.js](#organisationjs)
        - [Stripe.js](#stripejs)
        - [Ticket.js](#ticketjs)
      - [Python](#python)
    - [Automated Testing](#automated-testing)
      - [Continuous Integration](#continuous-integration)
    - [Credits](#credits)

## UX/UI Design

### Wireframes

The initial designs for this software can be found in the [Wireframes Folder](/wireframes), the desktop version of these were based off a full HD monitor with a resolution of 1920 x 1080px while the mobile designs were based off an iPhone X (375px x 812px Portrait) / (812px x 375px Landscape)

## Database Design

### Versions

Version 1
![User Model v1](/wireframes/database_design_v1.png)

Version 2
![User Model v2](/wireframes/db_design_v2.png)

Version 3
![User Model v3](/wireframes/db_design_v3.png)

Version 4
![User Model v4](/wireframes/db_design_v4.png)

Version 5
![User Model v5](/wireframes/db_design_v5.png)

### Database Models

#### User

The user model extends the default Django User model with a profile picture, user role, their organisation,  if they are an organisation admin and if they can view all their organisations requests.

#### Organisation

The organisation model simply contains the organisations UUID (Universally Unique Identifier), along with the organisation name.

#### Tickets

The tickets table contains all the information relevent to a support request, including who raised the request, the date/time it was raised on, status, priority, any associated users (Who would recieve emails when the request was updated), along with closure details (If the request is closed).

#### Comments

The Comments table links users to various comments, as well as the type of comment (Public or Internal), the date and time the comment was posted, and the ticket the comment was posted on.

#### Purchase

#### Ticket Files

While this remains a feature to be implemented (See Upcoming features), it would link an uploaded file to a request, as well as the type and size of the uploaded file

## Github Branches

### Master

This branch contains the live version of the site.

### 3.1-testing

This Branch was created to test a minor Django version upgrade

### Organisation-module

This branch was created to test splitting the 'Organisation' Table into it's own module, which means that it would be seperate and able to have its own set of URL's, instead of sharing the Authentication ones.

### Feature/Emails

This branch contains future email functionality.

### Feature/user-import

This branch contains functionality that would allow an admin to import a csv file of users into the system.

## Testing

### Code Testing

#### HTML

#### Javascript

All Javascript was tested via [JSHint](https://jshint.com/docs/), the results against each of the js files within the software can be found below

##### Core.js

![Core JS Result](/documentation_images/corejs_result.png)

Undefined Variables Listed

- Swal
  - This is a Sweetalert 2 alert initialisation

- introJS
  - This is used by IntroJS, which is the guided tooltips that are activated via the 'help' button
  
- stripe_init
  - This is one of the functions defined in stripe.js

##### Profile.js

![Core JS Result](/documentation_images/corejs_result.png)

##### Organisation.js

![Organisation JS Result](/documentation_images/organisationjs_result.png)

##### Stripe.js

![Stripe JS Result](/documentation_images/stripejs_result.png)

##### Ticket.js

![Ticket JS Result](/documentation_images/ticketjs_result.png)

#### Python

[Pylint](https://www.pylint.org/) was used in order to check the conformity of the code to PEP8 standard, as part of this the code report for the site is available [here](pylint.html).

This report is generated via the following commands once the software has been installed

`pylint --output-format=jsonextended authentication core emails organisations payments ticket > pylint.json`

`pylint-json2html -f jsonextended -o pylint.html pylint.json`

### Automated Testing

#### Continuous Integration

This project has a CI implementation with [Travis CI](https://travis-ci.com/), the only enforcement is for the import order, which is determined via the `.travis.yml` file. This is enforced via the `isort --check-only --diff --skip-glob=*/migrations/*` command.

### Credits

[Jesse Couch](https://codepen.io/designcouch/pen/Atyop) for the burger bar animation.
[WebFikirleri](https://codepen.io/WebFikirleri/pen/MLXYKm) for the floating action button
