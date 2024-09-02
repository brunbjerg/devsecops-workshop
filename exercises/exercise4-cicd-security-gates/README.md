# Exercise 4: CI/CD with Security Gates

## Objective
This exercise focuses on integrating security gates into your Continuous Integration and Continuous Deployment (CI/CD) pipeline. Security gates are automated checks that the code must pass before it can be deployed. These checks ensure that only secure code is deployed to production.

## Prerequisites
- Basic knowledge of CI/CD concepts.
- Familiarity with GitHub Actions.
- Experience with Python and Flask.
- A GitHub repository to host your project.

## Tools Used
- **Flask**: A lightweight web framework for Python.
- **Bandit**: For static analysis to identify security issues in your Python code.
- **Safety**: For checking Python dependencies for known security vulnerabilities.
- **OWASP ZAP**: For dynamic application security testing (DAST).
- **GitHub Actions**: For automating CI/CD with security gates.

## Repository Structure
Your repository should be structured as follows:

```plaintext
ex4-cicd-security-gates/
│
├── .github/
│   └── workflows/
│       └── ci-cd-security.yml
├── app.py
└── requirements.txt


## Explanation of the Workflow:

Checkout code: Retrieves the latest code from the repository.
Set up Python: Configures the Python environment.
Install dependencies: Installs project dependencies and security tools.
Run Bandit: Performs static analysis to identify security issues in the code.
Run Safety: Checks for known vulnerabilities in Python dependencies.
Run OWASP ZAP: Conducts dynamic application security testing.
Deploy: Deploys the application to production only if all security gates are passed.


## Running the Pipeline
Trigger the Pipeline: The GitHub Actions pipeline will automatically run on every push or pull request.

Monitor the Pipeline: Go to the "Actions" tab in your GitHub repository to monitor the pipeline's progress.

Review and Fix Issues: If any security issues or vulnerabilities are flagged by Bandit, Safety, or OWASP ZAP, fix them in your code and push the changes. The pipeline will re-run automatically to verify the fixes.

Deployment: The application will be deployed to production only if all security tests pass successfully.

# Conclusion
By completing this exercise, you have set up a CI/CD pipeline with security gates that ensure your Flask application is secure before it is deployed to production. This pipeline automatically performs security checks and allows deployment only when all security gates are passed, providing a strong security posture for your application.