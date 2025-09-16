c1 = 1000
c2 = 800
c3 = 600
c4 = 400
c5 = 200
c6 = 100
c7 = 50
c8 = 10
c9 = 5
c10 = 1

denum = eval(input("Enter the amount to deposit --->  "))
print ("here is the breakdown of the deposit amount : ")
# b1 = demun // c1   

b1 = denum // c1
denum = denum % c1
b2 = denum  // c2
denum = denum % c2
b3 = denum // c3
denum = denum % c3
b4 = denum // c4
denum = denum % c4
b5 = denum // c5
denum = denum % c5
b6 = denum // c6
denum = denum % c6
b7 = denum //  c7
denum = denum % c7
b8 = denum // c8
denum = denum % c8
b9 = denum // c9
denum = denum % c9
b10 = denum // c10
denum = denum  % c10


print(b1, "-", c1)
print(b2, "-", c2)
print(b3, "-", c3)
print(b4, "-", c4)
print(b5, "-", c5)
print(b6, "-", c6)
print(b7, "-", c7)
print(b8, "-", c8)
print(b9, "-", c9)
print(b10,"-",c10)