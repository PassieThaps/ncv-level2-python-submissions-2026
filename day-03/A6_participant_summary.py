fullname = input("Please enter your name: ")
staffnumber = input("Please enter your staff number: ")
level = input("Please enter your level: ")


if fullname == "": 
    print("Error, make sure the name is not empty and the staff number has numberical values")
    
elif not staffnumber.isdigit():
        
    print("Error, make sure the name is not empty and the staff number has numberical values")
    
else:
    print("Welcome ", fullname, "your staff number is ", staffnumber, "and your level is ", level)
    
        

        
    