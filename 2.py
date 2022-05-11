n = int(input("How many number you want to print?\n"))

Sum = 0
oddSum = 0

for i in range(1,n+1):
    z = int(input(f"What is the number {i}-\n"))
    if z % 2 == 0:
        Sum = Sum + z
    else:
        oddSum = oddSum + z

print(f"Total Even Sum Is {Sum}")
print(f"Total Odd Sum Is {oddSum}")