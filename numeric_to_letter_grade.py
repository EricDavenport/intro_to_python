def numeric_to_letter_grade(grade):
    #get user input of a numerical grade
    #grade = input("Enter your grade: ")

    # cast to an int
    #grade = int(grade)

    # test the range of the numbers and print appropriate letter grade
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print('C')
    elif grade >= 60:
        print('D')
    else:
        print('F')

# get user input of numeric grade
grade = input("Enter a numeric grade: ")
grade = int(grade)

# call the numeric_to_letter_grade function defined above
numeric_to_letter_grade(grade)
