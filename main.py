#Menu


#Damage
import random

def damage(c1, c2):
    dam = 0
    if c1=="Soldier":
        dam -= random.randint(1,10)
    else:
        dam -= random.randint(5,15)
    if c2=="Soldier":
        dam += random.randint(5,20)
    else:
        dam += random.randint(1,10)
    return dam

def defence(c1):
    if c1=="Soldier":
        df = random.randint(1,10)
    else:
        df = random.randint(5,15)
    return df

# Player Team
name1 = input("Enter your team name:")
print('''
-------------------------------
|      Select your team:      |
|1. Soldier - Tanker - Soldier|
|2. Tanker - Soldier - Tanker |
-------------------------------
''')
x=int(input())
if x==1:
    team1 = {"Soldier1":[100,0], "Tanker1":[100,0], "Soldier2":[100,0]}
else:
    team1 = {"Tanker1":[100,0], "Soldier1":[100,0], "Tanker2":[100,0]}

# AI Team
AI = ("AI")
name2 = (AI,random.randint(1,90))
x = random.randint(1,2)
if x==1:
    team2 = {"Soldier1":[100,0], "Tanker1":[100,0], "Soldier2":[100,0]}
else:
    team2 = {"Tanker1":[100,0], "Soldier1":[100,0], "Tanker2":[100,0]}

# Game
turn = 1
while team1 and team2:
    print("\n\nPlayer List:")
    print("Team 1:",name1)
    print(team1)
    print("Team 2:",name2)
    print(team2)

    if turn%2:
        print("\n\nHere's your turn:")
        print("Select the local unit you want to attack\n",name2)
        for player in team2:
            print(player,end="  ")
        print()
        target = input("Target: ")
        print("Choose our attacking soldier:\n",name1)
        for player in team1:
            print(player,end="  ")
        print()
        attacker = input("Attacker: ")
        d = damage(target[:-1], attacker[:-1])
        team2[target][0]-=d
        team2[target][1]+= defence(target[:-1])
        team1[attacker][1] += d
        if d>10:
            team1[attacker][1] += int(d/5)
            team2[target][1] += int(d/5)
        elif d<=0:
            team1[attacker][1] += int(d/2)
            team2[target][1] += int(d/2)
        if team2[target][0] <= 0:
            team2.pop(target)
    else:    # AI's turn
        print("\n\nAI's TURN:")
        print("Enter who you want to attack:\n",name1)
        for player in team1:
            print(player,end="  ")
        print()
        target = random.choice(list(team1.keys()))
        print(name2,"will attack :",target)
        print("Choose an attacker:\n",name2)
        for player in team1:
            print(player,end="  ")
        print()
        attacker = random.choice(list(team2.keys()))
        print(name2,"will attack :",attacker)
        d = damage(target[:-1], attacker[:-1])
        team1[target][0]-=d
        team1[target][1]+= defence(target[:-1])
        team2[attacker][1] += d
        if d>10:
            team2[attacker][1] += int(d/5)
            team1[target][1] += int(d/5)
        elif d<=0:
            team2[attacker][1] += int(d/2)
            team1[target][1] += int(d/2)
        if team1[target][0]<=0:
            team1.pop(target)
    turn += 1

# Printing the final scoreboard
print("Final Scoreboard:")
