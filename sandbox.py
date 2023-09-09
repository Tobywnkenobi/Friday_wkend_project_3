"""
Now, it is time to try to use tkinter....this can't go well.


"""

from tkinter import *
from tkinter import ttk


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

 
def user_input():
    rent_amount = float(input("Enter the monthly rent: "))
    purchase_price = float(input("How much did you pay for the property?: "))
    expenses = float(input("What expense did you occur in maintaing this property over the course of a year?" ))
    return rent_amount, purchase_price, expenses 

rent_amount, purchase_price, expenses = user_input()
property = Mortgage(rent_amount, purchase_price, expenses)
roi = property.R_O_I()

print(f"The Return on Investment (ROI) is: {roi:.2f}%")


property_instance = Mortgage(1500, 300000, 10000)  # rent:$1000, Purchase price: $200,000, Annual expense: $10,000 