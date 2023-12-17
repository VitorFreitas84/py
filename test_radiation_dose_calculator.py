import unittest
from tkinter import Tk
from Radiation_Dose_Calculator import RadiationCalculatorApp  # Replace with the actual name of your file without spaces

class TestRadiationCalculatorApp(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.app = RadiationCalculatorApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_calculate_dose(self):
        # Simulate user input
        self.app.activity_entry.insert(0, "1000")
        self.app.distance_entry.insert(0, "5")
        self.app.radiation_type_var.set("Gamma")

        # Call the method you want to test
        self.app.calculate_dose()

        # Assert the expected result based on your input
        result_text = self.app.result_label.cget("text")
        self.assertIn("Dose Rate (Gamma):", result_text)
        self.assertIn("Equivalent Dose:", result_text)
        self.assertIn("Acquired Dose:", result_text)
        self.assertIn("Effective Dose:", result_text)
        self.assertIn("Regulatory Compliance:", result_text)

    # Add more test methods as needed

if __name__ == "__main__":
    unittest.main()
