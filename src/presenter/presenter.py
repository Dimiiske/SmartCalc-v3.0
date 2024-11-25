import tkinter as tk
from tkinter import messagebox
import ctypes
import numpy as np
from sympy import symbols, lambdify, sympify

class CalculatorLogic:
    def __init__(self, entry, number_x, number_y, label, figure, ax, canvas):
        self.entry = entry
        self.number_x = number_x
        self.number_y = number_y
        self.label = label
        self.figure = figure
        self.ax = ax
        self.canvas = canvas

    def calculate(self, input_string):
        calc_lib = ctypes.CDLL('./model/libcalc.so')
        calc_lib.result_c.argtypes = [ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)]
        calc_lib.result_c.restype = ctypes.c_double
        error_code = ctypes.c_int()
        result = calc_lib.result_c(input_string.encode('utf-8'), ctypes.byref(error_code))
        return result, error_code.value

    def show_plot(self):
        expression = self.entry.get()
        x = symbols('x')

        try:
            value_x = int(self.number_x.get())
            value_y = int(self.number_x.get())
            if (value_x < 10 or value_x > 10) and (value_y < 10 or value_y > 10):
                pass
            else:
                value_x = value_y = 10
        except ValueError:
            self.result_label.config(text="Error.")

        try:
            expr = sympify(expression)
            func = lambdify(x, expr, 'numpy')

            x_vals = np.linspace(-value_x, value_y, 400)
            y_vals = func(x_vals)

            self.ax.clear()
            self.ax.plot(x_vals, y_vals, label=str(expr))
            self.ax.set_title(f"Graph {expression}")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.ax.axhline(0, color='black',linewidth=0.5, ls='--')
            self.ax.axvline(0, color='black',linewidth=0.5, ls='--')
            self.ax.grid()
            self.ax.legend()

            self.canvas.draw()

            self.save_expression(expression)
        except Exception as e:
            self.result_label.config(text="Error")

    def show_about(self):
        about_text = (
            "This is a calculator that does:\n"
            "Basic arithmetic operations;\n"
            "Basic trigonometric operations;\n"
            "Use the buttons to enter numbers and operations;\n"
            "To build a graph, enter an expression with 'X', select the range 'X', 'Y',\n"
            "which are located under the graph field and click the Graph button.\n"
        )
        about_window = tk.Toplevel()
        about_window.title("About")
        about_window.geometry("1400x300")
        about_window.resizable(False, False)
        about_label = tk.Label(about_window, text=about_text, justify="left")
        about_label.pack(padx=10, pady=10)

    def save_expression(self, expression):
        with open("history.txt", "a") as file:
            file.write(expression + "\n")

    def load_history(self):
        try:
            with open("history.txt", "r") as file:
                return file.readlines()
        except FileNotFoundError:
            return []

    def show_history(self):
        history = self.load_history()
        if not history:
            messagebox.showinfo("History", "Empty.")
        else:
            history_window = tk.Toplevel()
            history_window.title("History")
            history_window.geometry("500x500")
            history_window.resizable(False, False)

            history_listbox = tk.Listbox(history_window)
            history_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

            for expression in history:
                history_listbox.insert(tk.END, expression.strip())

            def add_to_expression():
                selected_expression = history_listbox.get(history_listbox.curselection())
                self.entry.insert(tk.END, selected_expression)

            def clean_history():
                with open("history.txt", 'w', encoding='utf-8') as file:
                    file.write('')  

            add_button = tk.Button(history_window, text="Add to expression", command=add_to_expression)
            add_button.pack(pady=10)

            add_button = tk.Button(history_window, text="Clean history", command=clean_history)
            add_button.pack(pady=10, padx=10)

    def button_click(self, value):
        if isinstance(value, (int, str)) and str(value).isdigit():
            current_text = self.entry.get()
            new_text = current_text + str(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
        elif value == '=':
            expression = self.entry.get()
            result, error_code = self.calculate(expression)
            if error_code == 1: 
                self.save_expression(expression)
                self.label.config(text=round(result,5))
            else:
                self.label.config(text="Error")
        elif value == 'Graph':  
            self.show_plot()
        elif value == 'About':
            self.show_about()
        elif value == 'History':
            self.show_history()
        elif value == 'AC':
            self.entry.delete(0, tk.END)
            self.label.config(text="") 
        elif value == 'C':
            current_text = self.entry.get()
            new_text = current_text[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)
            self.label.config(text="") 
        else:
            current_text = self.entry.get()
            new_text = current_text + str(value)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, new_text)