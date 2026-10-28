import tkinter as tk
from tkinter import ttk, messagebox


# Function to perform calculations
def calculate():
    try:
        # Get input values
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        # Get selected operation
        operation = operation_box.get()

        # Perform calculation
        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            if num2 == 0:
                messagebox.showerror(
                    "Error",
                    "Cannot divide by zero!"
                )
                result_label.config(text="Result: Error")
                return

            result = num1 / num2

        else:
            messagebox.showerror(
                "Error",
                "Please select an operation."
            )
            return

        # Display result
        result_label.config(text=f"Result: {result:g}")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers in both fields."
        )
        result_label.config(text="Result: --")


# Function to clear all fields
def clear_fields():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    operation_box.set("+")
    result_label.config(text="Result: --")
    entry1.focus()


# Create main window
root = tk.Tk()
root.title("Calculator App")
root.geometry("400x430")
root.resizable(False, False)
root.configure(bg="#f0f4f8")


# Project heading
title_label = tk.Label(
    root,
    text="PYTHON CALCULATOR",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#1f3a5f"
)
title_label.pack(pady=20)


# First number
tk.Label(
    root,
    text="Enter First Number:",
    font=("Arial", 11),
    bg="#f0f4f8"
).pack()

entry1 = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center",
    width=25
)
entry1.pack(pady=8)


# Second number
tk.Label(
    root,
    text="Enter Second Number:",
    font=("Arial", 11),
    bg="#f0f4f8"
).pack()

entry2 = tk.Entry(
    root,
    font=("Arial", 12),
    justify="center",
    width=25
)
entry2.pack(pady=8)


# Operation selection
tk.Label(
    root,
    text="Select Operation:",
    font=("Arial", 11),
    bg="#f0f4f8"
).pack(pady=(8, 4))

operation_box = ttk.Combobox(
    root,
    values=["+", "-", "*", "/"],
    state="readonly",
    font=("Arial", 12),
    width=10,
    justify="center"
)
operation_box.set("+")
operation_box.pack(pady=5)


# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate",
    font=("Arial", 12, "bold"),
    bg="#2878b5",
    fg="white",
    width=15,
    command=calculate
)
calculate_button.pack(pady=12)


# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 11),
    width=15,
    command=clear_fields
)
clear_button.pack(pady=3)


# Result display
result_label = tk.Label(
    root,
    text="Result: --",
    font=("Arial", 15, "bold"),
    bg="#f0f4f8",
    fg="#16803c"
)
result_label.pack(pady=18)


# Start application
root.mainloop()