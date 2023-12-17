"""
Author: Vitor Hugo Santos de Freitas

01 Prove Milestone: Review Python
"""
print ('Please enter the following information:\n')

import math

# Get user input for width, aspect ratio, and wheel diameter
width_mm = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
wheel_diameter_inch = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the volume of space inside the tire
# Formula: v = π w^2 a w a + 2,540 d / 10,000,000,000
volume_liters = (math.pi * (width_mm**2) * aspect_ratio * width_mm * aspect_ratio + 2540 * wheel_diameter_inch) / 10000000000

# Display the result
print(f"The approximate volume is {volume_liters:.2f} liters")
