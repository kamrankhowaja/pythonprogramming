
#Assignmnet 4 task 1
#Task 1: So you need to make a list of at least 5 participant height and using loop identify
#participants who height is less then 4ft and recommend them to improve their diet

height=[5,9,10,3,2] #random 5 people data
a=len(height) #just for the sake of information
print ("Total data is of",a,"participants")

for i in height:
    if i<=4:
        print("person with height",i,"ft Improve your Diet")
    else:
        print("person with height",i,"ft Good height")

