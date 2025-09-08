score = input("Please enter your score: ")
try:
    grade = float(score)
    if grade > 1:
        raise Exception
    elif grade <= 1 and grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("Bad Score")

#Write a program to prompt for a score between 0.0 and 1.0. If the score is out 

#of range, print an error message. If the score is between 0.0 and 1.0, print a grade.
