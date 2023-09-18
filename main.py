"""
CMPS 6100  Lab 2
Author: Tiancheng.Xu
"""
import random
print("Game Start")
f = open("Space Station.txt","rt")
content = f.readlines()
Room_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Map = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Monster = random.choice(Room_list)
Portkey = random.choice(Room_list)

Room_dict = {0:[1,2,3,4],
             1:[0,5],
             2:[0,6],
             3:[0,7],
             4:[0,8],
             5:[1,13,14],
             6:[2],
             7:[3,15,16],
             8:[4],
             9:[13],
             10:[14],
             11:[15],
             12:[16],
             13:[5,9],
             14:[5,10],
             15:[7,11],
             16:[7,12]}

def player_move(num):
    print(content[num + 2])
    print("Rooms adjacent to the current room are: ")
    print(Room_dict.get(num))
    while True:
        try:
            next_room = int(input("Choose the next room you want to explore: "))
            if next_room in Room_dict.get(num):
                return next_room
            else:
                print("You cannot go there now, please choose again: ")
        except ValueError:
            print("Invalid input, please enter a valid number.")           
    
def monster_move(num):
    next_move = random.choice(Room_dict.get(num))   
    return next_move 

player_initial = player_move(0)
monster_initial = Monster

player_hp = 100
monster_hp = 100
player_attack = {1:'1.Laser gun',
                 2:'2.Blast grenade',
                 3:'3.reckless blade'}


def battle(hp1,hp2):
    while True:
        print("Your HP:{}".format(hp1))
        print("Monster HP:{}".format(hp2))
        for value in player_attack.values():
            print(value)
        try:
            attack = int(input("Choose your attack move: "))
            if attack in [1,2,3]:
                if attack == 1:
                    print("You shoot the monster using laser gun, deal 10 damage.")
                    hp2 = hp2-10
                elif attack == 2:
                    print("You throw a blase grenade, deal 25 damage to ghost, but deal 5 damage to yourself.")
                    hp1 = hp1-5
                    hp2 = hp2-25
                elif attack ==3:
                    factor = random.uniform(0,1)
                    if factor >= 0.5:
                        print("You slash the monster recklessly, deal 35 damage.")
                        hp2 = hp2-35
                    elif factor <0.5:
                        print("You miss it!!!")
                        hp2 = hp2-0
        except ValueError: 
            print("Invalid input, please enter a valid number.")  
        if hp2 <= 0:
            print("You defeat the monster!")
            return True
        monster_attack = random.choice([1,2])
        if monster_attack ==1:
            print("The monster hits you by its huge claw, deal 15 damage.")
            hp1 = hp1-15
        elif monster_attack ==2:
            print("The monster bites you by its bloody fang, deal 10 damage and restore 10 HP.")
            if hp2 <= 50:
                hp1 = hp1-10
                hp2 = hp2+10
            else:
                hp1 = hp1-10
        if hp1 <= 0:
            print("You are killed. You lose.")
            return False
        
                    
        
Battle_checking = False
Portkey_checking = False
print(Portkey)
while True:
    player_initial = player_move(player_initial)
    monster_initial = monster_move(monster_initial)
    if player_initial == Portkey:
        Portkey_checking = True
        if Battle_checking == True:
            print("You can finally escape safely. You win!")
            break
        elif Battle_checking == False:
            print("You find the portkey! However, the monster is still chasing you! You have to defeat it ti escape!")
    elif player_initial == monster_initial and Battle_checking == False:
        print("You encounter the monster!. Prepare yourslef for a tough fight!")
        Battle_result = battle(player_hp,monster_hp)
        if Battle_result == False:
            break
        elif Battle_result == True:
            Battle_checking = True

f.close