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
  - [User stories](#user-stories)
  - [Database Design](#database-design)
    - [Versions](#versions)
    - [Database Models](#database-models)
      - [User](#user)
      - [Organisation](#organisation)
      - [Tickets](#tickets)
      - [Comments](#comments)
      - [Purchase](#purchase)
      - [Ticket Files](#ticket-files)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Technology, Frameworks and Tools Used](#technology-frameworks-and-tools-used)
    - [Languages](#languages)
    - [Frameworks and Libaries](#frameworks-and-libaries)
    - [Tools](#tools)
  - [Github Branches](#github-branches)
    - [Master](#master)
    - [~~3.1-testing~~](#s31-testings)
    - [~~Organisation-module~~](#sorganisation-modules)
    - [Feature/Emails](#featureemails)
    - [Feature/user-import](#featureuser-import)
  - [Deployment](#deployment)
    - [IMPORTANT NOTICE](#important-notice)
    - [Github Repository](#github-repository)
      - [Github Cloning](#github-cloning)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Stripe Deployment](#stripe-deployment)
    - [Setting up Amazon Web Services (AWS)](#setting-up-amazon-web-services-aws)
  - [Testing](#testing)
  - [Credits](#credits)

## UX/UI Design

### Wireframes

The initial designs for this software can be found in the [Wireframes Folder](/wireframes), the desktop version of these were based off a full HD monitor with a resolution of 1920 x 1080px while the mobile designs were based off an iPhone X (375px x 812px Portrait) / (812px x 375px Landscape)

## User stories

| User story # | What am I looking for?                                                                                                             |
|--------------|------------------------------------------------------------------------------------------------------------------------------------|
| 1            | As a end user I want to be able to see all updates to a request                                                              |
| 2            | As an employee user I want to be able to respond to requests without constantly being redirected to a seperate page                |
| 3            | As an employee user I want to bee able to search for a particular request, without having to go through each and every one          |
| 4            | As a end user I want to see all of my open requests, without having to select multiple filters                               |
| 5            | As a end user I want to be able to fix errors in my name or email, without having to contact the support company             |
| 6            | As a end user I want to be able to see all requests that need my reply, without having to filter all my requests             |
| 7            | As an employee user I want to be able to associate multiple users to an organisation, without having to select each user each time |

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

## Features

### Existing Features

- Full login system
  - Users can register and login, as well as manage their account.
- Instant Commenting
  - User's aren't redirected to a seperate page to comment, it is all contained within the ticket page
- Organisation List
  - Admin's can manage organisations, associate and disassociate users all from one screen
- Result filtering
  - Users can filter their results by keyword, status, and priority

### Features Left to Implement

The following are lists of features that remain to be implemented, along with a brief description of what they entail.

- Emails
  - Email functionality including, but not limited to:
    - Sending registration emails
    - Ticket update emails
    - Broadcast emails sent by site admin(s)

- User Management
  - While this is currently possible from the admin site for individual users, this includes the following:
    - The ability for organisation admins to manage their organisation users
    - Import and Export of Users (Import functionality limited to administrators only)

## Technology, Frameworks and Tools Used

### Languages

- [HTML](https://www.w3.org/standards/webdesign/htmlcss)
- [CSS](https://www.w3.org/standards/webdesign/htmlcss#whatcss)
- [Python](https://www.python.org/)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

### Frameworks and Libaries

- [JQuery](https://jquery.com)
  - The project uses **JQuery** to simplify DOM manipulation.
- [Django](https://www.djangoproject.com/)
  - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [FontAwesome](https://fontawesome.com/)
  - The project uses the free version of **FontAwesome** in order to add extra icons to the site
- [Popper JS](https://popper.js.org/)
  - Popper JS is used to position tooltips
- [Bootstrap](https://getbootstrap.com/)
  - Bootstrap is used for general grid layout + layout utilities
- [SASS](http://sass-lang.com/)
  - **SASS** was used to add extra functionality to CSS, it allows for nested statements to be used, which in turn made the files easier to read.

### Tools

- [DB Diagram](https://dbdiagram.io/home)
  - DB Diagram is a free tool that was used to design the database

## Github Branches

### Master

This branch contains the live version of the site.

### ~~3.1-testing~~

This Branch was created to test a minor Django version upgrade, it has been merged into the master branch

### ~~Organisation-module~~

This branch was created to test splitting the 'Organisation' Table into it's own module, which means that it would be seperate and able to have its own set of URL's, instead of sharing the Authentication ones. This branch has been merged into the master branch

### Feature/Emails

This branch contains future email functionality.

### Feature/user-import

This branch contains functionality that would allow an admin to import a csv file of users into the system.

## Deployment

### IMPORTANT NOTICE

These deployment steps are intented for a windows operating system, if your OS is different, please lookup the instructions for your OS

### Github Repository

- In a terminal, the git repository was initiated via the `git init` command
  e repository was linked to a .git file on github via
  - `git remote add origin https://github.com/Lowe54/supportsoftwareinc.git`
  - `git push -u origin master`

- After each change, the following commands were used to push the changes to the git repository
  - `git add *` - This adds all changed files to staging
  - `git commit -m "MESSAGE HERE"` - Commits the work with a brief message as to what has changed
  - `git push` - This pushes the work to the git repository, after entering your github username and password

#### Github Cloning

- In order to clone the github repository, type the following command in a terminal
  - `git clone https://github.com/Lowe54/Support-Software-Inc`
- If you wish to change the default directory to where the project is checked out to, use the following command
  - `git clone https://github.com/Lowe54/Support-Software-Inc *FolderName*`

### Local Deployment

1) Clone the repository using the commands in the Github Cloning section above
2) This project in windows runs on a virtual environment, in order to create one, use the following command
  `python3 -m venv .venv`
3)Once the virtual environment has been created, active the virtual environment with `source *path-to-virtual-environment*Scripts/activate`
4)Run `pip install -r requirements.txt`

Follow the steps for Heroku, Stripe and Amazon Web Services Deployment

### Heroku Deployment

[AppOverview]: documentationImages/heroku/app_overview.png
[AppCreate]: documentationImages/heroku/app_create.png
[AppAutoDeploy]: documentationImages/heroku/app_automatic_deploy.png
[AppManualDeploy]: documentationImages/heroku/app-manual-deployment.png
[AppSettingsLink]: documentationImages/heroku/app_Settings_link.png
[AppConfigVars]: documentationImages/heroku/app_config_var_button.png

1) If you already have an heroku account, please go to step 4 after signing in
2) Go to [https://signup.heroku.com/](https://signup.heroku.com/)
3) Fill out the registration form
4) Once on the app overview (See below), click on 'New -> Create new app'
![AppOverview]

5) Enter an app-name and choose the region, then click on 'Create App'

![AppCreate]
<!-- markdownlint-disable MD029 -->
6) Now choose the deployment method, there are 3 options
<!-- markdownlint-enable-->
  a) Heroku CLI (Command Line Interface)

  b) GitHub Deployment

  c) Container Registry (Docker)

For option 'a', follow the instructions given, for 'b', you will be asked to
link to a github account and for 'c', again follow the instructions given.

For this project, I went with the github deployment for simplicity, as it only
meant one push per deployment.

Once linked, You can enable automatic deploys based off a branch
![AppAutoDeploy]
Or perform a manual deployment
![AppManualDeploy]

In order for the app to run however, certain environment variables need to be set.

From the application overview page, click on 'Settings'

![AppSettingsLink]

Then click on 'Reveal Config Vars'

![AppConfigVars]

You need to add the following variables
<!--markdownlint-disable MD013 MD034 -->
| Config var name       | Purpose                                                                                    | Available Options  | Notes                                                                            |
|-----------------------|--------------------------------------------------------------------------------------------|--------------------|----------------------------------------------------------------------------------|
| AWS                   | If set to 1, will use AWS to serve styling and javascript                                  | 1 = Yes, 0 = No    |                                                                                  |
| AWS_ACCESS_KEY_ID     | Amazon Web Services Access Key                                                             | Supplied by AWS    | See AWS Deployment                                                               |
| AWS_SECRET_ACCESS_KEY | Amazon Web Services Secret Access Key                                                      | Supplied by AWS    | See AWS Deployment                                                               |
| DATABASE_URL          | Postgres DB URL, Auto populated once postgres is added to the Heroku App (See steps below) | Auto-Populated     | You can populate with your own database URL if it's hosted seperately.           |
| DEV                   | Development mode                                                                           | 1 = Yes, 0 = No    | DO NOT ENABLE IN PRODUCTION                                                      |
| SECRET_KEY            | Django Secret Key                                                                          |                    | https://miniwebtool.com/django-secret-key-generator/ recommended to generate one |
| STRIPE_SECRET         | Stripe's Secret Key                                                                        | Supplied by Stripe | See Stripe Deployment                                                            |

<!-- markdown-enable-->

### Stripe Deployment

**Notice: Only test keys are used in this software, if you wish to use live keys,
you will need to activate your Stripe account, and use the live keys in place
of the test ones**

[StripeKeys]: documentationImages/stripe/Keys.png

If you already have a Stripe account, please sign in [here](https://dashboard.stripe.com/login), then go to step 3

1) Go to https://dashboard.stripe.com/register
2) Fill out the register form
3) Once on the dashboard, click on the tab marked 'Your Test Keys'

![StripeKeys]

<!-- markdownlint-disable MD029 -->
4) Copy the Publishable key to the variable on line 2 in [stripe.js](static/js/stripe.js)
5) Click on the 'eye' icon next to the secret key, then copy the resulting key to the 'STRIPE_SECRET' in your environment variables in Heroku

### Setting up Amazon Web Services (AWS)

[AWSConfigOptions]: documentationImages/aws/AWS_s3_ConfigOptions.png
[AWSCreateBucket]: documentationImages/aws/AWS_s3_CreateBucket.png
[AWSCreateBucketModalP4]: documentationImages/aws/AWS_s3_CreateBucket_Modal_P4.png
[AWSSetPermissions]: documentationImages/aws/AWS_s3_SetPermissions.png

[AWSBucketDashboard]: documentationImages/aws/AWS_s3_Step2_BucketDashboard.png
[AWSBucketPolicy]: documentationImages/aws/AWS_s3_Step2_PermissionTab_BucketPolicy.png
[AWSBucketPolicyDetail]: documentationImages/aws/AWS_s3_Step2_PermissionTab_BucketPolicy_DetailScreen.png

[AWSIAMCreateGroup]: documentationImages/aws/AWS_s3_Step3_CreateGroupButton.png
[AWSIAMCreatePolicy]: documentationImages/aws/AWS_s3_Step3_CreatePolicyButton.png
[AWSIAMImportPolicy]: documentationImages/aws/AWS_s3_Step3_ImportPolicy.png
[AWSIAMImportPolicyJSON]: documentationImages/aws/AWS_s3_Step3_PolicyJsonScreen.png
[AWSIAMReviewPolicy]: documentationImages/aws/AWS_s3_Step3_ReviewPolicyScreen.png

[AWSIAMGroupAttachPolicy]: documentationImages/aws/AWS_s3_Step4_GroupAttachPolicyScreen.png
[AWSIAMGroupSearchPolicy]: documentationImages/aws/AWS_s3_Step4_PolicySearchScreen.png

[AWSIAMUserStep1]: documentationImages/aws/AWS_s3_Step5_NewUser_substep1.png
[AWSIAMUserStep2]: documentationImages/aws/AWS_s3_Step5_NewUser_substep2.png
[AWSIAMDownloadCredentials]: documentationImages/aws/AWS_s3_Step5_DownloadCSV.png

<!-- markdownlint-disable MD012 MD032 MD036-->
1) Go to [aws.amazon.com](https://aws.amazon.com/)
2) If you already have an account, please sign in and go to step 4, otherwise click on 'Create an AWS Account
3) Complete the registration process
4) Once signed in, search for 'S3'
5) Click on 'Create Bucket', then enter a name and region

  ![AWSCreateBucket]

6) Leave the second screen as-is

  ![AWSConfigOptions]

7) On the third screen, untick all options but leave the system permissions as-is

  ![AWSSetPermissions]

8) Click on Create Bucket

  ![AWSCreateBucketModalP4]

9) On the Bucket Dashboard, click on the newly created bucket

  ![AWSBucketDashboard]

10) Click on Permissions -> 'Bucket Policy'

  ![AWSBucketPolicy]

11) In this editor, copy the config found in [Bucket Policy](documentationImages/aws/BucketPolicy.txt).
  **Please make a note of the ARN Number, as you will need this later**

  ![AWSBucketPolicyDetail]

12) Go to the Cors Config, and paste the content from [CORS Config](documentationImages/aws/CorsConfig.txt)

13) Navigate to the AWS dashboard, and search for IAM (Identity and Access Management)
14) Click on Groups -> Create Group

  *Best practice here is to keep in theme with the Bucket name*

  ![AWSIAMCreateGroup]

  

15) Proceed through all the steps, do not change anything
16) Now Click on Policies -> Create Policy
  ![AWSIAMCreatePolicy]

17) Click on JSON -> Import Managed Policy
18) Search for S3, and click on the 'Full Access' -> Import

  ![AWSIAMImportPolicy]

19) Replace the JSON with the text in [policyjson.txt](documentationImages/aws/PolicyJSON.txt)
  ![AWSIAMImportPolicyJSON]

20) Click on 'Review Policy'
21) Enter the policy name e.g (bucket-milestone-policy)
22) Click on Create Policy
  ![AWSIAMReviewPolicy]

23) Now go back to 'groups' and click on the group you created
24) Click on Permissions -> Attach Policy
  ![AWSIAMGroupAttachPolicy]

25) Search for the policy you just created, tick the box next to it, and click on 'Attach'
  ![AWSIAMGroupSearchPolicy]

26) Now Go to the Users, and click on 'Add User'
27) Enter the User's name
28) Set their permissions to 'Programmatic Access'
  ![AWSIAMUserStep1]

29) Tag them to the created policy, then click on 'Next'
30) Do not enter any, tags, click on 'Review'
31) Click on 'Create User'
32) Download the csv containing the credentials
  ![AWSIAMDownloadCredentials]

33) Set the AWS_ACCESS_KEY and AWS_ACCESS_SECRET_KEY in the environment vars in Heroku

## Testing

For all testing ran on this site, please refer to [TESTING.md](TESTING.md)

## Credits

[Jesse Couch](https://codepen.io/designcouch/pen/Atyop) for the burger bar animation.

[WebFikirleri](https://codepen.io/WebFikirleri/pen/MLXYKm) for the floating action button
