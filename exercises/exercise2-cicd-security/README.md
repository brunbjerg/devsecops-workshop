# Exercise 2: Building a Security-Focused CI/CD Pipeline

## Objective
This exercise focuses on setting up a minimal security-focused CI/CD pipeline for a Python Flask application. You will learn how to configure the pipeline to automatically enforce security checks, handle environment configurations, and ensure the application is ready for production.

## Prerequisites
- Basic knowledge of CI/CD concepts.
- Familiarity with GitHub Actions.
- Basic knowledge of Python and Flask.

## Tools Used
- **GitHub Actions**: For CI/CD automation.
- **Bandit**: For static analysis to find security issues in Python code.
- **pip-audit**: For Python dependency vulnerability scanning.

## Repository Structure
Your repository should be structured as follows:

```plaintext
exercise2-cicd-pipeline/
│
├── .github/
│   └── workflows/
│       └── security.yml
├── app.py
└── requirements.txt

##Environment Setup
To ensure that your Flask application is secure and follows best practices, it is important to manage the FLASK_DEBUG environment variable correctly.

For Development: You can enable debug mode to get detailed error messages and the interactive debugger.


export FLASK_DEBUG=true  # for development
For Production: Debug mode should be disabled to prevent the exposure of sensitive information and to avoid the risk of arbitrary code execution.


export FLASK_DEBUG=false  # for production
##Addressing the Flask Debug Mode Issue
Bandit has flagged the use of debug=True in your Flask application as a security risk because it exposes the Werkzeug debugger, which can execute arbitrary code. Here’s how to resolve it:

Modify app.py to Control Debug Mode with Environment Variables:
Ensure your Flask application does not have debug=True hardcoded. Instead, use environment variables to control the debug mode.

Before:

if __name__ == '__main__':
    app.run(debug=True)

After:


import os

if __name__ == '__main__':
    # Control debug mode via environment variables
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)

##GitHub Actions Workflow
The CI/CD pipeline is configured using GitHub Actions, specifically through the .github/workflows/security.yml file. This workflow is the core of the CI/CD pipeline and will automatically run on every push or pull request.

What the Workflow Does:
Installs dependencies: Sets up the Python environment and installs the necessary packages.
Runs Bandit: Performs static analysis on your Python code to find potential security issues.
Runs pip-audit: Scans your Python dependencies for known vulnerabilities.
Executes Pre-Commit Hooks (if configured): Ensures that all configured pre-commit hooks are run.
The workflow ensures that your code is secure before it gets merged into the main branch, providing an automated layer of security.

##Running Locally
To run the Flask application locally, follow these steps:

Set Up Your Environment: Ensure that the necessary dependencies are installed:


pip install -r requirements.txt
Run the Application: Start the Flask application by running:


python app.py
Depending on your environment setup, the application will run with or without debug mode.

Testing the CI/CD Pipeline
To test the CI/CD pipeline, you can make a small change to the code and push it to the repository. For example, you might add a new route in app.py:


@app.route('/hello', methods=['GET'])
def hello():
    return "Hello, World!"
After making this change:

Commit and Push Your Changes:


git add app.py
git commit -m "Add hello route"
git push
Monitor the Pipeline:

Go to the "Actions" tab in your GitHub repository to monitor the workflow.
Ensure that all checks pass, including the Bandit scan and pip-audit.
Review and Fix Issues:

If any issues are flagged by Bandit or pip-audit, fix them in your code and push the changes again. The pipeline will re-run automatically.

Conclusion
By following these steps, you have set up a minimal yet effective CI/CD pipeline that enforces security best practices for a Python Flask application. This setup integrates automated security checks into your development workflow, ensuring that your application is secure and ready for production deployment.

