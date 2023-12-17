# Author: Vitor Hugo Santos de Freitas

# Constants for PVC pipe
PVC_SCHED80_INNER_DIAMETER = 0.28687  # meters
PVC_SCHED80_FRICTION_FACTOR = 0.013  # dimensionless
SUPPLY_VELOCITY = 1.65  # meters per second

# Constants for HDPE pipe
HDPE_SDR11_INNER_DIAMETER = 0.048692  # meters
HDPE_SDR11_FRICTION_FACTOR = 0.018  # dimensionless
HOUSEHOLD_VELOCITY = 1.75  # meters per second

# Constant
WATER_DENSITY = 998.2  # kg/m^3

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate water pressure loss due to pipe fittings.

    Parameters:
    fluid_velocity (float): Velocity of water in meters/second.
    quantity_fittings (int): Number of fittings in the pipeline.

    Returns:
    float: Pressure loss in kilopascals (kPa).
    """
    P = (-0.04 * WATER_DENSITY * fluid_velocity**2 * quantity_fittings) / 2000
    return P

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, smaller_diameter):
    """
    Calculate water pressure loss due to a change in pipe diameter.

    Parameters:
    larger_diameter (float): Diameter of the larger pipe in meters.
    fluid_velocity (float): Velocity of water in meters/second.
    smaller_diameter (float): Diameter of the smaller pipe in meters.

    Returns:
    float: Pressure loss in kilopascals (kPa).
    """
    k = 0.1 + (50 / reynolds_number(fluid_velocity, smaller_diameter)) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    P = (-k * WATER_DENSITY * fluid_velocity**2) / 2000
    return P

def reynolds_number(velocity, diameter):
    """
    Calculate the Reynolds number for a fluid flow.

    Parameters:
    velocity (float): Velocity of water in meters/second.
    diameter (float): Diameter of the pipe or flow area in meters.

    Returns:
    float: Reynolds number (dimensionless).
    """
    return (WATER_DENSITY * velocity * diameter) / 0.001  # Using dynamic viscosity for water in N·s/m^2

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    # Calculate water_height and pressure based on your functions.
    water_height = tower_height + tank_height
    reynolds_num = reynolds_number(SUPPLY_VELOCITY, PVC_SCHED80_INNER_DIAMETER)
    
    pressure_loss1 = pressure_loss_from_fittings(SUPPLY_VELOCITY, quantity_angles)
    pressure_loss2 = pressure_loss_from_pipe_reduction(PVC_SCHED80_INNER_DIAMETER, SUPPLY_VELOCITY, HDPE_SDR11_INNER_DIAMETER)

    pressure = (water_height * WATER_DENSITY * 9.81) + pressure_loss1 + pressure_loss2

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()
