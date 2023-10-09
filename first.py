print("Hello World")
print("What do you want to do?")
print("1. Divide")
print("2. Multiply")
print("3. Addition")
print("4. Subtraction")
print("5. Find power. Like = 2**2=4")
print("6. simple interest")
operation = int(input("Select one operation: "))

if operation == 1:
    STOP = int(input("Enter the dividend: "))
    B = int(input("Enter the divisor: "))
    while STOP % B == 0:
        STOP = STOP // B
        print(STOP)
        break
    
    if STOP % B == 0:
        print("This is not divisible")
    else:
        print("Successfully divided")

elif operation == 2:
    random = int(input("Enter the first number: "))
    S = int(input("Enter the second number: "))
    print(random * S)

elif operation == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1 + num2)

elif operation == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(num1 - num2)

elif operation == 5:
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    print(base ** exponent)

elif operation == 6:
    principle = int(input("Enter the P: "))
    rate = int(input("Enter R here: "))
    time = int(input("Enter T here: "))
    print(principle * rate * time // 100)

else:
    print("Invalid operation selected")