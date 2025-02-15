# Overview

We have a simple web application that consists of two primary components:
- A Front-End UI: A web page where a user can input their name and submit it.
        When the user enters a name and clicks the submit button, the name is sent to a Python-based REST API.
        The page then displays a confirmation message with the submitted name.

- A Python REST API (`app.py`): A simple backend built using Flask that accepts POST requests at the endpoint /submit-name. This API accepts a JSON payload with a name field, processes it, and responds with a confirmation message, e.g., { "message": "Name submitted successfully: <name>" }.

Your task is to demonstrate how you would go about testing both the UI and the API. 

Expected Skills to Assess:

- UI Testing: Familiarity with tools like Selenium, Cypress, or Playwright for testing the web page, form validation, and dynamic content rendering.
- API Testing: Understanding of API testing frameworks such as pytest, requests, or Postman, and experience writing tests for REST endpoints.
- End-to-End Testing: Knowledge of how to combine both UI and API testing to simulate real-world scenarios, such as testing form submissions that hit the API.


# Instructions
This exercise is intended to be 1-1.5 hours in duration. Please complete the following tasks and submit your solution by adding the following github accounts to your forked repository:
- sburkequindar
- zachmeza
- MKLeb

Tasks:
- Get the code running locally 
    - These are simple components, but documentation is sparsecdand we've introduced a couple minor bugs in each
    - Update the Setup instructions below with steps to run frontend and backend
- Utilizing Playwright (and optionally any additional unit-level or other tests you'd  like to add), set up initial testing in this repository to validate behavior of the frontend and backend (please spend no more than 1 hour on this step)
- If you have time, build (or draft) a github action which would run your tests on any merge
- Update the Testing section of this README to describe
    - Your approach and instructions for testing this app
    - Next steps you would take to bake tests into CI/CD
    - Any feedback you'd like to give the developers on the components you've been given


# Setup

Documentation is somewhat sparse here intentionally. As you get the components running, please update instructions here wtih an improved set of instructions (and feel free to make updates to the repo itself for cleaner setup!).

## Setup Project Dependencies

**Python App**

- Ensure you have [Python](https://www.python.org) installed.
- Create a virtual environment with `python -m venv venv`.
- Activate the virtual environment with `source venv/bin/activate` (or `venv\Scripts\activate` on Windows).
- Install Flask with `pip install Flask`.
- Install Flask-Cors with `pip install Flask-Cors`.

**Frontend**

- Ensure you have [Node.js](https://nodejs.org) installed.
- Install HTTPie with `pip install httpie`.
- Install http-server with `npm install -g http-server`.
- Install Frontend: 
   - Navigate to the frontend `simple-ts-ui` directory
   - Install frontend dependencies with `npm install`.

** Testing Dependencies **

- Pytest is installed with `pip install pytest`.
- Playwright is installed with `pip install pytest-playwright`.
- Playwright dependencies are installed with `playwright install`.

## Run the Python app
- Run the app itself with `python app.py` from the project root directory.

## Run the frontend
- The frontend itself can be run with `http .` (or `http-server .` on Windows) from the `simple-ts-ui` directory

# Testing Approach

## Playwright E2E Testing

### API Testing

These tests are going to focus on various data input validations performed and ensure that the API is responding as expected.

To execute the test, run the following command from the project root directory `pytest tests/test_api.py`.

### UI Testing

These tests are going to focus on the UI components of the application. We will be testing the form input, submission, and the confirmation message.

To execute the test, run the following command from the project root directory `pytest tests/test_ui.py`.

## Github Action

- **playwright.yml**:  This action will execute the Playwright tests on any merge to the main branch & any pull requests to the main branch.
