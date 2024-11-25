import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

class CalculatorButton:
    def __init__(self, master, command):
        self.master = master
        self.command = command
        self.create_buttons()
        
    def create_style(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 14), background="lightblue", foreground="black")
        style.map("TButton", background=[("active", "deepskyblue")])

    def create_trigonometric(self):
        self.button_sin = ttk.Button(self.master, text="sin", command=lambda: self.command("sin("), width=7, padding=(10, 20))
        self.button_sin.grid(row=1, column=0, padx=(45,5), pady=5)

        self.button_cos = ttk.Button(self.master, text="cos", command=lambda: self.command("cos("), width=7, padding=(10, 20))
        self.button_cos.grid(row=1, column=1, padx=5, pady=5)

        self.button_tan = ttk.Button(self.master, text="tan", command=lambda: self.command("tan("), width=7, padding=(10, 20))
        self.button_tan.grid(row=1, column=2, padx=5, pady=5)

        self.button_asin = ttk.Button(self.master, text="asin", command=lambda: self.command("asin("), width=7, padding=(10, 20))
        self.button_asin.grid(row=2, column=0, padx=(45,5), pady=5)

        self.button_acos = ttk.Button(self.master, text="acos", command=lambda: self.command("acos("), width=7, padding=(10, 20))
        self.button_acos.grid(row=2, column=1, padx=5, pady=5)

        self.button_atan = ttk.Button(self.master, text="atan", command=lambda: self.command("atan("), width=7, padding=(10, 20))
        self.button_atan.grid(row=2, column=2, padx=5, pady=5)

        self.button_log = ttk.Button(self.master, text="log", command=lambda: self.command("log("), width=7, padding=(10, 20))
        self.button_log.grid(row=3, column=0, padx=(45,5), pady=5)

        self.button_ln = ttk.Button(self.master, text="ln", command=lambda: self.command("ln("), width=7, padding=(10, 20))
        self.button_ln.grid(row=3, column=1, padx=5, pady=5)

        self.button_sqrt = ttk.Button(self.master, text="sqrt", command=lambda: self.command("sqrt("), width=7, padding=(10, 20))
        self.button_sqrt.grid(row=3, column=2, padx=5, pady=5)

        self.button_mod = ttk.Button(self.master, text="mod", command=lambda: self.command("mod"), width=7, padding=(10, 20))
        self.button_mod.grid(row=4, column=1, padx=5, pady=5)

        self.button_clear = ttk.Button(self.master, text="AC", command=lambda: self.command('AC'), width=7, padding=(10, 20))
        self.button_clear.grid(row=4, column=0, padx=(45,5), pady=5)

        self.button_deg = ttk.Button(self.master, text="^", command=lambda: self.command('^'), width=7, padding=(10, 20))
        self.button_deg.grid(row=4, column=2, padx=5, pady=5)

    def create_numbers(self):
        self.button_1 = ttk.Button(self.master, text="1", command=lambda: self.command(1), width=7, padding=(10, 20))
        self.button_1.grid(row=1, column=4, padx=(25, 5), pady=5)

        self.button_2 = ttk.Button(self.master, text="2", command=lambda: self.command(2), width=7, padding=(10, 20))
        self.button_2.grid(row=1, column=5, padx=5, pady=5)

        self.button_3 = ttk.Button(self.master, text="3", command=lambda: self.command(3), width=7, padding=(10, 20))
        self.button_3.grid(row=1, column=6, padx=5, pady=5)

        self.button_4 = ttk.Button(self.master, text="4", command=lambda: self.command(4), width=7, padding=(10, 20))
        self.button_4.grid(row=2, column=4, padx=(25, 5), pady=5)

        self.button_5 = ttk.Button(self.master, text="5", command=lambda: self.command(5), width=7, padding=(10, 20))
        self.button_5.grid(row=2, column=5, padx=5, pady=5)

        self.button_6 = ttk.Button(self.master, text="6", command=lambda: self.command(6), width=7, padding=(10, 20))
        self.button_6.grid(row=2, column=6, padx=5, pady=5)

        self.button_7 = ttk.Button(self.master, text="7", command=lambda: self.command(7), width=7, padding=(10, 20))
        self.button_7.grid(row=3, column=4, padx=(25, 5), pady=5)

        self.button_8 = ttk.Button(self.master, text="8", command=lambda: self.command(8), width=7, padding=(10, 20))
        self.button_8.grid(row=3, column=5, padx=5, pady=5)

        self.button_9 = ttk.Button(self.master, text="9", command=lambda: self.command(9), width=7, padding=(10, 20))
        self.button_9.grid(row=3, column=6, padx=5, pady=5)

        self.button_0 = ttk.Button(self.master, text="0", command=lambda: self.command(0), width=7, padding=(10, 20))
        self.button_0.grid(row=4, column=4, padx=(25, 5), pady=5)

        self.button_dot = ttk.Button(self.master, text=".", command=lambda: self.command("."), width=7, padding=(10, 20))
        self.button_dot.grid(row=4, column=5, padx=5, pady=5)

        self.button_equal = ttk.Button(self.master, text="=", command=lambda: self.command("="), width=7, padding=(10, 20))
        self.button_equal.grid(row=4, column=6, padx=5, pady=5)

    def create_ariphmetic(self):
        self.button_left = ttk.Button(self.master, text="(", command=lambda: self.command("("), width=7, padding=(10, 20))
        self.button_left.grid(row=1, column=7, padx=(25, 5), pady=5)

        self.button_right = ttk.Button(self.master, text=")", command=lambda: self.command(")"), width=7, padding=(10, 20))
        self.button_right.grid(row=1, column=8, padx=5, pady=5)

        self.button_multiply = ttk.Button(self.master, text="*", command=lambda: self.command('*'), width=7, padding=(10, 20))
        self.button_multiply.grid(row=2, column=7, padx=(25, 5), pady=5)

        self.button_del = ttk.Button(self.master, text="/", command=lambda: self.command("/"), width=7, padding=(10, 20))
        self.button_del.grid(row=2, column=8, padx=5, pady=5)

        self.button_add = ttk.Button(self.master, text="+", command=lambda: self.command("+"), width=7, padding=(10, 20))
        self.button_add.grid(row=3, column=7, padx=(25, 5), pady=5)

        self.button_minus = ttk.Button(self.master, text="-", command=lambda: self.command('-'), width=7, padding=(10, 20))
        self.button_minus.grid(row=3, column=8, padx=5, pady=5)

        self.button_c = ttk.Button(self.master, text="C", command=lambda: self.command("C"), width=7, padding=(10, 20))
        self.button_c.grid(row=4, column=7, padx=(25, 5), pady=5)

        self.plot_button = ttk.Button(self.master, text="X", command=lambda: self.command("x"), width=7, padding=(10, 20))
        self.plot_button.grid(row=4, column=8, padx=5, pady=5)

        self.button_x = ttk.Button(self.master, text="Graph", command=lambda: self.command("Graph"), width=7, padding=(10, 20))
        self.button_x.grid(row=7, column=8, padx=5, pady=5)

        self.button_clear = ttk.Button(self.master, text="About", command=lambda: self.command('About'), width=7, padding=7)
        self.button_clear.grid(row=7, column=0, padx=(45,5), pady=5)

        self.button_clear = ttk.Button(self.master, text="History", command=lambda: self.command('History'), width=6, padding=6)
        self.button_clear.grid(row=0, column=8, padx=(15,5), pady=(15, 25))

    def create_buttons(self):
        self.create_style()
        self.create_trigonometric()
        self.create_numbers()
        self.create_ariphmetic()