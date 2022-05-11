number = int(input("What is the number"))

sum = 0

if number<=15 and number>=9:
    for i in range(1,15):
        if number%i == 0:
            sum = sum + i
else:
    print("Number out of range (9 to 15")