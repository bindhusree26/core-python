# if
myInput = int(input("Enter the num: "))
if (myInput % 3 == 0 and myInput % 5 == 0):
    print("Positive")
print("Executed")

if True:
    print("It is true")
print("Exit")

a = 10
if (a == 10):
    print(True)
print("Exit")

# if-else
age = int(input("Enter the age: "))
if (age >= 18 and age <=100): # can also be written as 18 <= age <= 100
    print("You can vote")
else:
    print("Voting is not allowed")
print("Thank you")

# elif
marks = int(input("Enter the marks: "))
if (marks > 100):
    print("Enter the valid number")
elif (marks >= 85 and marks <= 100):
    print("Distinction")
elif (marks >= 60 and marks <= 84):
    print("First class")
elif(marks >= 35 and marks <= 59):
    print("Second class")
else:
    print("Fail")