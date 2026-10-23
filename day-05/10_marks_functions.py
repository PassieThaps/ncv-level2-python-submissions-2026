def get_marks():
    mark_list = []
    mark = int(input("Please enter a mark or -1 to stop: "))

    while mark != -1:
        mark_list.append(mark) #How to add values in a list
        mark = int(input("Please enter a mark or -1 to stop: "))
    return mark_list

def print_list(mark_list):
    print("Number of marks captured:", len(mark_list))
    
def print_marks(mark_list):    
    for i in range(len(mark_list)):   
        print('Student', i + 1,'-', mark_list[i])

#Get the sum of all marks
def get_sum(mark_list):
    sum = 0
    for i in range(len(mark_list)):
        mark = mark_list[i]
        sum = sum + mark
    return sum
    
#Find highest
def get_highest(mark_list):
    highest = 0
    for i in range(len(mark_list)):
        mark = mark_list[i]
        if mark > highest:
            highest = mark

    print("The highest mark is:", highest)

menu = "Press 1: Capture mark\n"
menu += "Press 2: Check number of marks\n"
menu += "Press 3: Calculate sum of mark\n"
menu += "Press 4: Find the highest mark\n"
menu += "Press -1: To exit\n"

print(menu)
choice = int(input("Enter a number to make a choice: "))
captured_mark = []
while choice != -1:    
    if choice == 1:        
        captured_mark = get_marks()
        print(captured_mark)
    elif choice == 2:
        print_list(captured_mark)
    elif choice == 3:
        calc_sum = get_sum(captured_mark)
        print('Sum of marks captured is: ',calc_sum)
    elif choice == 4:
        get_highest(captured_mark)
        
    else: print("Selected choice not on the menu")

    print(menu)
    choice = int(input("Enter a number to make a choice: "))
