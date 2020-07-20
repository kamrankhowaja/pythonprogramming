#Check whether the number is one digit or two digit
print("Task 1")
num = int(input("Enter Any number from 0 to 999 : "))
if num>=0 and num<=9:
    print("One digit number")
elif num>=10 and num<=99:
    print("Two digit number")
elif num>=100 and num<=999:
    print("Three digit number")
else:
    print("Number you enter is negative")

#Guessing Game
print("Task 2")
num2=int(int(input("Enter any number between 1-12 and i will guess")))
if num2>7:
    print("Your number is Above Seven i think")
elif num2<7:
    print("your number is below Seven i think")
elif num2==7:
    print("Lucky Seven")
else:
    print("Your Number is negative")