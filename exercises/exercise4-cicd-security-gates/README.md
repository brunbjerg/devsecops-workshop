
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

\`\`\`plaintext
ex4-cicd-security-gates/
│
├── .github/
│   └── workflows/
│       └── ci-cd-security.yml
├── app.py
└── requirements.txt
\`\`\`

## Instructions

### Step 1: Set Up Your Environment

1. **Clone the Repository**:
   Start by cloning the repository and navigating to the `ex4-cicd-security-gates` directory:

   \`\`\`bash
   git clone <repository-url>
   cd ex4-cicd-security-gates
   \`\`\`

2. **Install Required Python Packages**:
   Install all the required Python packages by running:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

### Step 2: Implement Basic Application with Security Practices

1. **Create `app.py`**:
   Implement basic secure coding practices in your Flask application, such as password hashing with `bcrypt` and JWT authentication.

   Example:

   \`\`\`python
   import os
   from flask import Flask, request, jsonify
   import bcrypt
   import jwt
   import datetime

   app = Flask(__name__)

   # Load the secret key from an environment variable
   SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'default_secret_key')
   users = {}  # In-memory storage (for simplicity)

   @app.route('/register', methods=['POST'])
   def register():
       username = request.json.get('username')
       password = request.json.get('password')
       
       # Hash the password using bcrypt
       hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
       users[username] = hashed_password

       return jsonify({"message": "User registered successfully"}), 201

   @app.route('/login', methods=['POST'])
   def login():
       username = request.json.get('username')
       password = request.json.get('password')

       # Fetch the hashed password from storage
       hashed_password = users.get(username)

       if hashed_password and bcrypt.checkpw(password.encode('utf-8'), hashed_password):
           # Generate a JWT token
           token = jwt.encode({
               'username': username,
               'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
           }, SECRET_KEY, algorithm='HS256')

           return jsonify({'token': token}), 200

       return jsonify({"message": "Invalid credentials"}), 401

   if __name__ == '__main__':
       app.run(debug=False)
   \`\`\`

2. **Create `requirements.txt`**:
   Define the necessary dependencies for your project.

   \`\`\`plaintext
   Flask==2.0.1
   bcrypt==3.2.0
   pyjwt==2.0.1
   \`\`\`

### Step 3: Set Up a CI/CD Pipeline with Security Gates

1. **Create a GitHub Actions Workflow**:
   Create a `.github/workflows/ci-cd-security.yml` file in your repository to define the CI/CD pipeline with security gates.

   \`\`\`yaml
   name: CI/CD with Security Gates

   on: [push, pull_request]

   jobs:
     security-tests:
       runs-on: ubuntu-latest

       steps:
       - name: Checkout code
         uses: actions/checkout@v2

       - name: Set up Python
         uses: actions/setup-python@v2
         with:
           python-version: '3.9'

       - name: Install dependencies
         run: |
           pip install -r requirements.txt
           pip install bandit safety
         working-directory: ex4-cicd-security-gates

       - name: Run Bandit for static analysis
         run: bandit -r .
         working-directory: ex4-cicd-security-gates

       - name: Run Safety for dependency checks
         run: safety check
         working-directory: ex4-cicd-security-gates

       - name: Run OWASP ZAP for DAST
         uses: zaproxy/action-full-scan@v0.6.0
         with:
           target: 'http://localhost:5000'
         env:
           JAVA_TOOL_OPTIONS: "-Djava.awt.headless=true"
           JWT_SECRET_KEY: ${{ secrets.JWT_SECRET_KEY }}

     deploy:
       runs-on: ubuntu-latest
       needs: security-tests

       steps:
       - name: Deploy to Production
         run: |
           echo "Deploying to production..."
         if: success()
         env:
           JWT_SECRET_KEY: ${{ secrets.JWT_SECRET_KEY }}
   \`\`\`

2. **Explanation of the Workflow**:
   - **Checkout code**: Retrieves the latest code from the repository.
   - **Set up Python**: Configures the Python environment.
   - **Install dependencies**: Installs project dependencies and security tools.
   - **Run Bandit**: Performs static analysis to identify security issues in the code.
   - **Run Safety**: Checks for known vulnerabilities in Python dependencies.
   - **Run OWASP ZAP**: Conducts dynamic application security testing.
   - **Deploy**: Deploys the application to production only if all security gates are passed.

3. **Commit and Push the Workflow**:
   After creating the `ci-cd-security.yml` file, commit and push it to your repository:

   \`\`\`bash
   git add .github/workflows/ci-cd-security.yml
   git commit -m "Add CI/CD pipeline with security gates"
   git push
   \`\`\`

### Step 4: Set the Environment Variable

To avoid hardcoding the JWT secret key in your application, set the `JWT_SECRET_KEY` environment variable.

- **For Development**:
  
  Set a value that you can use locally:

  \`\`\`bash
  export JWT_SECRET_KEY='your_development_secret_key'
  python app.py
  \`\`\`

- **For Production**:

  Set a more secure key:

  \`\`\`bash
  export JWT_SECRET_KEY='your_production_secret_key'
  python app.py
  \`\`\`

### Step 5: Running the Pipeline

1. **Trigger the Pipeline**:
   The GitHub Actions pipeline will automatically run on every push or pull request.

2. **Monitor the Pipeline**:
   Go to the "Actions" tab in your GitHub repository to monitor the pipeline's progress.

3. **Review and Fix Issues**:
   If any security issues or vulnerabilities are flagged by Bandit, Safety, or OWASP ZAP, fix them in your code and push the changes. The pipeline will re-run automatically to verify the fixes.

4. **Deployment**:
   The application will be deployed to production only if all security tests pass successfully.

### Conclusion

By completing this exercise, you have set up a CI/CD pipeline with security gates that ensure your Flask application is secure before it is deployed to production. Additionally, you have learned how to manage sensitive information like the JWT secret key securely using environment variables, preventing potential security risks.
