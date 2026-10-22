"""
Core financial calculation formulas for loan processing.
"""

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
