# FOSS-FinCalc: Open-Source Financial & Loan Analytics Package

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/License-GPLv3-green.svg)
![Version](https://img.shields.io/badge/Version-1.1.0-brightgreen.svg)
![Build](https://img.shields.io/badge/Tests-Passing-success.svg)

**Course**: 19CSP01 – Free Open Source Software  
**Department**: Computer Science and Engineering  
**Institution**: MEPCO SCHLENK ENGINEERING COLLEGE (Autonomous), SIVAKASI  
**Assignment**: Assignment 2 (Unit III: Package Management and Source Code Management)  
**Question**: *Make a sample package of your own. Host it in GIT. Check out any file and perform changes and push it again in the GIT repository.*

---

## 📌 Project Overview
`foss-fincalc` is an open-source, modular Python package designed for financial analytics, Equated Monthly Installment (EMI) calculations, loan amortization scheduling, applicant debt-to-income (DTI) eligibility screening, and loan prepayment savings optimization.

It demonstrates key concepts from **Unit III: Package Management and Source Code Management**:
1. **Packaging**: Standardized Python distribution using `setuptools`, `pyproject.toml`, console entry-points, and wheel build systems.
2. **Git Workflow**: Creation of a Git repository, remote hosting on GitHub, file checkout, modification, and pushing updates back to the remote repository.
3. **Open Source Licensing**: Licensed under **GNU GPL v3.0**, reflecting the Copyleft philosophy studied in Unit I.

---

## 🚀 Features
- **Accurate EMI Computation**: Calculates monthly installments using reducing balance formulas.
- **Amortization Breakdown**: Month-by-month payment schedule showing interest, principal, and remaining balance.
- **Prepayment & Savings Analysis (v1.1.0)**: Calculate loan tenure reduction and total interest saved by contributing extra monthly payments.
- **Eligibility Analyzer**: Evaluates loan affordability using standard banking Debt-to-Income (DTI) ratios.
- **Command-Line Interface (CLI)**: Direct terminal interaction via `foss-fincalc` command.
- **CSV Export**: Automated export of repayment schedules.

---

## 💻 Installation

### 1. Install in Development Mode (Editable)
```bash
git clone https://github.com/ananthicoder-debug/foss-assignment2-custom-package.git
cd foss-assignment2-custom-package
pip install --no-build-isolation -e .
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
from foss_fincalc import calculate_emi, evaluate_loan_eligibility, calculate_prepayment_savings

# 1. Calculate EMI
emi = calculate_emi(principal=500000, annual_rate=8.5, tenure_months=60)
print(f"Monthly EMI: Rs. {emi}")

# 2. Prepayment Savings Analysis (Added in v1.1.0)
savings = calculate_prepayment_savings(
    principal=500000,
    annual_rate=9.0,
    tenure_months=60,
    extra_monthly_payment=2500
)
print(f"Months Saved: {savings['months_saved']} months")
print(f"Interest Saved: Rs. {savings['interest_saved']}")

# 3. Check Eligibility
eligibility = evaluate_loan_eligibility(
    monthly_income=75000,
    existing_obligations=15000,
    requested_loan_amount=500000,
    annual_rate=8.5,
    tenure_months=60
)
print("Eligibility Decision:", eligibility["status"])
```

---

## 🧪 Running Unit Tests

```bash
python -m unittest discover tests
```

---

## 📜 Git Version Control Workflow (Assignment 2 Execution Log)
This repository directly demonstrates the step-by-step Git workflow specified in Assignment 2:

1. **Repository Creation & Hosting**:
   ```bash
   git init -b main
   git add .
   git commit -m "feat: initial release v1.0.0 of foss-fincalc package"
   git remote add origin https://github.com/ananthicoder-debug/foss-assignment2-custom-package.git
   git push -u origin main
   ```

2. **File Checkout & Branch Creation**:
   ```bash
   # Check out a branch / file for modification
   git checkout -b feature/prepayment-savings
   ```

3. **Modification & Enhancement**:
   - Added `calculate_prepayment_savings()` to `foss_fincalc/calculator.py`
   - Added corresponding unit test in `tests/test_calculator.py`
   - Bumped package version from `1.0.0` to `1.1.0` in `__init__.py`, `setup.py`, and `pyproject.toml`

4. **Commit & Push Updated Code**:
   ```bash
   git add .
   git commit -m "feat: add calculate_prepayment_savings and bump version to v1.1.0"
   git push -u origin feature/prepayment-savings
   git checkout main
   git merge feature/prepayment-savings
   git push origin main
   git tag -a v1.1.0 -m "Release v1.1.0 with Prepayment Savings feature"
   git push origin --tags
   ```

---

## 📄 License
This project is licensed under the **GNU General Public License v3.0 (GPLv3)** - Freedom to use, modify, study, and share.
