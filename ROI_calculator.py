"""
# How to solve a problem:

#     -Figure out wher the input and its type are
#     -Set up a function
#     -Figure out what the output and its type are
#     -Gather your Knowledge
#     -Gathers your contraints (Not Always Necessary)
#     -Determine a Logical way to solve the problem
#      -Write each step out in English
#       -Write each step out in Python-esse (sudo-code)
#       -Invoke and Test your function


income minus expenses  

annual net income = (monthly rent *12) - annual expenses

# ROI = (property_annual_income / ) * 100
"""
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