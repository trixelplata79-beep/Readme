say = input("what do you want your parrot to say? --> " )
repeat = eval(input("How many times should the parrot squawk? --> "))

for T in range(repeat, 0, -1):
    print("🦜 Squawk!" ,say)