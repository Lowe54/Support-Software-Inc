# Testing.md File

- [Testing.md File](#testingmd-file)
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

## Code Validation

### HTML

| Page              | Template file                              | Result | Confirmation link (If PASS) | Notes                                        |
|-------------------|--------------------------------------------|--------|-----------------------------|----------------------------------------------|
| Home page         | core/templates/index.html                  | PASS   |                             |                                              |
| Result            | ticket/templates/results.html              | FAIL   |                             | Fails due to how crispy forms renders labels |
| Add Form          | ticket/templates/add_ticket.html           | PASS   |                             |                                              |
| Dashboard         | ticket/templates/dashboard.html            | PASS   |                             |                                              |
| Organisation List | organisations/templates/organisation_list  | PASS   |                             |                                              |
| My Profile Page   | authentication/templates/profile_view.html | PASS   |                             |                                              |
| Ticket            | ticket/templates/ticket.html               | PASS   |                             |                                              |
| Login             | authentication/templates/login.html        | PASS   |                             |                                              |
| Register          | authentication/templates/register.html     | PASS   |                             |                                              |

### Javascript

All Javascript was tested via [JSHint](https://jshint.com/docs/), the results against each of the js files within the software can be found below

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

The reason for the sole error is that the function controls the result filters.

## Automated Testing

### Continuous Integration

This project has a CI implementation with [Travis CI](https://travis-ci.com/), the only enforcement is for the import order, which is determined via the `.travis.yml` file. This is enforced via the `isort --check-only --diff --skip-glob=*/migrations/*` command.
