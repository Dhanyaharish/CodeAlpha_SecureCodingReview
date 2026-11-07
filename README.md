# CodeAlpha Secure Coding Review Task

##  Executive Summary
This project demonstrates a complete **Secure Coding Review and Vulnerability Remediation** workflow conducted as part of the CodeAlpha Cybersecurity Internship. The evaluation combined Automated Static Application Security Testing (SAST) using **Bandit** with manual code inspection to identify, analyze, and remediate critical security flaws in a Python application.

* **Programming Language:** Python 3.x
* **Security Tool:** Bandit (v1.9.4)
* **Scope:** Source code review of database interaction scripts and dynamic evaluation functions.

---

##  Methodology
1. **Vulnerability Identification (Days 1–2):** Developed a deliberately flawed Python script (`vulnerable_app.py`) containing classic common software security weaknesses (CWEs).
2. **Automated SAST Scan (Day 3):** Installed and executed Bandit to parse the Abstract Syntax Tree (AST) and generate an automated vulnerability report (`bandit_report.txt`).
3. **Manual Code Inspection (Days 4–5):** Line-by-line review focusing on user input boundaries, data flows, and secret management.
4. **Remediation & Verification (Days 6–7):** Refactored the code into `secure_app.py`, implementing parameterized queries, environment variable storage, and safe input handling. Re-ran Bandit to verify zero high or medium-severity issues.

---

##  Vulnerability Summary Table

| Bug ID | Vulnerability Type | Severity | Affected File / Line | Status |
| :--- | :--- | :--- | :--- | :--- |
| **VULN-01** | SQL Injection (CWE-89) | Medium | `vulnerable_app.py` (Line 22) | **Remediated** |
| **VULN-02** | Hardcoded Secret (CWE-259) | Low | `vulnerable_app.py` (Line 5) | **Remediated** |
| **VULN-03** | Insecure `eval()` Use (CWE-78) | Medium | `vulnerable_app.py` (Line 32) | **Remediated** |

---

##  Detailed Findings & Remediation

### 1. SQL Injection (`VULN-01`)
* **Vulnerable Code:**
  ```python
  query = f"SELECT * FROM users WHERE username = '{username}'"
  cursor.execute(query)
