import unittest
from foss_fincalc.eligibility import evaluate_loan_eligibility

class TestEligibility(unittest.TestCase):

    def test_eligible_applicant(self):
        # Income: 80,000, Existing Debt: 5,000, Loan: 300,000 @ 9% for 60 months
        res = evaluate_loan_eligibility(
            monthly_income=80000,
            existing_obligations=5000,
            requested_loan_amount=300000,
            annual_rate=9.0,
            tenure_months=60
        )
        self.assertTrue(res["is_eligible"])
        self.assertEqual(res["status"], "APPROVED")
        self.assertLessEqual(res["dti_ratio_percentage"], 50.0)

    def test_ineligible_applicant(self):
        # Income: 20,000, Existing Debt: 8,000, Loan: 1,000,000 @ 12% for 36 months (high EMI)
        res = evaluate_loan_eligibility(
            monthly_income=20000,
            existing_obligations=8000,
            requested_loan_amount=1000000,
            annual_rate=12.0,
            tenure_months=36
        )
        self.assertFalse(res["is_eligible"])
        self.assertEqual(res["status"], "REJECTED")

if __name__ == "__main__":
    unittest.main()
