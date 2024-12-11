import os

def menu():
    while True:
        print("Welcome! My name is Ashley Hermione Gomez.")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from De Leon")
        print("4. Comment from Esparagoza")
        print("5. Comment from Alejandro")
        print("6. Comment from Mosenos")
        print("7. Exit")  
        choice = input("Choose an option: ")
        
        if choice == "1":
            os.system('cls')
            print("Nickname: Ash")
            print("Course: Diploma in Information Technology")
        elif choice == "2":
            os.system('cls')
            print("My goal is to become a game developer and contribute to open-source projects.")
        elif choice == '3':
            os.system('cls')
            print("------ Comment from De Leon ------")
            print ("------ Comment from De Leon ------")
            print ("You can do it.")
        elif choice == '4':
            os.system('cls')
            print("------ Comment from Esparagoza ------")   
            print ("------ Comment from Esparagoza ------") 
            print ('Goodluck to your goal')  
        elif choice == '5':
            os.system('cls')
            print("------ Comment from Alejandro ------")
            print ("------ Comment from Alejandro------")
            print ("Hi! That's nice to know. ")
        elif choice == '6':
            os.system('cls')
            print("------ Comment from Mosenos ------")
        elif choice == '7': 
            print("\nExiting program.\n")
            break
            print ("------ Comment from Mosenos ------") 
            print ("Hi, Ashley!") 
        else:
            print("Invalid choice. Please try again.")
