#Star printing
print("Task 1")
a =int(input("Enter number :"))

for i in range(1,a+1):
    for j in range(0,a-i):
        print(" " , end="")
    print(str("*")*i)

print("Task 2")
for f in range(0,a):
    for g in range(0,a-f):
        print("*",end=" ")
    print()