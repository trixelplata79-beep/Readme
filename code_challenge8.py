print("Multiplication Table Maker")

number = eval(input("Enter a number : ---> " ))

for trix in range(1, 11, 1):
    result = number * trix 
    print(number, "n" , trix, "=", result )