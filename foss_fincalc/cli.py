"""
Command Line Interface for FOSS-FinCalc package.
Allows running calculations directly from Linux / Windows terminal.
"""
import sys
import argparse
from . import __version__
from .calculator import calculate_emi, calculate_total_payment, calculate_total_interest
from .amortization import generate_amortization_schedule, export_schedule_csv
from .eligibility import evaluate_loan_eligibility

def main():
    parser = argparse.ArgumentParser(
        prog="foss-fincalc",
        description="FOSS-FinCalc: Open-Source Financial & Loan Analytics Tool (MEPCO CSE FOSS 19CSP01)"
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    
    subparsers = parser.add_subparsers(dest="command", help="Available sub-commands")
    
    # EMI command
    emi_parser = subparsers.add_parser("emi", help="Calculate Monthly EMI and Total Interest")
    emi_parser.add_argument("-p", "--principal", type=float, required=True, help="Loan principal amount")
    emi_parser.add_argument("-r", "--rate", type=float, required=True, help="Annual interest rate (percentage)")
    emi_parser.add_argument("-t", "--tenure", type=int, required=True, help="Tenure in months")
    
    # Amortization schedule command
    sched_parser = subparsers.add_parser("schedule", help="Generate Loan Amortization Schedule")
    sched_parser.add_argument("-p", "--principal", type=float, required=True, help="Loan principal amount")
    sched_parser.add_argument("-r", "--rate", type=float, required=True, help="Annual interest rate (percentage)")
    sched_parser.add_argument("-t", "--tenure", type=int, required=True, help="Tenure in months")
    sched_parser.add_argument("--csv", type=str, help="Optional CSV file path to export table")
    sched_parser.add_argument("--limit", type=int, default=12, help="Number of months to print on stdout (default 12)")
    
    # Eligibility command
    elig_parser = subparsers.add_parser("eligibility", help="Evaluate Applicant Loan Eligibility")
    elig_parser.add_argument("-i", "--income", type=float, required=True, help="Monthly gross income")
    elig_parser.add_argument("-o", "--obligations", type=float, default=0.0, help="Existing monthly EMI / obligations")
    elig_parser.add_argument("-p", "--principal", type=float, required=True, help="Requested loan amount")
    elig_parser.add_argument("-r", "--rate", type=float, required=True, help="Annual interest rate (percentage)")
    elig_parser.add_argument("-t", "--tenure", type=int, required=True, help="Tenure in months")
    elig_parser.add_argument("--max-dti", type=float, default=0.50, help="Max Debt-to-Income ratio (default 0.50)")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(0)
        
    if args.command == "emi":
        emi = calculate_emi(args.principal, args.rate, args.tenure)
        total_pay = calculate_total_payment(args.principal, args.rate, args.tenure)
        interest = calculate_total_interest(args.principal, args.rate, args.tenure)
        
        print("\n==============================================")
        print("          FOSS-FinCalc: EMI Summary           ")
        print("==============================================")
        print(f" Principal Loan Amount : Rs. {args.principal:,.2f}")
        print(f" Annual Interest Rate  : {args.rate:.2f}%")
        print(f" Tenure                : {args.tenure} Months ({args.tenure/12:.1f} Years)")
        print("----------------------------------------------")
        print(f" Monthly EMI           : Rs. {emi:,.2f}")
        print(f" Total Interest        : Rs. {interest:,.2f}")
        print(f" Total Payable Amount  : Rs. {total_pay:,.2f}")
        print("==============================================\n")
        
    elif args.command == "schedule":
        schedule = generate_amortization_schedule(args.principal, args.rate, args.tenure)
        print("\n=========================================================================")
        print(f" Month |    EMI (Rs)   | Principal (Rs)|  Interest (Rs) | Remaining Bal (Rs)")
        print("-------------------------------------------------------------------------")
        for row in schedule[:args.limit]:
            print(f"  {row['month']:4d} | {row['emi']:13,.2f} | {row['principal_paid']:13,.2f} | {row['interest_paid']:14,.2f} | {row['remaining_balance']:18,.2f}")
        if len(schedule) > args.limit:
            print(f"  ... [Showing first {args.limit} of {len(schedule)} months]")
        print("=========================================================================\n")
        
        if args.csv:
            export_schedule_csv(schedule, args.csv)
            print(f"[+] Amortization schedule exported to: {args.csv}\n")
            
    elif args.command == "eligibility":
        result = evaluate_loan_eligibility(
            args.income, args.obligations, args.principal, args.rate, args.tenure, args.max_dti
        )
        print("\n==============================================")
        print("      FOSS-FinCalc: Eligibility Assessment    ")
        print("==============================================")
        print(f" Decision            : {result['status']}")
        print(f" Proposed Monthly EMI: Rs. {result['proposed_emi']:,.2f}")
        print(f" Debt-to-Income (DTI): {result['dti_ratio_percentage']:.2f}% (Limit: {result['max_allowed_dti_percentage']:.2f}%)")
        print(f" Max Permissible EMI : Rs. {result['max_permissible_emi']:,.2f}")
        print(f" Max Loan Capacity   : Rs. {result['max_loan_capacity']:,.2f}")
        print(f" Remarks             : {result['recommendation']}")
        print("==============================================\n")

if __name__ == "__main__":
    main()
