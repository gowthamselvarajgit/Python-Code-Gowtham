print("WELCOME TO TREASURE ISLAND ☻")
print("Your mission is to find the treasure.")

# Normalize input to lowercase for easier checks
direction = input('You\'re at a crossroad. Type "left" or "right": ').lower()

if direction == "right":
    print("You are now at a lake. The treasure island is in the middle of the lake.")
    way_to_travel = input('Type "wait" to wait for a boat or "swim" to swim across: ').lower()
    
    if way_to_travel == "wait":
        print("You arrive safely at the island. There are three doors: one blue, one red, and one yellow.")
        door = input('Which door do you choose? Type "red", "blue", or "yellow": ').lower()
        
        if door == "yellow":
            print("You open the door... and find the treasure! You Win ☻")
        elif door == "red" or door == "blue":
            print("Oops! Dangerous traps behind this door. Game Over ☹")
        else:
            print("Invalid choice. Game Over ☹")
    else:
        print("You tried to swim across but got eaten by crocodiles. Game Over ☹")
else:
    print("You fell into a hole. Game Over ☹")
