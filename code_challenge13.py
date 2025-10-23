name = input("Input your name---> ")
print(" +++++++++++++++++++ ")
print("ODD NUMBER SUMMATION, press 0 to stop")
print(" ++++++++++++++++++++\n ")
plata = True
sum = 0
odd = " " #string

while plata == True:
        num = eval(input("input a random number --->"))
        
        if num % 2  == 1:
            print("ODD NUMBER DETECTED, code continues")
            sum += num
            odd += str(num) + " "
            continue
        elif num == 0:
             print("program stops....!!!!")
             break
        else:
             if num % 2 == 0:
                 print("EVEN NUMBER DETECTED, continue")
             else:
                     print("invalid input")
                     continue
print(f"Hi {name}, the sum of all odd number is {sum}")
print(f"ODD Numbers Detected Included the ff {odd}")