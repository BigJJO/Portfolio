import tkinter as tk
import math
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        self.total = 0
        self.entered_number = 0
        self.total_label_text = tk.StringVar()
        self.total_label_text.set(self.total)
        self.total_label = tk.Label(master, textvariable=self.total_label_text)
        self.total_label.grid(row=0, column=0, columnspan=2, sticky="w")
        self.entry = tk.Entry(master)
        self.entry.grid(row=1, column=0, columnspan=2)
        self.add_button = tk.Button(master, text="+", command=lambda: self.update("add"))
        self.add_button.grid(row=2, column=0)
        self.subtract_button = tk.Button(master, text="-", command=lambda: self.update("subtract"))
        self.subtract_button.grid(row=2, column=1)
        self.multiply_button = tk.Button(master, text="*", command=lambda: self.update("multiply"))
        self.multiply_button.grid(row=3, column=0)
        self.divide_button = tk.Button(master, text="/", command=lambda: self.update("divide"))
        self.divide_button.grid(row=3, column=1)
        self.exponent_button = tk.Button(master, text="^", command=lambda: self.update("exponent"))
        self.exponent_button.grid(row=4, column=0)
        self.square_root_button = tk.Button(master, text="√", command=lambda: self.update("square_root"))
        self.square_root_button.grid(row=4, column=1)
        self.equals_button = tk.Button(master, text="=", command=lambda: self.update("equals"))
        self.equals_button.grid(row=5, column=0)
        self.reset_button = tk.Button(master, text="C", command=lambda: self.update("reset"))
        self.reset_button.grid(row=5, column=1)
        self.previous_answer_button = tk.Button(master, text="Ans", command=lambda: self.update("previous_answer"))
        self.previous_answer_button.grid(row=6, column=0)
        self.calculate_button = tk.Button(master, text="Calculate", command=lambda: self.calculate())
        self.calculate_button.grid(row=6, column=1)
    def calculate(self):
        try:
            self.entered_number = float(self.entry.get())
        except ValueError:
            self.total_label_text.set("Error")
            self.entry.delete(0, tk.END)
            return
        if self.math_function == "add":
            self.total += self.entered_number
        elif self.math_function == "subtract":
            self.total -= self.entered_number
        elif self.math_function == "multiply":
            self.total *= self.entered_number
        elif self.math_function == "divide":
            self.total /= self.entered_number
        elif self.math_function == "exponent":
            self.total = pow(self.total, self.entered_number)
        elif self.math_function == "square_root":
            self.total = math.sqrt(self.entered_number)

        self.previous_answer = self.total
        self.total_label_text.set(self.total)
        self.entry.delete(0, tk.END)

    def update(self, math_function):
        if math_function == "reset":
            self.total = 0
            self.total_label_text.set(self.total)
            self.entry.delete(0, tk.END)
        elif math_function == "previous_answer":
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.previous_answer)
        else:
            if self.entry.get() == '':
                return
            self.math_function = math_function
            self.calculate()

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()
