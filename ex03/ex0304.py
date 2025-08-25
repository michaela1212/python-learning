score = input("Please enter your score: ")
try:
    grade = float(score)
    if grade > 1:
        print("Bad Score")
    elif grade >= 0.9:
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