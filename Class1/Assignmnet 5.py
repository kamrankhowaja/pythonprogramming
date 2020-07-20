#Star printing

a =int(input("Enter number :"))

for i in range(1, a):
    for j in range(1,a-i):
        print(" " , end="")
    print(str("*")*i)
