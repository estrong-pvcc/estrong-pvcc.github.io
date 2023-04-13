# Name: Erica Strong

# Prog Purpose: This program computes employee weekly pay

# Category codes:

#   C Cashier: $16.50

#   S Stocker: $15.75

#   J Janitor: $15.75

#   M Maintenance: $19.50

import datetime

# define pay rates & deduction rates

PAY_RATES = (16.50, 15.75, 15.75, 19.50)

DEDUCTION_RATES = (0.12, 0.03, 0.062, 0.0145)

# define global variables

inout = 'C' # C means Cashier, S means Stocker, J means Janitor, M means Maintenance

hoursworked= 0

payrates = 0

deductionrates = 0

grosspay = 0

netpay = 0

############ Define program functions ############

def main():

    another_employee = True

    while another_employee:

        hours_worked, job_code = get_user_data()

        gross_pay = perform_calculations(hours_worked, job_code)

        total_deductions, deductions = perform_deductions(gross_pay)

        net_pay = gross_pay - total_deductions

        display_results(hours_worked, gross_pay, deductions, total_deductions, net_pay)

        yesno = input("\nWould you like to enter data for another employee? (Y/N):")

        if yesno.upper() != "Y":

            another_employee = False

       

def get_user_data():

    while True:

        job_code = input("Please enter your job category (C=Cashier, S=Stocker, J=Janitor, M=Maintenance):")

        if job_code.upper() in ['C', 'S', 'J', 'M']:
            break

        print('Invalid job code. Please enter a valid job code.')

    hours_worked = float(input("Please enter your hours for the week: "))
   
    pay_rate_index = ord(job_code.upper()) - ord('C')

    if pay_rate_index >=len(PAY_RATES):

        pay_rate_index = len(PAY_RATES)-1

    return hours_worked,pay_rate_index

def perform_calculations(hours_worked, pay_rate_index):

    gross_pay = hours_worked * PAY_RATES[pay_rate_index]

    return gross_pay

def perform_deductions(gross_pay):

    deductions = []

    for rate in DEDUCTION_RATES:

        deduction_amount = gross_pay * rate

        deductions.append(deduction_amount)

    total_deductions = sum(deductions)

    return total_deductions, deductions

def display_results(hours_worked, gross_pay, deductions, total_deductions, net_pay):

    print('\nFresh Food Marketplace')

    print(f'\nHours worked: {hours_worked}')

    print(f'\nGross pay: ${gross_pay:.2f}')

    for i, deduction in enumerate(deductions):

        print(f'Deduction {i+1}: ${deduction:.2f}')

    print(f"Total deductions: ${total_deductions:.2f}")

    print(f"Net pay: ${net_pay:.2f}")

    print(str(datetime.datetime.now()))

############ call on main program to execute ############

main()
