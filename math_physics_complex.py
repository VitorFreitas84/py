import sqlite3
import math

# Connect to SQLite database
conn = sqlite3.connect('physics_calculations.db')
cursor = conn.cursor()

# Create a table to store calculations
cursor.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        calculation_type TEXT,
        result REAL
    )
''')
conn.commit()

def calculate_velocity(initial_velocity, acceleration, time):
    final_velocity = initial_velocity + acceleration * time
    return final_velocity

def calculate_acceleration(initial_velocity, final_velocity, time):
    acceleration = (final_velocity - initial_velocity) / time
    return acceleration

def calculate_distance(initial_velocity, time, acceleration):
    distance = initial_velocity * time + 0.5 * acceleration * time**2
    return distance

def calculate_force(mass, acceleration):
    force = mass * acceleration
    return force

def calculate_kinetic_energy(mass, velocity):
    kinetic_energy = 0.5 * mass * velocity**2
    return kinetic_energy

def save_calculation(calculation_type, result):
    """Save calculation results to the database"""
    cursor.execute('''
        INSERT INTO calculations (calculation_type, result)
        VALUES (?, ?)
    ''', (calculation_type, result))
    conn.commit()

def get_calculations():
    """Retrieve all calculations from the database"""
    cursor.execute('SELECT * FROM calculations')
    return cursor.fetchall()

# Test functions
def test_save_calculation():
    save_calculation("Velocity", 15)
    save_calculation("Distance", 30)
    assert get_calculations() == [(1, "Velocity", 15), (2, "Distance", 30)]

def main():
    mass = float(input("Enter mass (kg): "))
    initial_velocity = float(input("Enter initial velocity (m/s): "))
    final_velocity = float(input("Enter final velocity (m/s): "))
    time = float(input("Enter time (s): "))

    acceleration = calculate_acceleration(initial_velocity, final_velocity, time)
    distance = calculate_distance(initial_velocity, time, acceleration)
    velocity = calculate_velocity(initial_velocity, acceleration, time)
    force = calculate_force(mass, acceleration)
    kinetic_energy = calculate_kinetic_energy(mass, velocity)

    print(f"Acceleration: {acceleration} m/s^2")
    print(f"Distance: {distance} meters")
    print(f"Velocity: {velocity} m/s")
    print(f"Force: {force} N")
    print(f"Kinetic Energy: {kinetic_energy} J")

    # Save calculations to the database
    save_calculation("Acceleration", acceleration)
    save_calculation("Distance", distance)
    save_calculation("Velocity", velocity)
    save_calculation("Force", force)
    save_calculation("Kinetic Energy", kinetic_energy)

    print("Calculations saved to the database.")

if __name__ == "__main__":
    # Run the main function
    main()

    # Close the database connection
    conn.close()
