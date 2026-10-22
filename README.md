# FOSS-FinCalc: Open-Source Financial & Loan Analytics Package

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-GPLv3-green.svg)
![Version](https://img.shields.io/badge/Version-1.0.0-orange.svg)

**Course**: 19CSP01 – Free Open Source Software  
**Department**: Computer Science and Engineering  
**Institution**: MEPCO SCHLENK ENGINEERING COLLEGE (Autonomous), SIVAKASI  
**Assignment**: Assignment 2 (Unit III: Package Management and Source Code Management)  
**Question**: *Make a sample package of your own. Host it in GIT. Check out any file and perform changes and push it again in the GIT repository.*

---

## 📌 Project Overview
`foss-fincalc` is an open-source, modular Python package designed for financial analytics, Equated Monthly Installment (EMI) calculations, loan amortization scheduling, and applicant debt-to-income (DTI) eligibility screening.

It demonstrates key concepts from **Unit III: Package Management and Source Code Management**:
1. **Packaging**: Standardized Python distribution using `setuptools`, `pyproject.toml`, console entry-points, and wheel build systems.
2. **Git Workflow**: Creation of a Git repository, remote hosting on GitHub, file checkout, modification, and pushing updates back to the remote repository.
3. **Open Source Licensing**: Licensed under **GNU GPL v3.0**, reflecting the Copyleft philosophy studied in Unit I.

---

## 🚀 Features
- **Accurate EMI Computation**: Calculates monthly installments using reducing balance formulas.
- **Amortization Breakdown**: Month-by-month payment schedule showing interest, principal, and remaining balance.
- **Eligibility Analyzer**: Evaluates loan affordability using standard banking Debt-to-Income (DTI) ratios.
- **Command-Line Interface (CLI)**: Direct terminal interaction via `foss-fincalc` command.
- **CSV Export**: Automated export of repayment schedules.

---

## 💻 Installation

### 1. Install in Development Mode (Editable)
```bash
git clone https://github.com/ananthicoder-debug/foss-assignment2-custom-package.git
cd foss-assignment2-custom-package
pip install -e .
```

### 2. Standard Build & Installation
```bash
python setup.py sdist bdist_wheel
pip install .
```

---

## 🛠️ Command-Line Interface (CLI) Usage

### 1. Calculate Loan EMI
```bash
foss-fincalc emi -p 500000 -r 8.5 -t 60
```

### 2. Generate Amortization Schedule & Export to CSV
```bash
foss-fincalc schedule -p 200000 -r 9.0 -t 24 --csv repayment_schedule.csv
```

### 3. Check Loan Eligibility
```bash
foss-fincalc eligibility -i 65000 -o 12000 -p 400000 -r 8.5 -t 48
```

---

## 🐍 Python API Usage

```python
from foss_fincalc import calculate_emi, evaluate_loan_eligibility

# Calculate EMI
emi = calculate_emi(principal=500000, annual_rate=8.5, tenure_months=60)
print(f"Monthly EMI: Rs. {emi}")

# Check Eligibility
eligibility = evaluate_loan_eligibility(
    monthly_income=75000,
    existing_obligations=15000,
    requested_loan_amount=500000,
    annual_rate=8.5,
    tenure_months=60
)
print("Status:", eligibility["status"])
```

---

## 🧪 Running Unit Tests

```bash
python -m unittest discover tests
```

---

## 📜 Git Version Control Workflow (Assignment Requirement)
This repository demonstrates the complete Git workflow required for Assignment 2:
1. **Initialize & Host**: Local repository initialized, connected to GitHub remote (`origin`), and pushed initial commit (v1.0.0).
2. **Checkout File / Branch**: Checked out `foss_fincalc/calculator.py` and created a feature branch.
3. **Modify & Enhance**: Implemented Prepayment & Interest Savings analysis, and bumped version to v1.1.0.
4. **Push Updates**: Committed changes and pushed back to the GitHub repository.

---

## 📄 License
This project is licensed under the **GNU General Public License v3.0 (GPLv3)**.
