# Name: Janae Dorsey
# File: weightedAverage.py
#
# Purpose: This program will read students' grades and their weights from a text file and
# write each student's avergae (number and letter grade) and the class' average to a new text file.

# Certification of Authenticity:
# I certify that this lab is entirely my own work.


#defines function that will accept parameters
def weighted_average(infile_name, outfile_name):

    #opens files to read from and write to
    infile = open(f'{infile_name}', "r")
    outfile = open(f'{outfile_name}', "w")

    #creates string with letter grades
    letter_grades = "FFFFFFDCBA"

    #initiates accumulator for class total
    class_total = 0

    #loops through lines in file to get grades and weights
    for line in infile:
        numbers_list = []
        lineInfo = line.split()
        g_w = lineInfo[2:]

        #loops through grades and weights to seperate them
        for i in g_w:
            numbers = int(i)
            numbers_list.append(numbers)
        weights = numbers_list[1::2]
        grades = numbers_list[::2]

        #initiates accumulator for individual total
        total = 0

        #loops through grades, multiplies them by weights (indexing), adds them together
        for i in range(len(grades)):
            addition = grades[i] *  weights[i]
            total += addition

        #calculates student average and letter grade
        average = total / 100
        letter = int(average // 10)
        letter_grade = letter_grades[letter]

        #formats output
        name = lineInfo[0:2]
        z = name[1].replace(":", "'s")
        output = "{} {} average: {} {}".format(name[0], z, average, letter_grade)
        print(output, file=outfile)

        #adds students' averages together
        class_total += average

    #Counts # of students in file
    line_count = len(open(f'{infile_name}').readlines())

    #calculates and prints class avergae and letter grade
    class_average = round((class_total / line_count), 1)
    class_letter = int(class_average // 10)
    class_letter_grade = letter_grades[class_letter]
    print("\nClass average:", class_average, class_letter_grade, file=outfile)


    #closes files
    infile.close()
    outfile.close()



def main():
    #calls function with actual parameters
    weighted_average("grades.txt", "janaedorsey_avg.txt")
main()


