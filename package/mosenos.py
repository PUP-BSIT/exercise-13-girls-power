import os

def info():
    print("Name: Loise Nicole")
    print("Year: 2nd Year")
    print("Program: Diploma in Information Technology")

def goals():
    print("Goal #1: To graduate")

def mosenos_info():
    while True:
        print("---Loise Menu---")
        print("1. Basic Info")
        print("2. Goals")
        print("3. Comment from Teamate 1")
        print("4. Comment from Teamate 2")
        print("5. Comment from Teamate 3")
        print("6. Comment from Teamate 4")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 7:
            break

        match choice:
            case 1:
                os.system('cls')
                print("----Basic Info----")

                info()

                input("\nPress Enter to continue...")

            case 2:
                os.system('cls')
                print("----Goals----")

                goals()

                input("\nPress Enter to continue...")

            case 3:
                os.system('cls')
                print("----Comment from teamate 1----")
                print(" ")
                print("Hi! that is a very simple and realistic goal. Good luck!")
                print("- Aleck")
                
            case 4:
                os.system('cls')
                print("----Comment from teamate----")
                print("Good luck on your goal! ")

            case 5:
                os.system('cls')
                print("----Comment from teamate----")
                print(" ")
                print("great job")

            case 6:
                os.system('cls')
                print("----Comment from teamate----")
                print(" ")
                print("Super Good work!")

