total = 0
count = 0
mark = int(input("Please enter a mark or -1 to stop: "))
while mark != -1:
    if 0 <= mark <= 100:
        total = total + mark
        count = count + 1
    else:
        print("Rejected: ", mark, "is not a valid mark")
    mark = int(input("Please enter a mark or -1 to stop: "))
if count > 0:
    average = total / count
    print(f"Your average mark is: {average:.2f}")
else:
    print("No valid marks entered.")
