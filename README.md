**Resolve Automation Assessment**

This repository contains my solution for the Resolve Automation Engineer student Co-op assessment.

The tests were written using Selenium and Pytest to interact with the provided HTML test page and complete the tasks listed in the guide.

**What I used:**

- Python 3
- Selenium WebDriver
- Pytest
- Google Chrome


**How to run (selenium.dev)**

- Start the local web server from the project folder: `python -m http.server 8000`
- Create and activate a virtual environment:  `python -m venv .venv`
  Windows:
  `.\.venv\Scripts\Activate.ps1`
  Mac/Linux:
  `source .venv/bin/activate`
- TO install dependencies: `pip install -r requirements.txt`
- To run the tests: `pytest -q`

**Tests**

- Test 1 checks that the login fields and button exist and allows entering values
- Test 2 checks the list items and badge values
- Test 4 checks enabled and disabled buttons
- Test 5 waits for a delayed button, clicks it, and checks the success message
- Test 6 reads values from the table and verifies a specific cell

**Notes**
- Explicit waits were used where needed due to random delays on the page
- Element selectors are scoped to each test section to keep things simple

Resource used: ****https://www.selenium.dev/documentation/webdriver/getting_started/first_script/****

_Aniketh Srinivasa Kini_
