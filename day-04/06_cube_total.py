n = int(input("please enter a whole number: "))
total = int(0)
for n in range(1,n+1):
    n = n **3
    print(n, end=",")
    total = total + n
print(" The total of cubes is: ", total)

