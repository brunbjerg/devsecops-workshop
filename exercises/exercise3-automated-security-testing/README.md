
# Exercise 3: Advanced Automated Security Testing

## Objective
This exercise focuses on expanding the automated security testing within your CI/CD pipeline. You will integrate advanced security tools to perform dynamic application security testing (DAST), check for insecure configurations, and audit your application's dependencies. The goal is to further enhance the security posture of your Python Flask application through comprehensive automated testing.

## Prerequisites
- Experience with CI/CD pipelines and GitHub Actions.
- Familiarity with Python, Flask, and basic security concepts.
- Basic understanding of security testing tools.

## Tools Used
- **OWASP ZAP**: For dynamic application security testing (DAST).
- **Safety**: For Python dependency security checks.
- **Bandit**: For static analysis to find security issues in Python code.
- **GitHub Actions**: For automating security testing in the CI/CD pipeline.

## Repository Structure
Your repository should be structured as follows:

\`\`\`plaintext
exercise3-advanced-security-testing/
│
├── .github/
│   └── workflows/
│       └── advanced-security.yml
├── app.py
└── requirements.txt
\`\`\`

## Instructions

### Step 1: Set Up Your Environment

1. **Clone the Repository**:
   Start by cloning the repository and navigating to the `exercise3-advanced-security-testing` directory:

   \`\`\`bash
   git clone <repository-url>
   cd exercise3-advanced-security-testing
   \`\`\`

2. **Install Required Python Packages**:
   Install all the required Python packages by running:

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

### Step 2: Configure GitHub Actions for Advanced Security Testing

In this step, you will configure GitHub Actions to automate advanced security testing using multiple tools.

1. **Create the GitHub Actions Workflow**:
   Create a `.github/workflows/advanced-security.yml` file to define the CI/CD pipeline.

   \`\`\`yaml
   name: Advanced Security Testing Pipeline

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
         working-directory: exercise3-advanced-security-testing

       - name: Run Bandit for static analysis
         run: bandit -r .
         working-directory: exercise3-advanced-security-testing

       - name: Run Safety for dependency checks
         run: safety check
         working-directory: exercise3-advanced-security-testing

       - name: Run OWASP ZAP for DAST
         uses: zaproxy/action-full-scan@v0.6.0
         with:
           target: 'http://localhost:5000'
         env:
           JAVA_TOOL_OPTIONS: "-Djava.awt.headless=true"
   \`\`\`

### Explanation:
- **Bandit**: Runs static analysis to identify security issues in your Python code.
- **Safety**: Audits Python dependencies for known vulnerabilities.
- **OWASP ZAP**: Performs dynamic analysis of the running web application to detect vulnerabilities.

2. **Commit and Push the Workflow**:
   After creating the `advanced-security.yml` file, commit and push it to your repository:

   \`\`\`bash
   git add .github/workflows/advanced-security.yml
   git commit -m "Add advanced security testing workflow"
   git push
   \`\`\`

### Step 3: Running the Advanced Security Tests

1. **Trigger the Pipeline**:
   Any push or pull request to the repository will automatically trigger the GitHub Actions pipeline. The pipeline will execute the advanced security tests defined in the `advanced-security.yml` file.

2. **Monitor the Pipeline**:
   Go to the "Actions" tab in your GitHub repository to monitor the progress and results of the pipeline.

   - **Bandit**: Review any static security issues found in your Python code.
   - **Safety**: Check for vulnerabilities in your dependencies.
   - **OWASP ZAP**: Review the DAST scan results to identify any potential vulnerabilities.

3. **Review and Fix Issues**:
   If any issues are flagged by Bandit, Safety, or OWASP ZAP, fix them in your code and push the changes. The pipeline will re-run automatically to verify the fixes.

### Step 4: Running Security Tests Locally

Although the CI/CD pipeline automates security testing, it is also important to run these tests locally before pushing code.

1. **Run Bandit Locally**:
   Use Bandit to scan your Python code for security issues:

   \`\`\`bash
   bandit -r .
   \`\`\`

2. **Run Safety Locally**:
   Audit your Python dependencies for vulnerabilities:

   \`\`\`bash
   safety check
   \`\`\`

3. **Run OWASP ZAP Locally**:
   Perform dynamic analysis using OWASP ZAP by running it against your locally hosted application.

   - **Start your Flask application locally**:

     \`\`\`bash
     python app.py
     \`\`\`

   - **Launch OWASP ZAP and configure it to scan your running application**.

4. **Fix Issues Locally**:
   Review the results from the local scans, fix any issues, and rerun the tests until no issues are detected.

### Conclusion

By following these steps, you have set up an advanced security testing pipeline that integrates multiple security tools into your CI/CD process. This setup ensures comprehensive security testing, covering static analysis, dependency checks, and dynamic application security testing. It significantly enhances the security of your Python Flask application and helps prevent vulnerabilities from reaching production.
