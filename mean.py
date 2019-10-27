# Name: Janae Dorsey
# File: mean.py
#
# Problem/Purpose: This program will calculate the RMS Average, the Harmonic Mean, and the Geometric Mean of a specified group of numbers.
#
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
#
# Inputs: The number of values and the values themselves
# Outputs: The RMS Average, the Harmonic Mean, and the Geometric Mean
#
#Algorithm: 1. Print purpose
#2. Ask user for number of values (store in list)
#3. Ask user for values
#4. Calculate rms average (the square root of the average of the square of the values)
#5. Calculate the harmonic mean (the number of values divided by sum of the reciprocals of each value)
#6. Calculate the geometric mean (the nth root of the product of the values)
#7. Print/Show the rms average, the harmonic mean, and the geometric mean


import math


def main():
    print("This program calculates the RMS Average, the Harmonic Mean, and the Geometric Mean.")
    num_of_values = eval(input("\nEnter the number of values: "))
    rms_sum = 0
    harmonic_sum = 0
    gms_product = 1
    for i in range(num_of_values):
        values = [eval(input("Enter a value: "))]
        for numbers1 in values:
            squares = numbers1 **  2
            rms_sum += squares
            average_of_squares = rms_sum / num_of_values
            rms_average = math.sqrt(average_of_squares)
            denominator = 1 / numbers1
            harmonic_sum += denominator
            harmonic_mean = num_of_values / harmonic_sum
            gms_product = gms_product * numbers1
            geometric_mean = gms_product ** (1 / num_of_values)
    print("\nThe RMS Average of the values is " + str(round(rms_average, 3)) + ".")
    print("The Harmonic Mean of the values is " + str(round(harmonic_mean, 2)) + ".")
    print("The Geometric Mean of the values is " + str(round(geometric_mean, 2)) + ".")






main()
