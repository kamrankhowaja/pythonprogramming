#Caluclator
def add(a,b):
    c=a+b
    return c

def subtract(a,b):
    c=a-b
    return c

def multiply(a,b):
    c=a*b
    return c
def divide(a,b):
    c=a/b
    return c

print("Simple Calculator")
num1=int(input("Enter your First number"))
num2=int(input("Enter your Second number"))

a=add(num1,num2)
s=subtract(num1,num2)
m=multiply(num1,num2)
d=divide(num1,num2)

print("Addition Answer is",a)
print("Subtraction Answer is",s)
print("Multiplication Answer is",m)
print("Division Answer is",d)

