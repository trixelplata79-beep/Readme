#ITCS102 Finals Project - Interactive Menu Program 


import os
name = input ("Hi, what is your name?")
pangalan = input(f"Hello, {name}")
menu = input("Welcome to Python Menu Program")
cont = input("Type 'enter' to continue:")

def main_menu():
    os.system('cls')
    while True:
        print(f"Hi, {name}. You can choose anything here in the main menu.")
        print("----------MAIN MENU----------")
        print("1 - Print statements")
        print("2 - Operators")
        print("3 - Variables")
        print("4 - Functions")
        print("5 - Loops")
        print("0 - Exit")
        print("----------------------------")
        
        choice = input("Choose an option: 0-5 ")
        
        
        #MAIN MENU 1 
        if choice == "1":
            os.system('cls')
            while True:
               print(f"Hi, {name}. You are in PRINT STATEMENTS") 
               print("-------PRINT STATEMENTS-------")
               print("1 - Definition")
               print("2 - Example")
               print("3 - Try It Yourself")
               print("0 - Back")   
               print("------------------------------")
            
               select = input("Select your choice (0 - 3):")
                
           #SUB MENU 1 
               if select == '1':
                    os.system('cls')
                    print("----------DEFINITION----------")
                    print(" A print statement is a command in programming used to display text,numbers,or other data to the screen or console. ")
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
                    
                
               elif select == '2':
                    os.system('cls')
                    print("-----------EXAMPLE------------")
                    print("Input: print(\"Hello, world!\")")         
                    print("\nOutput: Hello, world!")
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                
        

               elif select == '3':
                    os.system('cls')
                    print("--------TRY IT YOURSELF-------")                   
                    print("------------------------------")
                    print("Example: \nprint(\"Hello World\")")
                    print("------------------------------")
                    print("ENTER on empty line to run the code")
                    print("------------------------------")
                    print("Try it Yourself:")

                    lines_of_code = []

                    while True:
                        line = input(">>> ")
                        if line.strip() == "": 
                            break
                        lines_of_code.append(line)

                    program_text = "\n".join(lines_of_code)

                    print("\nResult:")
                    try:
                        exec(program_text)
                        print("\nCode executed successfully!")
                    except Exception as e:
                        print("\nThere was an error in your code.")
                        print("Error details:", e)

                    print("-----------------------------")
                    select = input("\nPress (0) to return:")

                
               elif select == '0':
                    os.system('cls')
                    break
                
               else:
                    print("Invalid.")
                    
              
                    
                
        
        #MAIN MENU 2    
        if choice == "2":
            while True:
                os.system('cls')
                print(f"Hi, {name}. You are in OPERATORS category") 
                print("-----------OPERATORS----------") 
                print("1 - Definition")          
                print("2 - Example")
                print("3 - Try It Yourself")
                print("0 - Back")   
                print("------------------------------")
            
                select = input("Select your choice (0 - 3):")
        
           #SUB MENU 2
                if select == '1':
                    os.system('cls')
                    print("----------DEFINITION----------")
                    print("Operators are special symbols or keywords used in programming to perform operations on values or variables.")
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
                    
                elif select == '2':
                    os.system('cls')
                    print("------------EXAMPLE-----------")
                    print("Input: x = 5 + 3") 
                    print("print(x)")          
                    print("Output: 8")  
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                     
                elif select == '3':
                    os.system('cls')
                    print("------------------------------")
                    print("--------TRY IT YOURSELF-------")                   
                    print("------------------------------")
                    print("Example: \nx = 5 + 3")
                    print("print(x)")             
                    print("------------------------------")
                    print("ENTER twice to run the code")
                    print("------------------------------")
                    print("Try it Yourself:")

                    lines_of_code = []

                    while True:
                        line = input(">>> ")
                        if line.strip() == "": 
                            break
                        lines_of_code.append(line)

                    program_text = "\n".join(lines_of_code)

                    print("\nResult:")
                    try:
                        exec(program_text)
                        print("\nCode executed successfully!")
                    except Exception as e:
                        print("\nThere was an error in your code.")
                        print("Error details:", e)

                    print("-----------------------------")
                    select = input("\nPress (0) to return:")

                
                elif select == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid.")    
        

        #MAIN MENU 3   
        if choice == "3":
            while True:
                os.system('cls')
                print(f"Hi, {name}. You are in VARIABLES category") 
                print("-----------VARIABLES----------")
                print("1 - Definition")  
                print("2 - Example")
                print("3 - Try It Yourself")
                print("0 - Back")   
                print("------------------------------")
            
                select = input("Select your choice (0 - 3):")
        
            #SUB MENU 3
                if select == '1':
                    os.system('cls')
                    print("------------------------------")
                    print("----------DEFINITION----------")
                    print("------------------------------")
                    print("It allows you to store,share and use values while the program runs.") 
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
                    
                elif select == '2':
                    os.system('cls')
                    print("------------------------------")
                    print("-----------EXAMPLE------------")
                    print("Input: \n")
                    print("name = alice")
                    print("age = 12")
                    print("weight = 1.45") 
                    print("print(name, age, weight)")
                    print("Output: \n")   
                    print("(alice 12 1.45")
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
        
                elif select == '3':
                    os.system('cls')
                    print("------------------------------")
                    print("--------TRY IT YOURSELF-------")                   
                    print("------------------------------")
                    print("Example: \n")
                    print("age = 12")
                    print("weight = 1.45")
                    print("print(age, weight)")
                    print("------------------------------")
                    print("ENTER twice to run the code")
                    print("------------------------------")
                    print("Try it Yourself:")

                    lines_of_code = []

                    while True:
                        line = input(">>> ")
                        if line.strip() == "": 
                            break
                        lines_of_code.append(line)

                    program_text = "\n".join(lines_of_code)

                    print("\nResult:")
                    try:
                        exec(program_text)
                        print("\nCode executed successfully!")
                    except Exception as e:
                        print("\nThere was an error in your code.")
                        print("Error details:", e)

                    print("-----------------------------")
                    select = input("\nPress (0) to return:")

                
                elif select == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid.")



        #MAIN MENU 4   
        if choice == "4":
            while True:
                os.system('cls')
                print(f"Hi, {name}. You are in FUNCTIONS category") 
                print("-----------FUNCTIONS----------")
                print("1 - Definition")   
                print("2 - Example")
                print("3 - Try It Yourself")
                print("0 - Back")   
                print("------------------------------")
            
                select = input("Select your choice (0 - 3):")
        
            #SUB MENU 4
                if select == '1':
                    os.system('cls')
                    print("------------------------------")
                    print("----------DEFINITION----------")
                    print("------------------------------")
                    print(" A function is a block of reusable code designed to perform a specific task ") 
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
                    
                elif select == '2':
                    os.system('cls')
                    print("------------------------------")
                    print("-----------EXAMPLE------------")
                    print("Input:")
                    print("result = add_numbers(5, 3)")
                    print("print()")
                    print("Output:")
                    print("8")
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
        
                elif select == '3':
                    os.system('cls')
                    print("------------------------------")
                    print("--------TRY IT YOURSELF-------")                   
                    print("------------------------------")
                    print("Example: \ndef multiply(a, b):")
                    print("\treturn a * b") 
                    print("print(multiply(5, 3))")
                    print("------------------------------")
                    print("ENTER twice to run the code")
                    print("------------------------------")
                    print("Try it Yourself:")

                    lines_of_code = []

                    while True:
                        line = input(">>> ")
                        if line.strip() == "": 
                            break
                        lines_of_code.append(line)

                    program_text = "\n".join(lines_of_code)

                    print("\nResult:")
                    try:
                        exec(program_text)
                        print("\nCode executed successfully!")
                    except Exception as e:
                        print("\nThere was an error in your code.")
                        print("Error details:", e)

                    print("-----------------------------")
                    select = input("\nPress (0) to return:")

                
                elif select == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid.")



        #MAIN MENU 5   
        if choice == "5":
            while True:
                os.system('cls')
                print(f"Hi, {name}. You are in LOOPS category") 
                print("-------------LOOPS------------") 
                print("1 - Definition")  
                print("2 - Example")
                print("3 - Try It Yourself")
                print("0 - Back")   
                print("------------------------------")
            
                select = input("Select your choice (0 - 3):")
        
            #SUB MENU 5
                if select == '1':
                    os.system('cls')
                    print("------------------------------")
                    print("----------DEFINITION----------")
                    print("------------------------------")
                    print("A loop is a programming structure that repeats a block of code multiple times until a condition is met.Loops help avoid writing the same code again and again.") 
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
                    
                elif select == '2':
                    os.system('cls')
                    print("------------------------------")
                    print("-----------EXAMPLE------------")
                    print("------------------------------")
                    print("Input: \nfor i in range(6):")
                    print("\tprint(i)")         
                    print("Output: \n0\n1\n2\n3\n4\n5")   
                    print("------------------------------")
                    select = input("\nPress (0) to return:")
                    
        
                elif select == '3':
                    os.system('cls')
                    print("------------------------------")
                    print("--------TRY IT YOURSELF-------")                   
                    print("------------------------------")
                    print("Example: \nfor i in range(6):")
                    print("\tprint(i)")           
                    print("------------------------------")
                    print("ENTER twice to run the code")
                    print("------------------------------")
                    print("Try it Yourself:")

                    lines_of_code = []

                    while True:
                        line = input(">>> ")
                        if line.strip() == "": 
                            break
                        lines_of_code.append(line)

                    program_text = "\n".join(lines_of_code)

                    print("\nResult:")
                    try:
                        exec(program_text)
                        print("\nCode executed successfully!")
                    except Exception as e:
                        print("\nThere was an error in your code.")
                        print("Error details:", e)

                    print("-----------------------------")
                    select = input("\nPress (0) to return:")

                
                elif select == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid.")
                    
                    
                    
        #MAIN MENU 0
        elif choice == "0":
            os.system('cls')  
            print(f"EXITING the program. Goodbye, {name}!")
            break


if cont == 'enter':
    main_menu()

