# Exercise 1: Advanced Secure Coding Practices

## Objective
Enhance an existing Python web application by implementing advanced secure coding practices. The focus will be on secure authentication, data protection, and authorization controls. Additionally, you will set up pre-commit hooks to enforce security checks before any code is committed.

## Prerequisites
- Basic knowledge of Python programming.
- Familiarity with concepts of web security, including JWT, encryption, and RBAC.
- Python environment with `pip` installed.

## Tools Used
- **Python Libraries**:
  - `pyjwt`: For JSON Web Token (JWT) authentication.
  - `cryptography`: For AES encryption of sensitive data.
  - `bcrypt`: For secure password hashing.
- **Bandit**: A tool to find common security issues in Python code.
- **Pre-Commit**: A framework for managing and maintaining multi-language pre-commit hooks.

## Instructions

### Step 1: Set Up Your Environment

1. **Clone the repository** and navigate to the `exercise1-secure-coding` directory:
   ```bash
   git clone <repository-url>
   cd exercise1-secure-coding
   ```

2. **Install the required Python packages** by running:
   ```bash
   pip install -r requirements.txt
   ```

### Step 2: Harden Authentication

1. **Implement JWT for secure authentication**:
   - Use the `pyjwt` library to generate and verify JWT tokens.
   - Ensure that tokens are signed with a secure algorithm (e.g., HS256).
   - Implement token-based authentication for users logging into the application.

2. **Enforce Multi-Factor Authentication (MFA)**:
   - Implement MFA using TOTP (Time-based One-Time Password).
   - Use a library like `pyotp` to generate TOTP tokens.
   - Require users to enter a TOTP code after entering their password.

3. **Protect against brute force attacks**:
   - Implement rate limiting on login attempts.
   - Lock accounts temporarily after a certain number of failed attempts.

### Step 3: Secure Data Handling

1. **Encrypt sensitive data**:
   - Use the `cryptography` library to encrypt data at rest (e.g., user credentials, personal information).
   - Ensure data in transit is encrypted using HTTPS.

2. **Hash passwords securely**:
   - Use `bcrypt` to hash and securely store user passwords.
   - Ensure that passwords are never stored in plaintext.

3. **Implement Data Loss Prevention (DLP)**:
   - Implement checks to prevent sensitive data (e.g., PII) from being logged or exposed.
   - Apply masking or encryption for sensitive fields before storage or logging.

### Step 4: Implement Authorization Controls

1. **Role-Based Access Control (RBAC)**:
   - Implement RBAC in the application to control access to different resources based on user roles.
   - Define roles and permissions clearly, and enforce them across the application.

2. **Apply Least Privilege Principle**:
   - Ensure that users and services have only the minimum privileges necessary to perform their tasks.
   - Regularly review and audit permissions to maintain this principle.

### Step 5: Set Up Pre-Commit Hooks

1. **Install Pre-Commit**:
   - If not already installed, install `pre-commit`:
     ```bash
     pip install pre-commit
     ```

2. **Create the `.pre-commit-config.yaml` file**:
   - This file is already provided in the directory. It contains hooks to run `bandit` and check for security issues before commits.

3. **Install the pre-commit hooks**:
   - Run the following command to set up the pre-commit hooks:
     ```bash
     pre-commit install
     ```

4. **Run the pre-commit hooks manually** to check all files:
   ```bash
   pre-commit run --all-files
   ```

### Step 6: Perform Security Analysis

1. **Run Bandit**:
   - Use `bandit` to scan the code for security vulnerabilities:
     ```bash
     bandit -r .
     ```
   - Review and fix any issues that are reported by `bandit`.

2. **Commit Your Changes**:
   - After ensuring that all security checks pass, commit your changes:
     ```bash
     git add .
     git commit -m "Implement advanced secure coding practices"
     git push
     ```

## Conclusion
By completing this exercise, you have enhanced a web application by implementing secure authentication, data protection, and authorization mechanisms. You have also set up pre-commit hooks to enforce security practices automatically before code is committed. These are key practices in DevSecOps, ensuring that security is built into every stage of the development process.
