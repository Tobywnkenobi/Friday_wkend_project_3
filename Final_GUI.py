import tkinter as tk
from tkinter import ttk, messagebox

class Mortgage:

    def __init__(self, rent_amount, purchase_price, expenses):
        self.rent_amount = rent_amount
        self.purchase_price = purchase_price
        self.expenses = expenses

    def property_annual_income(self):
        return (self.rent_amount * 12) - self.expenses

    def R_O_I(self):
        annual_net_income = self.property_annual_income()
        return (annual_net_income / self.purchase_price) * 100

class MortgageApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Mortgage ROI Calculator")
        self.geometry("300x250")

        self.create_widgets()

    def create_widgets(self):

        ttk.Label(self, text="Monthly Rent:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.rent_amount_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.rent_amount_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self, text="Purchase Price:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.purchase_price_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.purchase_price_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self, text="Annual Expenses:").grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.expenses_var = tk.DoubleVar()
        ttk.Entry(self, textvariable=self.expenses_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self, text="Calculate ROI", command=self.calculate_roi).grid(row=3, column=0, columnspan=2, pady=15)

        ttk.Label(self, text="ROI:").grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)
        self.roi_var = tk.StringVar()
        ttk.Label(self, textvariable=self.roi_var).grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

    def calculate_roi(self):
        rent_amount = self.rent_amount_var.get()
        purchase_price = self.purchase_price_var.get()
        expenses = self.expenses_var.get()

        property_instance = Mortgage(rent_amount, purchase_price, expenses)
        roi = property_instance.R_O_I()

        self.roi_var.set(f"{roi:.2f}%")

if __name__ == "__main__":
    app = MortgageApp()
    app.mainloop()
