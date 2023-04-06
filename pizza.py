#Name: Erica-Strong
#Prog Purpose: Welcome to Palermo Pizza
#  Sales tax rate: 5.5%
#  Pizza sizes
#     small: $9.99
#     medium: $12.99
#     large: $14.99
#     extra large: $17.99

import datetime

# Define global variables
SALES_TAX_RATE = 0.055
SIZE_PIZZA = ['small', 'medium', 'large', 'extra large']
PRICE_PIZZA = [9.9, 12.9, 14.9, 17.9]

# Initialize variables
size_pizza = 0
num_pizzas = 0
subtotal = 0
sales_tax = 0
total = 0

##############  define program functions  ################
def main():
    another_order = True
    while another_order:
      get_user_data()
      perform_calculations()
      display_results()
      yesno = input("Would you like to place another order? (Y\\N): ")
      if yesno.upper() != "Y":
          another_order = False

def get_user_data():
    global size_pizza, num_pizzas
    size_pizza = input("Size of pizza: ")  
    num_pizzas = int(input("Number of pizzas: "))  

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_pizzas * PRICE_PIZZA[SIZE_PIZZA.index(size_pizza)]
    sales_tax = subtotal * SALES_TAX_RATE 
    total = subtotal + sales_tax  

def display_results():
    print('------------------------------')
    print('**** PALERMO PIZZA ****')
    print('Your neighborhood pizza place')
    print('------------------------------')
    print(f"Size of pizza: {size_pizza}")
    print(f"Number of pizzas: {num_pizzas}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Sales tax: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")
    print('------------------------------')
    print(str(datetime.datetime.now()))
    print('------------------------------')
    
##########  call on main program to execute  ############
main()
