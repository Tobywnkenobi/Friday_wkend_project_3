import tkinter as tk
from tkinter import ttk

class SimpleCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Calculator")
        self.geometry("300x200")

        self.create_widgets()

    def create_widgets(self):
        # Entry widget to input numbers
        self.entry = ttk.Entry(self)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        # Create buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("0", 4, 1),
            ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
            ("=", 4, 2), ("C", 4, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        button = ttk.Button(self, text=text, command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == "C":
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    app = SimpleCalculator()
    app.mainloop()
