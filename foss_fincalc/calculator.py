"""
Core financial calculation formulas for loan processing.
"""
from typing import Dict

def calculate_emi(principal: float, annual_rate: float, tenure_months: int) -> float:
    """
    Calculate Equated Monthly Installment (EMI) using reducing balance method.
    Formula: EMI = [P x R x (1+R)^N] / [(1+R)^N - 1]
    where:
      P = Principal loan amount
      R = Monthly interest rate (annual_rate / 12 / 100)
      N = Loan tenure in months
    """
    if principal <= 0:
        raise ValueError("Principal must be greater than zero.")
    if tenure_months <= 0:
        raise ValueError("Tenure must be at least 1 month.")
    
    if annual_rate == 0:
        return round(principal / tenure_months, 2)
    
    monthly_rate = (annual_rate / 100.0) / 12.0
    factor = (1.0 + monthly_rate) ** tenure_months
    emi = (principal * monthly_rate * factor) / (factor - 1.0)
    return round(emi, 2)


def calculate_total_payment(principal: float, annual_rate: float, tenure_months: int) -> float:
    """Calculate total amount paid over the entire loan tenure."""
    emi = calculate_emi(principal, annual_rate, tenure_months)
    return round(emi * tenure_months, 2)


def calculate_total_interest(principal: float, annual_rate: float, tenure_months: int) -> float:
    """Calculate total interest paid over the entire loan tenure."""
    total_payment = calculate_total_payment(principal, annual_rate, tenure_months)
    return round(total_payment - principal, 2)


def calculate_prepayment_savings(
    principal: float,
    annual_rate: float,
    tenure_months: int,
    extra_monthly_payment: float
) -> Dict[str, float]:
    """
    Calculate savings and tenure reduction when paying extra EMI every month.
    Added in v1.1.0 (Assignment 2 checkout & modification workflow).
    """
    if extra_monthly_payment < 0:
        raise ValueError("Extra monthly payment cannot be negative.")
        
    regular_emi = calculate_emi(principal, annual_rate, tenure_months)
    regular_total_interest = calculate_total_interest(principal, annual_rate, tenure_months)
    
    if extra_monthly_payment == 0:
        return {
            "regular_tenure_months": tenure_months,
            "new_tenure_months": tenure_months,
            "months_saved": 0,
            "regular_total_interest": regular_total_interest,
            "new_total_interest": regular_total_interest,
            "interest_saved": 0.0,
            "effective_monthly_payment": regular_emi
        }
        
    monthly_rate = (annual_rate / 100.0) / 12.0
    balance = float(principal)
    total_accelerated_interest = 0.0
    new_months = 0
    effective_payment = regular_emi + extra_monthly_payment
    
    while balance > 0 and new_months < tenure_months * 2:
        new_months += 1
        interest_charge = balance * monthly_rate
        total_accelerated_interest += interest_charge
        principal_repaid = effective_payment - interest_charge
        
        if principal_repaid >= balance:
            balance = 0.0
            break
        else:
            balance -= principal_repaid
            
    interest_saved = max(0.0, regular_total_interest - total_accelerated_interest)
    months_saved = max(0, tenure_months - new_months)
    
    return {
        "regular_tenure_months": tenure_months,
        "new_tenure_months": new_months,
        "months_saved": months_saved,
        "regular_total_interest": round(regular_total_interest, 2),
        "new_total_interest": round(total_accelerated_interest, 2),
        "interest_saved": round(interest_saved, 2),
        "effective_monthly_payment": round(effective_payment, 2)
    }
