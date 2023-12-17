import tkinter as tk
from tkinter import ttk
import math

class PhysicsCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Physics Calculator")

        # Entry widgets for user input
        self.initial_velocity_label = self.create_label("Initial Velocity:")
        self.initial_velocity_entry = self.create_entry()

        self.final_velocity_label = self.create_label("Final Velocity:")
        self.final_velocity_entry = self.create_entry()

        self.time_label = self.create_label("Time:")
        self.time_entry = self.create_entry()

        # Button to trigger calculations
        self.calculate_button = ttk.Button(master, text="Calculate", command=self.perform_calculations)
        self.calculate_button.pack(pady=10)

        # Label to display results
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def create_label(self, text):
        label = ttk.Label(self.master, text=text)
        label.pack()
        return label

    def create_entry(self):
        entry = ttk.Entry(self.master)
        entry.pack()
        return entry

    def calculate_velocity(self):
        try:
            initial_velocity = float(self.initial_velocity_entry.get())
            final_velocity = float(self.final_velocity_entry.get())
            time = float(self.time_entry.get())

            velocity = initial_velocity + (final_velocity - initial_velocity) / time
            return velocity
        except ValueError:
            return None

    def calculate_acceleration(self):
        try:
            initial_velocity = float(self.initial_velocity_entry.get())
            final_velocity = float(self.final_velocity_entry.get())
            time = float(self.time_entry.get())

            acceleration = (final_velocity - initial_velocity) / time
            return acceleration
        except ValueError:
            return None

    def calculate_distance(self):
        try:
            initial_velocity = float(self.initial_velocity_entry.get())
            time = float(self.time_entry.get())
            acceleration = self.calculate_acceleration()

            distance = initial_velocity * time + 0.5 * acceleration * time**2
            return distance
        except ValueError:
            return None

    def perform_calculations(self):
        velocity = self.calculate_velocity()
        acceleration = self.calculate_acceleration()
        distance = self.calculate_distance()

        if velocity is not None and acceleration is not None and distance is not None:
            result_text = f"Velocity: {velocity:.4f}\nAcceleration: {acceleration:.4f}\nDistance: {distance:.4f}"
            self.result_label.config(text=result_text)
        else:
            self.result_label.config(text="Invalid input. Please enter valid numerical values.")

def main():
    root = tk.Tk()
    app = PhysicsCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function
    main()
