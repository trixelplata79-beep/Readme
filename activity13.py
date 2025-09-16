#ask user to input ten(10) numbers  - checked 
#after get the summation  of all numbers 

sum = 0
for R in range(1, 11, 1):
       print(R)
       number = eval(input("Enter any number ---> "))
sum += number
print("The sum of all the numbers given is", sum)