import tkinter as tk
from tkinter import ttk
import math

class RadiationCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Radiation Calculator")

        # Entry widgets for user input
        self.activity_label = self.create_label("Radioactive Activity (Bq):")
        self.activity_entry = self.create_entry()

        self.distance_label = self.create_label("Distance from Source (m):")
        self.distance_entry = self.create_entry()

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
            # Get user input for activity and distance
            activity = float(self.activity_entry.get())
            distance = float(self.distance_entry.get())

            # Calculate dose rate using the inverse square law
            dose_rate = activity / (4 * math.pi * distance**2)

            # Display the calculated dose rate
            result_text = f"Dose Rate: {dose_rate:.4e} Gy/s"

            # Display results
            self.result_label.config(text=result_text)

        except ValueError:
            self.result_label.config(text="Invalid input. Please enter valid numerical values.")

def main():
    root = tk.Tk()
    app = RadiationCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function
    main()
