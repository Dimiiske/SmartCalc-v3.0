import tkinter as tk
from tkinter import ttk
from view.button import CalculatorButton
from presenter.presenter import CalculatorLogic
import json
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class CalculatorView:
    def __init__(self, window_width=1600, window_height=1000):
        self.master = tk.Tk()
        self.master.title("SmartCalc_v3")
        self.master.geometry(f"{window_width}x{window_height}")
        self.master.resizable(False, False)

        self.number_entry = ttk.Entry(self.master, width=35, font=("Arial", 16))
        self.number_entry.grid(row=0, column=0, columnspan=6, padx=(15,5), pady=(15, 25), sticky='ew')
        self.number_entry.config(justify='right')

        self.result_label = ttk.Label(self.master, text="", width=10, font=("Arial", 16), foreground="black", background="lightgrey")
        self.result_label.grid(row=0, column=6, columnspan=2, padx=(15,5), pady=(15, 25), sticky='e')

        self.result_label_x = ttk.Label(self.master, text="X definition=", width=10, font=("Arial", 12))
        self.result_label_x.grid(row=7, column=1, padx=(15,5), pady=5, sticky='e')
        
        self.number_x = ttk.Entry(self.master, width=5, font=("Arial", 12))
        self.number_x.grid(row=7, column=2, padx=5, pady=(15, 25), sticky='ew')
        self.number_x.insert(0, "10")

        self.result_label_y = ttk.Label(self.master, text="Y definition=", width=10, font=("Arial", 12))
        self.result_label_y.grid(row=7, column=5, padx=(15,5), pady=5, sticky='e')
        
        self.number_y = ttk.Entry(self.master, width=5, font=("Arial", 12))
        self.number_y.grid(row=7, column=6, padx=5, pady=(15, 25), sticky='ew')
        self.number_y.insert(0, "10")

    def create_graph(self):
        self.figure, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.master)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=9, padx=45, pady=5, sticky='nsew')

    def create_buttons(self):
        self.buttons = CalculatorButton(self.master, self.calculator_logic.button_click)

    def button_click(self):
        self.calculator_logic = CalculatorLogic(self.number_entry, self.number_x, self.number_y, self.result_label, self.figure, self.ax, self.canvas)

    def start(self):
        self.create_graph()
        self.button_click()
        self.create_buttons()
        self.master.mainloop()