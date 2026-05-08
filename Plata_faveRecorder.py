def read_file(filename):
    try:
       with open(filename, "r") as file:
            content = file.read()
            if content.strip() == "":
             print("Dream Big: I want to become a skilled programmer who builds system that help people.Stay Curious: I will keep learning even when things get difficult.Embrace Failure: Every error is a step closer to success.Create Impact: I want my code to solve real-world problems.Be Consistent: Small progress every day leads to big results.Believe in Yourself: I am capable of learning and growing.Someday we will be free")
            else:
                print("\n--- Inspiring Messages ---")
                print(content)
    except FileNotFoundError:
        print("\nFile not found. Make sure dreams.txt exists.\n")


def add_message(filename):
    message = input("\nEnter your inspiring message: ")
    with open(filename, "a") as file:
        file.write(message + "\n")
    print("\nMessage added successfully!\n")


def rewrite_file(filename):
    confirm = input("\nAre you sure you want to overwrite the file? (yes/no): ").lower()
    
    if confirm == "yes":
        print("\nEnter new messages (type 'END' on a new line to finish):")
        new_content = []
        
        while True:
            line = input()
            if line.upper() == "END":
                break
            new_content.append(line)
        
        with open(filename, "w") as file:
            for line in new_content:
                file.write(line + "\n")
        
        print("\nFile successfully overwritten!\n")
    else:
        print("\nRewrite cancelled.\n")


def menu():
    filename = "dreams.txt"
    
    while True:
        print("==== Dreams File Manager ====")
        print("1. Read inspiring messages")
        print("2. Add a new inspiring message")
        print("3. Rewrite the entire file")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            read_file(filename)
        elif choice == "2":
            add_message(filename)
        elif choice == "3":
            rewrite_file(filename)
        elif choice == "4":
            print("\nExiting program. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.\n")


menu()