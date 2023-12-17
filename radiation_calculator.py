import tkinter as tk
from tkinter import ttk
import math

class RadiationCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Radiation Dose Calculator")

        # Entry widgets for user input
        self.activity_label = self.create_label("Radioactive Activity (Bq):")
        self.activity_entry = self.create_entry()

        self.distance_label = self.create_label("Distance from Source (m):")
        self.distance_entry = self.create_entry()

        # Dropdown menu for selecting radiation type
        self.radiation_type_label = self.create_label("Select Radiation Type:")
        self.radiation_types = ["Alpha", "Beta", "Gamma"]
        self.radiation_type_var = tk.StringVar()
        self.radiation_type_var.set(self.radiation_types[0])  # Default to Alpha
        self.radiation_type_menu = ttk.Combobox(master, values=self.radiation_types, textvariable=self.radiation_type_var)
        self.radiation_type_menu.pack()

        # Button to trigger calculations
        self.calculate_button = ttk.Button(master, text="Calculate Dose Rate", command=self.calculate_dose_rate)
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

    def calculate_dose_rate(self):
        try:
            # Get user input for activity, distance, and radiation type
            activity = float(self.activity_entry.get())
            distance = float(self.distance_entry.get())
            radiation_type = self.radiation_type_var.get()

            # Calculate dose rate based on radiation type
            if radiation_type == "Alpha":
                dose_rate = self.calculate_dose_rate_alpha(activity, distance)
            elif radiation_type == "Beta":
                dose_rate = self.calculate_dose_rate_beta(activity, distance)
            elif radiation_type == "Gamma":
                dose_rate = self.calculate_dose_rate_gamma(activity, distance)
            else:
                raise ValueError("Invalid radiation type selected.")

            # Display the calculated dose rate
            result_text = f"Dose Rate ({radiation_type}): {dose_rate:.4e} Gy/s"
            self.result_label.config(text=result_text)

        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}")

    def calculate_dose_rate_alpha(self, activity, distance):
        # Adjust the formula for alpha radiation
        return activity / (4 * math.pi * distance**2)

    def calculate_dose_rate_beta(self, activity, distance):
        # Adjust the formula for beta radiation
        return activity / (4 * math.pi * distance**2)

    def calculate_dose_rate_gamma(self, activity, distance):
        # Adjust the formula for gamma radiation
        return activity / (4 * math.pi * distance**2)

def main():
    root = tk.Tk()
    app = RadiationCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function
    main()
