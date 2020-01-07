# Support Software Inc
![PyPI - Django Version](https://img.shields.io/badge/Django-3.0-green)
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

