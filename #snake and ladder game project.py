#snake and ladder game project

import random

snakes={16:6, 47:26, 49:11, 95:75, 98:78}
ladders={1:38, 4:14, 9:31, 71:91, 80:100}
def dice():
    return random.randint(1,6)


def playerposition(position,roll):
    newposition=position+roll
    if newposition in snakes:
        print(f'Snake found. You postion is now at {snakes[newposition]}')
        newposition=snakes[newposition]
    elif newposition in ladders:
        print(f'Ladder found. You postion is now at {ladders[newposition]}')
        newposition=ladders[newposition]
    return newposition

def game():
    playerposition1=0
    while playerposition1<100:
        
        input("To roll a dice press Enter  :")
        roll=dice()
        print(f"Your dice says {roll}")
        playerposition1=playerposition(playerposition1,roll)
        print(f"Your current position is at {playerposition1}")
        if playerposition1>=100:
            print("!!! You win !!!")

game()