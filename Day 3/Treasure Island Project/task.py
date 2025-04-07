print(r'''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')
print("⚔️  Welcome, brave soul, to the legendary Treasure Island...")
print("🗺️  Your quest is treacherous, but clear: uncover the lost treasure or be lost to time!\n")
print("Are you ready to start your adventure? Let's go!!!\n")

print("🧭 The path splits before you is a silent crossroad shrouded in mystery.")
answer_one = input("Will you turn left, where whispers echo in the dark… or right, "
                   "where danger may lie in wait? (left/right): \n").lower()

if   answer_one == "left":
    choice_two = input("Congratulations,you made it to the lake. "
                       "There is an island in the middle, are you gonna swim or wait a the boat? "
                       "type 'wait for boat or 'swim' to swim\n").lower()

    if choice_two == "wait":
        choice_three = input("You made it to the island. In the middle of the island there is a house with 3 doors. "
                             "Which door are you choosing? Red, Blue or Yellow?").lower()
        if choice_three == "blue":
            print("Oh no, you just got eaten by a beast. game over. Better luck next time")
        elif choice_three == "red":
            print("Ops, burned by fire. Game over. Better luck next time")
        elif choice_three == "yellow":
            print("You are a winner! Here are some flowers and treasures for you to brighten your day 🌸💐🌼🌷🌹🌺🌻🌞✨")
        else:
            print("Oh no, do you want to give the game another try? Click run again")
    else:
        print("Ops! A trout just swallowed you, game over. Better luck next time!")
else:
    print("You fell into a hole, game over. Better luck next time!")