#Capture marks
strmark = input("Enter mark: ")
#Show marks
    
if strmark.isdigit():
    mark = int(strmark)    
    print("Mark: ", strmark)
        
    if mark >= 0 or mark <= 100:
        if mark >=80 and mark <=100:
            print("Outstanding")
        elif mark >=70 and mark <=79:
            print("Highly competent")
        elif mark >=50 and mark <=69:
            print("competent")
        elif mark >=40 and mark <=49:
            print("Not yet competent")
        elif mark >=0 and mark <=39:
            print("Not achieved")
else:
    print("invalid! Enter a valid mark")



