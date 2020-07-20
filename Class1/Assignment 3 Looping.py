#Table Printing
print("Task 1 : Table Printing")
num=int(input("Enter any Number whose table you want to Print : "))
for i in range(1,11):
    print("{0} * {1} = {2}".format(num,i,num*i))

#even number
print("Task 2: Even number Printing 2-18")
for j in range(2,20,2):
    print("{0}".format(j))
