import random

# ● ┌ ─ ┐ │ └ ┘

continueroll = "y"

while continueroll == "y":
    num = random.randint(1, 6)
    
    if num == 1:
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
    
    elif num == 2:
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
    
    elif num == 3:
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
    
    elif num == 4:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
    
    elif num == 5:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
    
    elif num == 6:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")
    
    print("\n") 
    continueroll = input("Press 'y' to roll again, or any other key to quit: ").lower()
    if (input == 'y'):
        pass
    else:
        print("Thank you for playing!")