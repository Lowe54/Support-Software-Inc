# Testing File

- [Testing File](#testing-file)
  - [Manual Testing](#manual-testing)
  - [Known Bugs](#known-bugs)
  - [User story testing](#user-story-testing)
  - [Code Validation](#code-validation)
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

## Manual Testing

| Test Number | Section of Site         | What is the test                                                                        | What Should Happen                                                                         | What Actually Happened         | Actions to take (If applicable)                          |
|-------------|-------------------------|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|--------------------------------|----------------------------------------------------------|
| 1           | Side Menu Functionality | Click on 'Burger Bar'                                                                   | Side menu should open                                                                      | Side menu opened               | N/A                                                      |
| 2           | Side Menu Functionality | Click on 'Cross'                                                                        | Side menu should close                                                                     | Side menu closed               | N/A                                                      |
| 3           | Side Menu Links         | Not Signed in - click on 'Home'                                                         | Redirect to Index page                                                                     | Redirected to index page       | N/A                                                      |
| 4           | Top Menu Links          | Not Signed in - click on 'Login'                                                        | Redirect to Login page                                                                     | Redirected to Login page       | N/A                                                      |
| 5           | Top Menu Links          | Not Signed in - click on 'Register'                                                     | Redirect to Register page                                                                  | Redirected to Register page    | N/A                                                      |
| 6           | Side Menu Links         | Signed In - Click on 'Dashboard'                                                        | Redirect to Dashboard page                                                                 | Redirected to dashboard page   | N/A                                                      |
| 7           | Side Menu Links         | Signed In - Click on 'Add Ticket'                                                       | Redirect to Add Ticket page                                                                | Sent to add ticket page        | N/A                                                      |
| 8           | Side Menu Links         | Signed In - Click on 'Organisations'                                                    | Redirect to Organisation List                                                              | Sent to Organisation list      | N/A                                                      |
| 9           | Side Menu Links         | Signed In - Click on 'Admin'                                                            | User sent to admin site                                                                    | Sent to admin site             | N/A                                                      |
| 10          | Side Menu Links         | Quick links (Agent User) - Click on 'Unassigned Requests'                               | User should be sent to results page containing all unassigned requests                     | Sent to correct results page   | N/A                                                      |
| 11          | Side Menu Links         | Quick links (Agent User) - Click on 'Requests assigned to me'                           | User should be sent to results page containing all requests assigned to the logged in user | Sent to correct results page   | N/A                                                      |
| 12          | Side Menu Links         | Quick links (Agent User) - Click on 'Open Requests'                                     | User should be sent to results page containing all open requests                           | Sent to correct results page   | N/A                                                      |
| 13          | Top Links               | Signed in - Click on Username -> My Profile                                             | Redirect to My Profile page                                                                | Sent to my profile page        | N/A                                                      |
| 14          | Add Ticket page         | Add a new request                                                                       | New ticket should be saved to database                                                     | Ticket saved                   | N/A                                                      |
| 15          | Request List            | Enter 'Test' in the keyword search box and filter                                       | Requests that contain 'Test' in the title should be returned                               | Correct results returned       | N/A                                                      |
| 16          | Request List            | Filter by 'Open' Status                                                                 | Requests that have a status of 'Open' should be returned                                   | Correct results returned       | N/A                                                      |
| 17          | Request List            | Filter by 'Low' Priority                                                                | Requests that have a priority of 'Low' should be returned                                  | Correct results returned       | N/A                                                      |
| 18          | Request List            | Enter 'Test' in the keyword search box and select 'Closed' in the status filter         | Requests that contain 'Test in the title and have a status of 'closed' should be returned  | Correct results returned       | N/A                                                      |
| 19          | Ticket                  | (Agent User) - Click on Menu (Bottom Left) -> Edit Request Details and change a value   | Request details should be changed                                                          | Request updated                | N/A                                                      |
| 20          | Ticket                  | (Agent User) - Click on Menu (Bottom Left) -> Add comment , set Internal comment to yes | Comment set as internal should be added                                                    | Internal comment added         | N/A                                                      |
| 21          | Ticket                  | (Agent User) - Click on Menu (Bottom Left) -> Add comment , set Internal comment to no  | Comment set as public should be added                                                      | Public comment added           | N/A                                                      |
| 22          | Ticket                  | (Agent User) - Click on Menu (Bottom Left) -> Close request                             | Request closure popup should be shown, on completion request should be closed              | Comment closed on completion   | Known bug following on from this, see known bugs section |
| 23          | Ticket                  | (Agent User) - Unassigned request - Click on 'take it'                                  | Request should be assigned to logged in user                                               | Request assigned               | N/A                                                      |
| 24          | Ticket                  | (End User) - Click on Menu (Bottom Left) -> Add comment                                 | Comment should be added                                                                    | Comment added                  | N/A                                                      |
| 25          | Ticket                  | (End User) - Click on Menu (Bottom Left) -> Edit Request Details                        | Request details should be altered                                                          | Request Updated                | N/A                                                      |
| 26          | Organisation            | Click on Menu (Bottom Left) -> Add Organisation                                         | New organisation entered should be added                                                   | Organisation Added             | N/A                                                      |
| 27          | Organisation            | Click on Edit Organisation -> Enter value in popup box                                  | Organisation name should be updated to value entered                                       | Title updated                  | N/A                                                      |
| 28          | Organisation            | Click on Attached Users -> Associate a user -> tick Unassociated user -> Associate      | User should be associated                                                                  | User associated                | N/A                                                      |
| 29          | Organisation            | Click on Attached Users -> Remove from organisation below a user                        | User should removed from organisation                                                      | User removed from organisation | N/A                                                      |
| 30          | Request list            | (End User Only) - Filter by Open requests                                               | Requests that the logged in user has raised and has a status of  'Open' should be returned | Correct results returned       | N/A                                                      |
| 31          | Request list            | (End User Only) On load with no filters applied                                         | Only requests that the logged in user has raised should be returned                        | Correct results returned       | N/A                                                      |
| 32          | Dashboard               | (End User) - Click on 'View my open requests'                                           | Redirect to results page showing all logged in users open requests                         | Correct results returned       | N/A                                                      |
| 33          | Dashboard               | (End User) - Click on 'View my requests needing a reply'                                | Redirect to results page showing all logged in users pending requests                      | Correct results returned       | N/A                                                      |

## Known Bugs

1) After closing a ticket, until the page is refreshed comments can still be added

## User story testing

| User story number | How it was achieved                                                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 1                 | Once signed in, Click into the request, all updates are present at the bottom                                                            |
| 2                 | Once signed in and within a request, click on the bottom menu, add a comment, this is then added to the request without being redirected |
| 3                 | There is a search form on the results page that allows for this filtering                                                                |
| 4                 | Once signed in, Open the side menu, and click on 'all my open requests'                                                                  |
| 5                 | Once signed in, click on your username and go to 'My Profile' -> Edit button on the right                                                |
| 6                 | Once signed in, open the side menu and click on 'View my Pending request'                                                                |
| 7                 | Once signed in, in the associate user form, you can select multiple users to associate to an organisation                                |

## Code Validation

### HTML
<!-- markdownlint-disable MD034-->
| Page              | Template file                              | Result | Confirmation link / How it was validated                                                                                            | Notes                                                                              |
|-------------------|--------------------------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Home page         | core/templates/index.html                  | PASS   | https://validator.w3.org/nu/?doc=https%3A%2F%2Fsupportsoftwareinc.herokuapp.com%2F                                                  |                                                                                    |
| Result            | ticket/templates/results.html              | FAIL   | Manually entered page source of https://supportsoftwareinc.herokuapp.com/results into validator                                     | Fails because Crispy Forms is adding blank `<div id="" class="">`  around the labels |
| Add Form          | ticket/templates/add_ticket.html           | PASS   | Manually entered page source of https://supportsoftwareinc.herokuapp.com/ticket/add/ into validator                                 | Link not provided as the validator cannot check pages that require a login         |
| Dashboard         | ticket/templates/dashboard.html            | PASS   | Manually entered page source of https://supportsoftwareinc.herokuapp.com/dashboard into validator                                   | Link not provided as the validator cannot check pages that require a login         |
| Organisation List | organisations/templates/organisation_list  | PASS   | Manually entered page source of https://supportsoftwareinc.herokuapp.com/organisations/list into validator                          | Link not provided as the validator cannot check pages that require a login         |
| My Profile Page   | authentication/templates/profile_view.html | PASS   | Manually entered page source of https://supportsoftwareinc.herokuapp.com/auth/profile into validator                                | Link not provided as the validator cannot check pages that require a login         |
| Ticket            | ticket/templates/ticket.html               | PASS   | Manually entered page source of https://supportsoftwareinc.herokuapp.com/ticket/86ba6d9c-c748-4398-9f24-5fba4c1a2de8 into validator | Link not provided as the validator cannot check pages that require a login         |
| Login             | authentication/templates/login.html        | PASS   | https://validator.w3.org/nu/?doc=https%3A%2F%2Fsupportsoftwareinc.herokuapp.com%2Fauth%2Flogin                                      |                                                                                    |
| Register          | authentication/templates/register.html     | PASS   | https://validator.w3.org/nu/?doc=https%3A%2F%2Fsupportsoftwareinc.herokuapp.com%2Fauth%2Fregister                                   |                                                                                    |                                                                   |
<!-- markdownlint-enable-->
### Javascript

All Javascript was tested via [JSHint](https://jshint.com/docs/), the results
against each of the js files within the software can be found below

#### Core.js

![Core JS Result](/documentationImages/corejs_result.png)

Undefined Variables Listed

- Swal
  - This is a Sweetalert 2 alert initialisation

- introJS
  - This is used by IntroJS, which is the guided tooltips that are activated via the 'help' button
  
- stripe_init
  - This is one of the functions defined in stripe.js

#### Profile.js

![Core JS Result](/documentationImages/corejs_result.png)

#### Organisation.js

![Organisation JS Result](/documentationImages/organisationjs_result.png)

#### Stripe.js

![Stripe JS Result](/documentationImages/stripejs_result.png)

#### Ticket.js

![Ticket JS Result](/documentationImages/ticketjs_result.png)

### Python

[Pylint](https://www.pylint.org/) was used in order to check the conformity of the code to PEP8 standard, as part of this the code report for the site is available [here](pylint.html).

This report is generated via the following commands once the software has been installed

`pylint --output-format=jsonextended authentication core comments organisations payments ticket > pylint.json`

`pylint-json2html -f jsonextended -o pylint.html pylint.json`

The final report can be found [here](pylint.html)

Two refactor codes have been suppressed, the codes and the reasons for suppression are listed in the below table

| Code                  | Reason for suppression                          |
|-----------------------|-------------------------------------------------|
| too-many-branches     | Function contains the filter functionality      |
| simplify-if-statement | See Known Bugs / Issues in main Readme.md File  |

## Automated Testing

### Continuous Integration

This project has a CI implementation with [Travis CI](https://travis-ci.com/), the only enforcement is for the import order, which is determined via the `.travis.yml` file. This is enforced via the `isort --check-only --diff --skip-glob=*/migrations/*` command. In addition it also runs all tests present (See below table)
<!-- markdownlint-disable MD013 MD036-->
**NOTE: While the status checked for is 302, it actually redirects the user to the login page**

| Test Number | Module         | What is it testing?                                                                  |
|-------------|----------------|--------------------------------------------------------------------------------------|
| 1           | Authentication | Testing that the login page returns status 200                                       |
| 2           | Authentication | Testing that the register page returns status 200                                    |
| 3           | Core           | Testing that the index page returns status 200                                       |
| 4           | Organisation   | Checks to see if the organisation list page returns 302 if the user is NOT logged in |
| 5           | Organisation   | Checks to see if the organisation list page loads if the user is logged in           |
| 6           | Ticket         | Confirms the default status of a new ticket is Open (OPN in the DB)                  |
| 7           | Ticket         | Confirms the default priority of a new ticket is Low                                 |
| 8           | Ticket         | Tests that the dashboard returns 302 if the user is not signed in                    |
| 9           | Ticket         | Tests that the dashboard returns 200 if the user is signed in                        |
<!-- markdownlint-enable-->