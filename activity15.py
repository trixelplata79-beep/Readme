pers = 'Trixel'
midol = 'Leal'
last = 'Plata'

print("My name is " , pers," ", midol," ",last)



up = 'Trixel'
gp = 'Leal'
hp = 'Plata'

print(f"My name is {up} {gp} {hp} ")



upm = 'Trixel'
gpm = 'Leal' 
hpm = 'Plata' 

print(f"My name is {upm.upper()} {gpm.upper()} {hpm.upper()} {10 + 8}") 


una = 'Trixel' 
ikalawa = 'Leal' 
ikatlo = 'Plata' 

print(f"My name is {una.lower()} {ikalawa.lower()} {ikatlo.lower()} {10 + 8}") 



sum = 0
for add in range(1, 11, 1):
    num = eval(input(f" {add} - Input any number: "))
    sum += num
print(f"The total sum of all the numbers is {sum} ")