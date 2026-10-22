import unittest
from foss_fincalc.calculator import (
    calculate_emi,
    calculate_total_payment,
    calculate_total_interest
)

class TestCalculator(unittest.TestCase):

    def test_emi_zero_interest(self):
        # 12,000 principal, 0% rate, 12 months = 1,000 per month
        emi = calculate_emi(12000, 0, 12)
        self.assertEqual(emi, 1000.0)

    def test_emi_standard_loan(self):
        # 100,000 principal, 10% annual rate, 12 months -> EMI is approx 8,791.59
        emi = calculate_emi(100000, 10, 12)
        self.assertAlmostEqual(emi, 8791.59, places=2)

    def test_total_payment_and_interest(self):
        principal = 100000
        rate = 10
        tenure = 12
        emi = calculate_emi(principal, rate, tenure)
        total_payment = calculate_total_payment(principal, rate, tenure)
        total_interest = calculate_total_interest(principal, rate, tenure)
        
        self.assertAlmostEqual(total_payment, emi * 12, places=2)
        self.assertAlmostEqual(total_interest, total_payment - principal, places=2)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            calculate_emi(-50000, 10, 12)
        with self.assertRaises(ValueError):
            calculate_emi(50000, 10, 0)

if __name__ == "__main__":
    unittest.main()
