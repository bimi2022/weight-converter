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

        # Create a frame for the main window
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(padx=10, pady=10)

        # Label and entry for weight input
        self.weight_label = ttk.Label(self.main_frame, text="Enter Weight:")
        self.weight_label.grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(self.main_frame)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)

        # Labels and dropdowns for unit selection
        self.from_label = ttk.Label(self.main_frame, text="From:")
        self.from_label.grid(row=1, column=0, padx=10, pady=10)
        self.from_unit = ttk.Combobox(self.main_frame, values=["Grams", "Kilograms", "Pounds", "Ounces"])
        self.from_unit.grid(row=1, column=1, padx=10, pady=10)
        self.from_unit.current(0)

        self.to_label = ttk.Label(self.main_frame, text="To:")
        self.to_label.grid(row=2, column=0, padx=10, pady=10)
        self.to_unit = ttk.Combobox(self.main_frame, values=["Grams", "Kilograms", "Pounds", "Ounces"])
        self.to_unit.grid(row=2, column=1, padx=10, pady=10)
        self.to_unit.current(1)

        # Convert button
        self.convert_button = ttk.Button(self.main_frame, text="Convert", command=self.convert_weight)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Result label
        self.result_label = ttk.Label(self.main_frame, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def convert_weight(self):
        try:
            # Get user input
            weight = float(self.weight_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            # Perform conversion based on selected units
            if from_unit == "Grams" and to_unit == "Kilograms":
                result = weight * GRAMS_TO_KG
            elif from_unit == "Kilograms" and to_unit == "Grams":
                result = weight * KG_TO_GRAMS
            elif from_unit == "Pounds" and to_unit == "Kilograms":
                result = weight * POUNDS_TO_KG
            elif from_unit == "Kilograms" and to_unit == "Pounds":
                result = weight * KG_TO_POUNDS
            elif from_unit == "Ounces" and to_unit == "Grams":
                result = weight * OUNCES_TO_GRAMS
            elif from_unit == "Grams" and to_unit == "Ounces":
                result = weight * GRAMS_TO_OUNCES
            else:
                result = weight  # No conversion needed

            # Display result
            self.result_label.config(text=f"Result: {result:.2f} {to_unit}")
        except ValueError:
            # Handle invalid input
            self.result_label.config(text="Invalid input. Please enter a number.")

def open_new_window():
    new_window = tk.Toplevel()
    new_window.title("New Window")
    label = ttk.Label(new_window, text="This is a new window!")
    label.pack(padx=10, pady=10)

def main():
    root = tk.Tk()
    app = WeightConverterApp(root)
    
    # Create a button to open a new window
    new_window_button = ttk.Button(root, text="Open New Window", command=open_new_window)
    new_window_button.pack(padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
