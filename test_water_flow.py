# test_water_flow.py

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
