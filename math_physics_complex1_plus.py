import tkinter as tk
from tkinter import ttk
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

class PhysicsCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Physics Calculator")

        # Entry widgets for user input
        self.mass_entry = self.create_entry("Mass (kg):")
        self.initial_velocity_entry = self.create_entry("Initial Velocity (m/s):")
        self.final_velocity_entry = self.create_entry("Final Velocity (m/s):")
        self.time_entry = self.create_entry("Time (s):")

        # Button to trigger calculations
        self.calculate_button = ttk.Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack(pady=10)

        # Label to display results
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def create_entry(self, label_text):
        label = ttk.Label(self.master, text=label_text)
        label.pack()
        entry = ttk.Entry(self.master)
        entry.pack()
        return entry

    def calculate(self):
        try:
            mass = float(self.mass_entry.get())
            initial_velocity = float(self.initial_velocity_entry.get())
            final_velocity = float(self.final_velocity_entry.get())
            time = float(self.time_entry.get())

            acceleration = calculate_acceleration(initial_velocity, final_velocity, time)
            distance = calculate_distance(initial_velocity, time, acceleration)
            velocity = calculate_velocity(initial_velocity, acceleration, time)
            force = calculate_force(mass, acceleration)
            kinetic_energy = calculate_kinetic_energy(mass, velocity)

            result_text = (
                f"Acceleration: {acceleration} m/s^2\n"
                f"Distance: {distance} meters\n"
                f"Velocity: {velocity} m/s\n"
                f"Force: {force} N\n"
                f"Kinetic Energy: {kinetic_energy} J"
            )

            self.result_label.config(text=result_text)

            # Save calculations to the database
            save_calculation("Acceleration", acceleration)
            save_calculation("Distance", distance)
            save_calculation("Velocity", velocity)
            save_calculation("Force", force)
            save_calculation("Kinetic Energy", kinetic_energy)

            print("Calculations saved to the database.")

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numerical values.")

def main():
    root = tk.Tk()
    app = PhysicsCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function
    main()

    # Close the database connection
    conn.close()
