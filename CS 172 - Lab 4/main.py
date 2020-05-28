#Mark Boady and Matthew Burlick
#Drexel University 2020
#CS 172


import random
import time
## TODO: import CustomMonster class here 
from monster import CustomMonster

def driver():
    ## TODO: Get first monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a CustomMonster using that info.
    name1 = input("Enter monster 1 name:")
    health1 = int(input("\nEnter a number for monster 1 health:"))
    description1 = input("\nEnter monster 1 description:")
    bad1 = int(input("\nEnter a number for monster 1 basic attack damage:"))
    sad1 = int(input("\nEnter a number for monster 1 special attack damage:"))
    dad1 = int(input("\nEnter a number for monster 1 defense damage:"))
    badName1 = input("\nEnter monster 1 basic attack name:")
    sadName1 = input("\nEnter monster 1 special attack name:")
    dadName1 = input("\nEnter monster 1 defense name:")
    first = CustomMonster(name1, health1, description1, bad1, sad1, dad1, badName1, sadName1, dadName1)  #this should be an instance of your CustomMonster class
        
    # TODO: Get second monster's name, health, description, basicAttackDamange, specialAttackDamage, defenseDamage, defenseName here.
    # Instantiate a CustomMonster using that info.
    name2 = input("\nEnter monster 2 name:")
    health2 = int(input("\nEnter a number for monster 2 health:"))
    description2 = input("\nEnter monster 2 description:")
    bad2 = int(input("\nEnter a number for monster 2 basic attack damage:"))
    sad2 = int(input("\nEnter a number for monster 2 special attack damage:"))
    dad2 = int(input("\nEnter a number for monster 2 defense damage:"))
    badName2 = input("\nEnter monster 2 basic attack name:")
    sadName2 = input("\nEnter monster 2 special attack name:")
    dadName2 = input("\nEnter monster 2 defense name:")
    second = CustomMonster(name2, health2, description2, bad2, sad2, dad2, badName2, sadName2, dadName2)  #this should be an instance of your CustomMonster class
  
    winner = monster_battle(first,second)

#This function has two monsters fight and returns the winner
def monster_battle(m1, m2):

    #first reset everyone's health!
    #####TODO######
    m1.resetHealth
    m2.resetHealth

    #next print out who is battling
    print("\nStarting Battle Between")
    print(m1.getName()+": "+m1.getDescription())
    print(m2.getName()+": "+m2.getDescription())
    
    
    #Whose turn is it?
    attacker = None
    defender = None
    
    #Select Randomly whether m1 or m2 is the initial attacker
    #to other is the initial definder
    ######TODO######
    rand = random.randint(0,1)
    if rand == 0:
        attacker = m1
        defender = m2
    else :
        attacker = m2
        defender = m1
    
    print(attacker.getName()+" goes first.")
    #Loop until either monster is unconscious (health < 1) or choose to stop.
    while( m1.getHealth() > 0 and m2.getHealth() > 0):
        #Ask the user a move among special attack, basic attack, defense or the stop.
        move = input('Pick one of these (s)pecial attack, (b)asic attack, (d)efense or sto(p):')        

        #It will be nice for output to record the damage done
        before_health=defender.getHealth()
        
        #for each of the options above, apply the appropriate attack and 
        #print out who did what attack on whom
        #basic attack
        if( move.lower() == "b"):
            # Attacker uses basic attack on defender 
            # and print results by calling print_results function
            ######TODO######
            attacker.basicAttack(defender)
            print_results(attacker, defender, attacker.getBasicName(), attacker.getBasicAttackDamage())
        #defense attack
        elif move.lower() == "d":
            # Defend! and print results by calling print_results function
            ######TODO######
            attacker.defenseAttack(defender)
            print_results(attacker, defender, attacker.getDefenseName(), attacker.getDefenseAttackDamage())
        #special attack
        elif move.lower() == "s":
            # Special Attack! and print results by calling print_results function
            ######TODO######
            attacker.specialAttack(defender)
            print_results(attacker, defender, attacker.getSpecialName(), attacker.getSpecialAttackDamage())
        elif move.lower() == "p":
            #stop the fight
            break
        
        #Swap attacker and defender
        ######TODO######
        temp = attacker
        attacker = defender
        defender = temp
        
        #Print the names and healths after this round
        ######TODO######
        nameD = defender.getName()
        healthD = str(defender.getHealth())
        print("{} at {}".format(nameD, healthD))
        
        nameA = attacker.getName()
        healthA = str(attacker.getHealth())
        print("{} at {}".format(nameA, healthA))
                   
    # Print out who won.
    if m1.getHealth() > m2.getHealth():
        print("\nBattle is over. let's see who has won...")
        print("{} is victorious!".format(m1.getName()))
        victor = m1
    else :
        print("\nBattle is over. let's see who has won...")
        print("{} is victorious!".format(m2.getName()))
        victor = m2
        
    # Return who won
    ######TODO######
    return victor

#Print status updates
####TODO####
def print_results(attacker,defender,attack,hchange):
    ####TODO####
    # Get the name of the attacker and the defender.
    # then give status updates based on the the attack. For more
    # info refer to the example trace.
    attackerName = attacker.getName()
    defenderName = defender.getName()
    dmg = str(hchange)
    
    print("{} used {} on {}".format(attackerName, attack, defenderName))
    print("The attack did {} damage.".format(dmg))

#----------------------------------------------------
if __name__=="__main__":
    #Ideally every battle will be different
    #But for reproducability, we'll seed the random number generator as 0
    
    random.seed(0)
    driver()