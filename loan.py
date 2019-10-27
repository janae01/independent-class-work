# Name: Janae Dorsey
# File: loan.py
#
# Problem/Purpose: To calculate the the monthly payment, total amount paid, and the total interest paid on a loan
#
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
#
# Inputs: From user, initial loan amount, the time span (months) of the loan, and the interest rate of the loan.
# Outputs: Calculate the monthly payment, the total amount of money paid, and the total amount of interest paid on the loan.


print("This program calculates the monthly payment, total amount paid, and the total interest paid on a loan.")


def main():

#Ask user for input of loan amount
    principal = eval(input("What is the principal loan amount?"))
#Ask user for input of number of months
    months = eval(input("What is the number of months of the loan?"))
#Ask user for interest rate
    interest_rate = eval(input("What is the interest rate? (enter as 2.1 not 0.021)"))

#Calculate rate
    rate = interest_rate / 1200
#Calculate monthly payment
    monthly_payment = (principal * (rate * ((1+rate)**months))) / ((1+rate)**months - 1)
#Calculate the total amount paid
    total_amount_paid = monthly_payment * months
#Calculate the total interest paid
    total_interest_paid = total_amount_paid - principal

#Output the results for monthly payment
    print("The payment for each month is ${}." .format(monthly_payment))
#Output the results for total amount paid
    print("The total amount paid over the life of the loan is ${}." .format(total_amount_paid))
#Output the results for total interest paid
    print("The total interest paid is ${}." .format(total_interest_paid))


main()