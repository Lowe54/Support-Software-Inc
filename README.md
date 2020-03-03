# Support Software Inc
![PyPI - Django Version](https://img.shields.io/badge/Django-3.0.1-green)
![Build Status](https://travis-ci.org/Lowe54/Support-Software-Inc.svg?branch=master)
## UX/UI Design

### Wireframes
All wireframe designs can be found in the [Wireframes Folder](/wireframes)

The desktop wireframes were based off a full HD monitor (1920px x 1080px)

The mobile wireframes were based off the screen size of a iPhone X (375px x 812px Portrait) / (812px x 375px Landscape)

### Database Design

#### User Model

The user model extends the default Django User model, adding on a profile picture and linking to an organisation table, which contains a uuid (Universally Unique Identifier) as the Primary Key for an Organisation, along with the Organisations name.

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

### Github Branches

#### Organisation-module

This branch was created to test splitting the 'Organisation' Table into it's own module, which means that it would be seperate and able to have its own set of URL's, instead of sharing the Authentication ones.


### Testing

#### Automated Testing

##### Continuous Integration

This project has a CI implementation with [Travis CI](https://travis-ci.com/), the only enforcement is for the import order, which is determined via the `.travis.yml` file. This is enforced via the `isort --check-only --diff --skip-glob=*/migrations/*` command.


#### Github Branches

##### 3.1-testing

This Branch was created to test a minor Django version upgrade



### Credits

[Jesse Couch](https://codepen.io/designcouch/pen/Atyop) for the burger bar animation.
[WebFikirleri](https://codepen.io/WebFikirleri/pen/MLXYKm) for the floating action button