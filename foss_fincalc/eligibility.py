"""
Loan applicant eligibility and Debt-To-Income (DTI) assessment.
"""
from typing import Dict
from .calculator import calculate_emi

def evaluate_loan_eligibility(
    monthly_income: float,
    existing_obligations: float,
    requested_loan_amount: float,
    annual_rate: float,
    tenure_months: int,
    max_dti_ratio: float = 0.50
) -> Dict:
    """
    Evaluates whether an applicant qualifies for a loan based on Debt-to-Income (DTI).
    Returns decision, proposed EMI, calculated DTI, max permissible EMI, and maximum loan capacity.
    """
    if monthly_income <= 0:
        raise ValueError("Monthly income must be greater than zero.")
    
    proposed_emi = calculate_emi(requested_loan_amount, annual_rate, tenure_months)
    total_monthly_debt = existing_obligations + proposed_emi
    dti = round(total_monthly_debt / monthly_income, 4)
    
    max_allowed_emi = max(0.0, (monthly_income * max_dti_ratio) - existing_obligations)
    
    # Calculate max possible loan with max_allowed_emi
    monthly_rate = (annual_rate / 100.0) / 12.0
    if monthly_rate > 0:
        factor = (1.0 + monthly_rate) ** tenure_months
        max_loan_capacity = round((max_allowed_emi * (factor - 1.0)) / (monthly_rate * factor), 2)
    else:
        max_loan_capacity = round(max_allowed_emi * tenure_months, 2)
        
    is_eligible = (dti <= max_dti_ratio) and (proposed_emi <= max_allowed_emi)
    
    status = "APPROVED" if is_eligible else "REJECTED"
    reason = (
        "Applicant satisfies debt-to-income threshold." 
        if is_eligible else 
        f"DTI ratio ({dti*100:.1f}%) exceeds maximum limit ({max_dti_ratio*100:.1f}%)."
    )
    
    return {
        "status": status,
        "is_eligible": is_eligible,
        "requested_loan": requested_loan_amount,
        "proposed_emi": proposed_emi,
        "dti_ratio_percentage": round(dti * 100, 2),
        "max_allowed_dti_percentage": round(max_dti_ratio * 100, 2),
        "max_permissible_emi": round(max_allowed_emi, 2),
        "max_loan_capacity": max(0.0, max_loan_capacity),
        "recommendation": reason
    }
