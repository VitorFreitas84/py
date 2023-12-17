import tkinter as tk
from tkinter import ttk
import math

class RadiationCalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Radiation Dose Calculator")

        # Entry widgets for user input
        self.activity_label = self.create_label("Radioactive Activity:")
        self.activity_entry = self.create_entry()

        # Button to toggle between Bq and Curie
        self.unit_button = ttk.Button(master, text="Toggle Unit", command=self.toggle_unit)
        self.unit_button.pack(pady=5)

        # Default unit (Bq)
        self.unit = "Bq"
        self.update_activity_label()

        self.distance_label = self.create_label("Distance from Source (m):")
        self.distance_entry = self.create_entry()

        # Dropdown menu for selecting radiation type
        self.radiation_type_label = self.create_label("Select Radiation Type:")
        self.radiation_types = ["Alpha", "Beta", "Gamma", "Neutron", "Proton", "Muon", "X-ray", "Electron"]
        self.radiation_type_var = tk.StringVar()
        self.radiation_type_var.set(self.radiation_types[0])  # Default to Alpha
        self.radiation_type_menu = ttk.Combobox(master, values=self.radiation_types, textvariable=self.radiation_type_var)
        self.radiation_type_menu.pack()

        # Button to trigger calculations
        self.calculate_button = ttk.Button(master, text="Calculate Dose", command=self.calculate_dose)
        self.calculate_button.pack(pady=10)

        # Labels to display results
        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

        # CNEN annual dose limits
        self.cnen_limits = {
            "Whole Body": {"Occupationally exposed individual": 20, "Member of the public": 1},
            "Crystalline": 20,
            "Skin": {"Occupationally exposed individual": 500, "Member of the public": 50},
            "Hands and feet": {"Occupationally exposed individual": 500}
        }

        # Valores padrão para número de radionuclídeos e grupos etários
        self.num_radionuclides = 10
        self.num_age_groups = 5

    def create_label(self, text):
        label = ttk.Label(self.master, text=text)
        label.pack()
        return label

    def create_entry(self):
        entry = ttk.Entry(self.master)
        entry.pack()
        return entry

    def toggle_unit(self):
        # Toggle between Bq and Curie
        if self.unit == "Bq":
            self.unit = "Curie"
        else:
            self.unit = "Bq"
        self.update_activity_label()

    def update_activity_label(self):
        # Update the label to show the current unit
        unit_label = "mSv" if self.unit == "Bq" else "mSv/MBq"
        self.activity_label.config(text=f"Radioactive Activity ({self.unit}): ({unit_label})")

    def calculate_dose(self):
        try:
            # Get user input for activity, distance, and radiation type
            activity = float(self.activity_entry.get())
            distance = float(self.distance_entry.get())
            radiation_type = self.radiation_type_var.get()

            # Convert activity to Bq for calculations
            if self.unit == "Curie":
                activity = self.curie_to_bq(activity)

            # Calculate dose rate based on radiation type
            dose_rate = self.calculate_dose_rate(activity, distance, radiation_type)

            # Calculate equivalent dose (mSv)
            equivalent_dose = dose_rate * self.get_qf(radiation_type)

            # Calculate acquired dose (mSv)
            acquired_dose = equivalent_dose * self.get_time_factor()

            # Calculate effective dose (mSv) using the provided formula
            effective_dose = self.calculate_effective_dose(dose_rate, equivalent_dose, acquired_dose)

            # Check compliance with CNEN annual dose limits
            compliance_info = self.check_cnen_limits(equivalent_dose)

            # Display the calculated doses, compliance information, and color the result label
            result_text = f"Dose Rate ({radiation_type}): {dose_rate:.4e} Gy/s\n" \
                          f"Equivalent Dose: {equivalent_dose:.4e} mSv\n" \
                          f"Acquired Dose: {acquired_dose:.4e} mSv\n" \
                          f"Effective Dose: {effective_dose:.4e} mSv\n\n" \
                          f"Regulatory Compliance: {compliance_info}"

            if "Exceeds" in compliance_info:
                self.result_label.config(text=result_text, fg="red")
            else:
                self.result_label.config(text=result_text, fg="black")

        except ValueError as e:
            self.result_label.config(text=f"Error: {str(e)}", fg="red")

    def calculate_effective_dose(self, dose_rate, equivalent_dose, acquired_dose):
        # Placeholder values for demonstration purposes, replace with actual values
        Hp_10 = 0.1  # Example value for Hp(10) in Gy
        e_ingroup = 0.01  # Example value for e(g)j,ing
        e_inagroup = 0.02  # Example value for e(g)j,ina
        I_ing = 10  # Example value for Ij,ing in Bq or MBq
        I_ina = 5  # Example value for Ij,ina in Bq or MBq

        # Calculate the sum over all radionuclides and age groups for ingestion
        sum_ingroup = 0
        for j in range(self.num_radionuclides):
            for g in range(self.num_age_groups):
                sum_ingroup += e_ingroup * I_ing

        # Calculate the sum over all radionuclides and age groups for inhalation
        sum_inagroup = 0
        for j in range(self.num_radionuclides):
            for g in range(self.num_age_groups):
                sum_inagroup += e_inagroup * I_ina

        # Calculate the effective dose using the provided formula
        effective_dose = Hp_10 + sum_ingroup + sum_inagroup

        return effective_dose

    def calculate_dose_rate(self, activity, distance, radiation_type):
        # Calculate dose rate based on radiation type
        return activity / (4 * math.pi * distance**2)

    def get_qf(self, radiation_type):
        # Get quality factor based on radiation type
        qf_values = {
            "Alpha": 20,
            "Beta": 1,
            "Gamma": 1,
            "Neutron": 10,  # Example value, you can change it based on your requirements
            "Proton": 5,    # Example value, you can change it based on your requirements
            "Muon": 2,      # Example value, you can change it based on your requirements
            "X-ray": 1,     # Example value, you can change it based on your requirements
            "Electron": 1   # Example value, you can change it based on your requirements
        }
        return qf_values.get(radiation_type, 1)  # Default to 1 if radiation type not found

    def get_time_factor(self):
        # Get time factor, you can modify this based on your requirements
        return 1

    def curie_to_bq(self, curie):
        # Conversion from Curie to Becquerels
        return curie * 3.7e10

    def check_cnen_limits(self, equivalent_dose):
        # Check compliance with CNEN annual dose limits
        compliance_info = "Compliant with CNEN Limits"

        for organ, limits in self.cnen_limits.items():
            if isinstance(limits, dict):
                for population, limit in limits.items():
                    if equivalent_dose > limit:
                        compliance_info = f"Exceeds CNEN {organ} limit for {population}"
                        break
            else:
                if equivalent_dose > limits:
                    compliance_info = f"Exceeds CNEN {organ} limit"
                    break

        return compliance_info

def main():
    root = tk.Tk()
    app = RadiationCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Run the main function
    main()
