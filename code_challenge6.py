print("Enter 7 numbers")

result = 0
for odd in range(7):
    number = eval(input("Enter any number: "))
    if number % 2 != 0:
        result += number
    
print("The sum of all odd number is:"