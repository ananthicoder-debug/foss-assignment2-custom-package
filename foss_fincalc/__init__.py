"""
FOSS-FinCalc: Open-Source Financial & Loan Analytics Package
Developed for 19CSP01 - Free Open Source Software (Assignment 2)
MEPCO SCHLENK ENGINEERING COLLEGE (Autonomous), SIVAKASI
"""

__version__ = "1.1.0"
__author__ = "ananthicoder-debug"
__license__ = "GPL-3.0"

from .calculator import (
    calculate_emi,
    calculate_total_interest,
    calculate_total_payment,
    calculate_prepayment_savings
)
from .amortization import (
    generate_amortization_schedule,
    export_schedule_csv
)
from .eligibility import (
    evaluate_loan_eligibility
)

__all__ = [
    "calculate_emi",
    "calculate_total_interest",
    "calculate_total_payment",
    "calculate_prepayment_savings",
    "generate_amortization_schedule",
    "export_schedule_csv",
    "evaluate_loan_eligibility"
]
