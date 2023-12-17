"""
Author: Vitor Hugo Santos de Freitas

02 Prove: Calling Functions
"""

from datetime import datetime


name = input("Please enter your full name: ")

print(f"Hello {name}")

manufecture = input("Please enter you car manufacture: ")

model = input("Please enter your car model: ")

# Function to calculate the tire volume
def calculate_tire_volume(width, aspect_ratio, diameter):
    pi = 3.14159265359
    radius = (width * aspect_ratio * 0.01 + diameter * 25.4) / 2.0
    volume = (pi * width**2 * aspect_ratio * (width * aspect_ratio + (2540 * diameter))) / 10000000000
    return volume

# Get user inputs
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# Calculate the tire volume
tire_volume = calculate_tire_volume(width, aspect_ratio, diameter) 

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Display the approximate volume
print(f"The approximate volume is {tire_volume:.2f} liters")

# Append data to the volumes.txt file
with open("volumes.txt", "a") as file:
   file.write(f"{name}, {manufecture}, {model}, {current_date}, {width}, {aspect_ratio}, {diameter}, {tire_volume:.2f}\n")

   # Close the fil# test_water_flow.py

import water_flow
import pytest

# Test pressure_loss_from_fittings function
def test_pressure_loss_from_fittings():
    # Test cases with various input values
    assert pytest.approx(water_flow.pressure_loss_from_fittings(1.65, 3), abs=0.001) == -0.198
    assert pytest.approx(water_flow.pressure_loss_from_fittings(1.75, 2), abs=0.001) == -0.122
    # Add more test cases as needed

# Test reynolds_number function
def test_reynolds_number():
    # Test cases with various input values
    assert pytest.approx(water_flow.reynolds_number(0.048692, 1.65), abs=1) == 80069
    assert pytest.approx(water_flow.reynolds_number(0.28687, 1.75), abs=1) == 500318
    # Add more test cases as needed

# Test pressure_loss_from_pipe_reduction function
def test_pressure_loss_from_pipe_reduction():
    # Test case 1
    loss1 = water_flow.pressure_loss_from_pipe_reduction(0.28687, 0, 1, 0.048692)
    assert pytest.approx(loss1, abs=0.001) == 0.0  # Expected pressure loss is 0.0 kPa

    # Test case 2
    loss2 = water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692)
    assert pytest.approx(loss2, abs=0.001) == -163.744  # Expected pressure loss is -163.744 kPa

    # Test case 3
    loss3 = water_flow.pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692)
    assert pytest.approx(loss3, abs=0.001) == -184.182  # Expected pressure loss is -184.182 kPa

# Run the tests
if __name__ == "__main__":
    pytest.main()
e