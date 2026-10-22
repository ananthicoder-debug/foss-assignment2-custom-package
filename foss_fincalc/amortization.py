"""
Amortization schedule generator and CSV export utilities.
"""
import csv
from typing import List, Dict
from .calculator import calculate_emi

def generate_amortization_schedule(principal: float, annual_rate: float, tenure_months: int) -> List[Dict]:
    """
    Generate month-by-month repayment schedule breakdown.
    Each row contains:
      - month: Month index (1 to N)
      - emi: Total monthly installment
      - principal_paid: Principal portion for the month
      - interest_paid: Interest portion for the month
      - remaining_balance: Outstanding principal after this installment
    """
    if principal <= 0 or tenure_months <= 0:
        raise ValueError("Principal and tenure must be positive numbers.")
    
    emi = calculate_emi(principal, annual_rate, tenure_months)
    monthly_rate = (annual_rate / 100.0) / 12.0
    
    schedule = []
    balance = float(principal)
    
    for month in range(1, tenure_months + 1):
        interest_payment = round(balance * monthly_rate, 2)
        principal_payment = round(emi - interest_payment, 2)
        
        # Handle rounding differences in final month
        if month == tenure_months or principal_payment > balance:
            principal_payment = balance
            emi = round(principal_payment + interest_payment, 2)
            balance = 0.0
        else:
            balance = round(balance - principal_payment, 2)
            
        schedule.append({
            "month": month,
            "emi": emi,
            "principal_paid": principal_payment,
            "interest_paid": interest_payment,
            "remaining_balance": max(0.0, balance)
        })
        
        if balance <= 0:
            break
            
    return schedule


def export_schedule_csv(schedule: List[Dict], filepath: str) -> str:
    """Export amortization schedule rows to a standard CSV file."""
    if not schedule:
        raise ValueError("Schedule is empty.")
    
    fieldnames = ["month", "emi", "principal_paid", "interest_paid", "remaining_balance"]
    with open(filepath, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(schedule)
        
    return filepath
