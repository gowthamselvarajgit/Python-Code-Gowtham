import random

hand_signal = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor: "))
ascii_hand_signal = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
    ]
    
print("YOUR CHOICE")
if hand_signal == 0:
    print("Rock")
    print(ascii_hand_signal[0])
elif hand_signal == 1:
    print("Paper")
    print(ascii_hand_signal[1])
elif hand_signal == 2:
    print("Scissor")
    print(ascii_hand_signal[2])
else:
    print("Enter a correct value.")
    
game_list = ["rock", "paper", "scissor"]
machine_signal = random.randint(0,2)

print("MACHINE CHOICE")
if machine_signal == 0:
    print("Rock")
    print(ascii_hand_signal[0])
elif machine_signal == 1:
    print("Paper")
    print(ascii_hand_signal[1])
else:
    print("Scissor")
    print(ascii_hand_signal[2])

if hand_signal == machine_signal:
    print("Its Draw Play Again")
elif hand_signal == 0 and machine_signal == 2:
    print("You are Winner")
elif hand_signal == 1 and machine_signal == 0:
    print("You are Winner")
elif hand_signal == 2 and machine_signal == 1:
    print("You are Winner")
else:
    print("Machine is Winner")