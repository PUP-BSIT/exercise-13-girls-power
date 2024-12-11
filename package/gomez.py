import os

def menu():
    while True:
        print("Welcome! My name is Ashley Hermione Gomez.")
        print("1. Basic Info")
        print("2. Goals")
        print("[3] Comment from De Leon")
        print("[4] Comment from Esparagoza")
        print("[5] Comment from Alejandro")
        print("[6] Comment from Mosenos")
        choice = input("Choose an option: ")
        
        if choice == "1":
            os.system('cls')
            print("I am Diploma information technology major, and I enjoy programming and playing games.")
        elif choice == "2":
            os.system('cls')
            print("My goal is to become a game developer and contribute to open-source projects.")
        elif choice == '3':
            os.system('cls')
            print ("------ Comment from De Leon ------")
        elif choice == '4':
                os.system('cls')
                print ("------ Comment from Esparagoza ------") 
                print ('Goodluck to your goal')  
        elif choice == '5':
            os.system('cls')
            print ("------ Comment from Alejandro------")
            print ("Hi! That's nice to know. ")
        elif choice == '6':
            os.system('cls')
            print ("------ Comment from Mosenos ------") 
        else:
            print("Invalid choice. Please try again.")