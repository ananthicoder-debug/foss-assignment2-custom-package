"""
Demonstration script showing how to use the foss_fincalc package programmatically.
"""
from foss_fincalc import (
    calculate_emi,
    calculate_total_payment,
    calculate_total_interest,
    generate_amortization_schedule,
    evaluate_loan_eligibility
)

def run_demo():
    print("=" * 60)
    print("   FOSS-FinCalc: Open Source Package Demonstration")
    print("=" * 60)
    
    # Example 1: Calculate EMI
    principal = 250000.0  # Rs. 2,50,000
    rate = 8.75           # 8.75% per annum
    tenure = 36           # 36 months
    
    emi = calculate_emi(principal, rate, tenure)
    total_interest = calculate_total_interest(principal, rate, tenure)
    total_payment = calculate_total_payment(principal, rate, tenure)
    
    print("\n[1] EMI Calculation:")
    print(f"    - Principal       : Rs. {principal:,.2f}")
    print(f"    - Rate of Interest: {rate}% p.a.")
    print(f"    - Tenure          : {tenure} months")
    print(f"    -> Monthly EMI    : Rs. {emi:,.2f}")
    print(f"    -> Total Interest : Rs. {total_interest:,.2f}")
    print(f"    -> Total Repayment: Rs. {total_payment:,.2f}")
    
    # Example 2: Amortization Schedule
    print("\n[2] Amortization Schedule (First 3 Months):")
    schedule = generate_amortization_schedule(principal, rate, tenure)
    for row in schedule[:3]:
        print(f"    Month {row['month']}: EMI=Rs.{row['emi']} | Principal=Rs.{row['principal_paid']} | Interest=Rs.{row['interest_paid']} | Balance=Rs.{row['remaining_balance']}")

    # Example 3: Eligibility Assessment
    print("\n[3] Eligibility Assessment:")
    elig = evaluate_loan_eligibility(
        monthly_income=55000,
        existing_obligations=7000,
        requested_loan_amount=250000,
        annual_rate=8.75,
        tenure_months=36
    )
    print(f"    - Status: {elig['status']}")
    print(f"    - Debt-to-Income (DTI): {elig['dti_ratio_percentage']}%")
    print(f"    - Recommendation: {elig['recommendation']}")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()
