mark_list = []
mark = int(input("Please enter a mark or -1 to stop: "))

while mark != -1:
    mark_list.append(mark) #How to add values in a list
    mark = int(input("Please enter a mark or -1 to stop: "))

print("Number of marks captured:", len(mark_list))

for i in range(len(mark_list)):   
    print('Student', i + 1,'-', mark_list[i])

#Get the sum of all marks
sum = 0
for i in range(len(mark_list)):
    mark = mark_list[i]
    sum = sum + mark
    
print('The sum of all the marks captured is: ', sum)
    
#Get the average of all marks
total = 0
for i in range(len(mark_list)):
    mark = mark_list[i]
    total = total + mark
    
avg = total / len(mark_list)
print('The average of all marks captured is: ', avg)
    
#Find highest
highest = mark_list[0]

for mark in mark_list:
    if mark > highest:
        highest = mark

print("The highest mark is:", highest)

    
    