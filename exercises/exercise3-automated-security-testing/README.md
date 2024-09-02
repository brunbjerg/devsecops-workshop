# Exercise 3: Implementing Secure Data Storage and Transmission

## Objective
In this exercise, you will focus on securing data both at rest and in transit. You will implement encryption for sensitive data stored in the database and ensure that all communications between clients and the server are encrypted. Additionally, you will secure password storage using hashing techniques.

## Prerequisites
- Basic knowledge of Python programming.
- Familiarity with encryption concepts and hashing techniques.
- Python environment with `pip` installed.

## Tools Used
- **Python Libraries**:
  - `cryptography`: For AES encryption of sensitive data.
  - `bcrypt`: For secure password hashing.
- **SSL/TLS**: For encrypting communications between the client and server.

## Repository Structure
Your repository should be structured as follows:

```plaintext
exercise3-secure-storage/
│
├── app.py
└── requirements.txt
