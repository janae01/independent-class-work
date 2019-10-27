# Name: Janae Dorsey
# File: workingTime.py
#
# Problem/Purpose: This program will calculate the amount of time worked by teams at a company in days, hours, and minutes.
#
# Certification of Authenticity:
# I certify that this lab is entirely my own work.
#
# Inputs: Number of teams, Number of employees on the team, Number of hours and minutes worked by each employee
# Outputs: Total number of hours and minutes worked by an entire team, Total number of days, hours, and minutes worked by teams in a company


def part1():
    print("This program calculates the number of hours and minutes worked by employees on a team.")
    total_hours = 0
    total_minutes = 0
    num_of_employees = eval(input("Enter the number of employees on the team: "))
    for j in range(int(num_of_employees)):
        hours = eval(input("\nEnter the number of hours worked by Employee #" + str(j+1) + " (Enter 0 if total time worked is in mintes): "))
        minutes = eval(input("Enter the number of minutes worked by Employee#" + str(j+1) + " (Enter 0 if total time worked is in hours: "))
        total_hours += hours
        total_minutes += minutes
    hour_calc = total_minutes // 60
    minutes_calc = total_minutes % 60
    total_hours += hour_calc
    print("\nTotal time:", total_hours, "hours", minutes_calc, "minutes")



def part2():
    print("This program calculates the number of days, hours, and minutes worked by teams in a company.")
    teams_days = 0
    teams_hours = 0
    teams_minutes = 0
    num_of_teams = eval(input("Enter the number of teams in the company: "))
    for i in range(num_of_teams):
        total_hours = 0
        total_minutes = 0
        num_of_employees = eval(input("\nEnter the number of employees on the team: "))
        for j in range(int(num_of_employees)):
            hours = eval(input("Enter the number of hours worked by Employee #" + str(
                j + 1) + " (Enter 0 if total time worked is in mintes): "))
            minutes = eval(input("Enter the number of minutes worked by Employee#" + str(
                j + 1) + " (Enter 0 if total time worked is in hours: "))
            total_hours += hours
            total_minutes += minutes
        hour_calc = total_minutes // 60
        minutes_calc = total_minutes % 60
        total_hours += hour_calc
        teams_hours += total_hours
        teams_minutes += minutes_calc
        print("Team" + str(i+1) + " Total time:", total_hours, "hours", minutes_calc, "minutes")
    teams_hours_calc = teams_minutes // 60
    teams_minutes_calc = teams_minutes % 60
    teams_hours += teams_hours_calc
    teams_days_calc = teams_hours // 24
    teams_hours = teams_hours % 24
    teams_days += teams_days_calc
    print("\nTotal time of all teams:",teams_days, "days", teams_hours, "hours", teams_minutes_calc, "minutes")


def main():
    #part1()
    part2()



main()