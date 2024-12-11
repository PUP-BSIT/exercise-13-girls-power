import os

def aleck_info():
    while True:
        print ("\nHi! I'm Aleck Mcklaiyre R. Alejandro")
        print("\n---Main Menu ---")
        print("[1] Basic Info")
        print("[2] Goals")
        print("[3] Comment from De Leon")
        print("[4] Comment from Esparagoza")
        print("[5] Comment from Gomez")
        print("[6] Comment from Mosenos")
        print("[7] Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            os.system('cls')
            print ("------ Basic Info ------") 
            print ("Age: 20 years old")
            print ("Birthday: September 03, 2004")       
            print("Year: 2nd Year")
            print("Program: Diploma in Information Technology")      

        elif choice == '2':
            os.system('cls')
            print ("------ Goals ------") 
            print ("1. Graduate with a diploma in Information Technology.")
            print ("2. Obtain a non-professional driver’s license.")

        elif choice == '3':
           os.system('cls')
           print ("------ Comment from De Leon ------")
           print ("Great Work!") 

        elif choice == '4':
            os.system('cls')
            print ("------ Comment from Esparagoza ------") 
            print ("Great Work!")   

        elif choice == '5':
           os.system('cls')
           print ("Great work!") 

        elif choice == '6':
           os.system('cls')
           print ("------ Comment from Mosenos ------") 
           print ("Good job, Aleck!")
           
        elif choice == '7':
            print("\nExiting program.\n")
            break
        else:
            print("\nInvalid option. Please try again.\n")

if __name__ == "__main__":
    aleck_info()