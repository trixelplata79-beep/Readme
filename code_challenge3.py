name = input("what is your name? ")
fare = eval(input("Enter your fare fee ---> "))
student = input("are you a student?")
if student == "yes":
    discount = fare * 0.20
    new_fare = fare - discount
    print("Hi ", name)
    print("your discount is ", discount)
    print("your new fare is ", new_fare)
else:
    print("sorry ", name, "you are not eligitable for a student discount")