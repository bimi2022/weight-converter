# weight-converter
import tkinter as tk
from tkinter import ttk

# Conversion factors
GRAMS_TO_KG = 0.001
KG_TO_GRAMS = 1000
POUNDS_TO_KG = 0.453592
KG_TO_POUNDS = 2.20462
OUNCES_TO_GRAMS = 28.3495
GRAMS_TO_OUNCES = 0.035274

class WeightConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weight Converter")
        self.root.geometry("400x200")

        # Label and entry for weight input
        self.weight_label = ttk.Label(root, text="Enter Weight:")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(root)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        # Labels and dropdowns for unit selection
        self.from_label = ttk.Label(root, text="From:")
        self.from_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_unit = ttk.Combobox(root, values=["Grams", "Kilograms", "Pounds", "Ounces"])
        self.from_unit.grid(row=1, column=1, padx=10, pady=10)
        self.from_unit.current(0)

        self.to_label = ttk.Label(root, text="To:")
        self.to_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_unit = ttk.Combobox(root, values=["Grams", "Kilograms", "Pounds", "Ounces"])
        self.to_unit.grid(row=2, column=1, padx=10, pady=10)
        self.to_unit.current(1)

        # Convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_weight)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
