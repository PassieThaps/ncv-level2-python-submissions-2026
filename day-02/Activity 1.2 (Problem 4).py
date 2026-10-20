#Highest common factor (Problem 4)

firstno = int(input("Enter First Number: "))
secondno = int(input("Enter Second Number: "))

if firstno < secondno:
    hcf = firstno
else:
    hcf = secondno

while firstno % hcf != 0 or secondno % hcf != 0:
    hcf = hcf - 1

print("The highest common factor is: ", hcf)
