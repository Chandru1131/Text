def intro():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark room. There are two doors.")
    choice = input("Do you go through door 1 or door 2? ")

    if choice == "1":
        door_1()
    elif choice == "2":
        door_2()
    else:
        print("Invalid choice. Please choose 1 or 2.")
        intro()

def door_1():
    print("You enter a room filled with treasure. Congratulations, you won!")
    
def door_2():
    print("You enter a room with a dragon. Unfortunately, you were defeated.")
    retry = input("Do you want to try again? (yes/no): ")
    if retry.lower() == "yes":
        intro()
    else:
        print("Game Over!")

# Start the game
intro()
