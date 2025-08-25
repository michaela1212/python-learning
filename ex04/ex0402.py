def computegrade(grade):
    if grade > 1:
        return "Bad Score"
    elif grade >= 0.9:
        return "A"
    elif grade >= 0.8:
        return "B"
    elif grade >= 0.7:
        return "C"
    elif grade >= 0.6:
        return "D"
    else:
        return "F"
try:
    grade = float(input("Please enter your score: "))
except:
    print("Bad Score")
    quit()

computegrade(grade)
print(computegrade(grade))

#Rewrite the grade program from the previous chapter using a function called 
# computegrade that takes a score as its parameter and returns a grade as a string.