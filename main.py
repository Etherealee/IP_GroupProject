
#Menu


#Character Damage
import random

def damage(c1, c2):
    dam = 0
    if c1=="Wizard":
        dam -= random.randint(1,10)
    else:
        dam -= random.randint(5,15)
    if c2=="Wizard":
        dam += random.randint(5,20)
    else:
        dam += random.randint(1,10)
    return dam

def defence(c1):
    if c1=="Wizard":
        df = random.randint(1,10)
    else:
        df = random.randint(5,15)
    return df

# Player Team
name1 = input("Enter your team name:")
print('''
-----------------------------
|     Select your team:     |
|1. Wizard - Tanker - Wizard|
|2. Tanker - Wizard - Tanker|
-----------------------------
''')
x=int(input())
if x==1:
    team1 = {"Wizard1":[100,0], "Tanker1":[100,0], "Wizard2":[100,0]}
else:
    team1 = {"Tanker1":[100,0], "Wizard1":[100,0], "Tanker2":[100,0]}

# AI Team
name0 = random.randint(1,90)
name2 = ("AI-",name0)
x = random.randint(1,2)
if x==1:
    team2 = {"Wizard1":[100,0], "Tanker1":[100,0], "Wizard2":[100,0]}
else:
    team2 = {"Tanker1":[100,0], "Wizard1":[100,0], "Tanker2":[100,0]}

