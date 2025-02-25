CI/CD Implementation Report

Project Overview

This project is a simple Flask web application that includes a basic API with two endpoints:

/ - Returns a JSON message {"message": "Hello, CI/CD!"}.

/add/<a>/<b> - Accepts two integer parameters and returns their sum in JSON format.

The project is configured with a Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions to automate testing and deployment.

Task 1: Setting Up the Project Repository

Repository Creation: The project repository was set up on GitHub.

Project Structure:

src/ - Contains app.py (Flask web application).

tests/ - Contains test cases for the application.

.github/workflows/ci.yml - GitHub Actions workflow file for CI/CD automation.

README.md - Project documentation.

requirements.txt - Lists the dependencies required for the application.

README File: A README file was created to explain the purpose of the project.

Task 2: Writing Test Cases

Implemented two test cases using pytest:

Test to check if the home route (/) returns the correct JSON response.

Test to verify the /add/<a>/<b> route returns the correct sum.

Tests were executed locally using pytest before automating them in the CI/CD pipeline.

Task 3: Configuring CI/CD Pipeline

GitHub Actions Workflow: A CI/CD pipeline was set up in .github/workflows/ci.yml with the following steps:

Checkout the repository.

Set up Python 3.12.

Install dependencies from requirements.txt.

Run test cases using pytest.

The pipeline is triggered on:

Pushes to the main branch.

Pull requests targeting the main branch.

Optional Deployment (Future Scope): The pipeline can be extended to deploy the application to Heroku, AWS, or a Docker container.

Task 4: Executing and Debugging the CI/CD Pipeline

Push Changes: The project files were pushed to the GitHub repository.

Pipeline Execution: The GitHub Actions workflow executed successfully, running the test cases.

Debugging: The pipeline logs were reviewed to ensure all steps ran without errors.

Fixes: Issues, if any, were resolved, and the pipeline was re-executed successfully.