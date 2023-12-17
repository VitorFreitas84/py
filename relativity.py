import tkinter as tk
from tkinter import ttk
import math

# Constants
speed_of_light = 3e8  # meters per second

class SpecialRelativityCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Special Relativity Calculator")

        # Entry widgets for user input
        self.mass_label = self.create_label("Mass (kg):")
        self.mass_entry = self.create_entry()

        self.velocity_label = self.create_label("Velocity (m/s):")
        self.velocity_entry = self.create_entry()

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

    def calculate_energy(self, mass):
        energy = mass * speed_of_light**2
        return energy

    def special_relativity(self, mass, velocity):
        gamma = 1 / math.sqrt(1 - (velocity**2 / speed_of_light**2))
        contracted_length = 1 / gamma
        return gamma, contracted_length

    def perform_calculations(self):
        try:
            mass = float(self.mass_entry.get())
            velocity = float(self.velocity_entry.get())

            energy = self.calculate_energy(mass)
            gamma, contracted_length = self.special_relativity(mass, velocity)

            result_text = f"Mass: {mass} kg\nVelocity: {velocity} m/s\n"
            result_text += f"Energy: {energy:.4e} J\nGamma: {gamma:.4f}\nContracted Length: {contracted_length:.4f} meters"
            self.result_label.config(text=result_text)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numerical values.")

def main():
    root = tk.Tk()
    app = SpecialRelativityCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function
    main()
