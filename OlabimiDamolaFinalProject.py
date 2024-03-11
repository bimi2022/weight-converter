import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class MainWindow:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title("Main Window")

        # Create a frame within the root window
        self.main_frame = ttk.Frame(self.root, padding=20)
        self.main_frame.grid(row=0, column=0)

        # Create GUI widgets
        self.create_widgets()

    def create_widgets(self):
        # Welcome message label
        self.label1 = ttk.Label(self.main_frame, text="Welcome to the Main Window")
        self.label1.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Entry widget for weight input
        self.weight_label = ttk.Label(self.main_frame, text="Enter Weight:")
        self.weight_label.grid(row=1, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(self.main_frame)
        self.weight_entry.grid(row=1, column=1, padx=10, pady=10)

        # Dropdowns for unit selection
        self.from_label = ttk.Label(self.main_frame, text="From:")
        self.from_label.grid(row=2, column=0, padx=10, pady=10)
        self.from_unit = ttk.Combobox(self.main_frame, values=["Grams", "Kilograms", "Pounds", "Ounces"])
        self.from_unit.grid(row=2, column=1, padx=10, pady=10)
        self.from_unit.current(0)

        self.to_label = ttk.Label(self.main_frame, text="To:")
        self.to_label.grid(row=3, column=0, padx=10, pady=10)
        self.to_unit = ttk.Combobox(self.main_frame, values=["Grams", "Kilograms", "Pounds", "Ounces"])
        self.to_unit.grid(row=3, column=1, padx=10, pady=10)
        self.to_unit.current(1)

        # Button to trigger the conversion
        self.convert_button = ttk.Button(self.main_frame, text="Convert", command=self.convert_weight)
        self.convert_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Label to display the result of the conversion
        self.result_label = ttk.Label(self.main_frame, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Button to exit the application
        self.exit_button = ttk.Button(self.main_frame, text="Exit", command=self.exit_application)
        self.exit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def convert_weight(self):
        # Convert weight based on selected units
        try:
            weight = float(self.weight_entry.get())
            from_unit = self.from_unit.get()
            to_unit = self.to_unit.get()

            if weight <= 0:
                messagebox.showerror("Error", "Weight must be a positive number.")
                return

            if from_unit == "Grams" and to_unit == "Kilograms":
                result = weight / 1000
            elif from_unit == "Kilograms" and to_unit == "Grams":
                result = weight * 1000
            elif from_unit == "Pounds" and to_unit == "Kilograms":
                result = weight * 0.453592
            elif from_unit == "Kilograms" and to_unit == "Pounds":
                result = weight * 2.20462
            elif from_unit == "Ounces" and to_unit == "Grams":
                result = weight * 28.3495
            elif from_unit == "Grams" and to_unit == "Ounces":
                result = weight * 0.035274
            else:
                result = weight

            # Display the result
            self.result_label.config(text=f"Result: {result:.2f} {to_unit}")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

    def exit_application(self):
        # Prompt the user before quitting the application
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

def main():
    # Create the main Tkinter window
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
