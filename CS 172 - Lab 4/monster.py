#Mark Boady and Matthew Burlick
#Drexel University 2020
#CS 172


#This class defines a generic monster
#It doesn't actually DO anything.
#It just gives you a template for how a monster works.

#We can make any number of monsters and have them fight
#they just all need to INHERIT from this one so that work the same way

#Since this class is not intended to be used
#none of the methods do anything
#This class is cannot be used by itself.
from abc import ABC, abstractmethod

### DO NOT CHANGE ANYTHING BELOW IN THIS monster CLASS ####
class Monster(ABC):

    #Methods that need to be implemented
    #The description is printed at the start to give additional details
    
    #The constructor. In order for parameters to have whatever name they want they must be provide in the order shown.
    #The parameters are (in this order, with their expected type in parenthesis):
    
    #n (str) is the name
    #health (int) is the starting health of the monster
    #description (str) 
    #basicAttackDamage (int)
    #specialAttackDamage (int)
    #defenseDamage (int)
    #basicAttackName (str)
    #specialAttackName (str)
    #defenseName
    @abstractmethod
    def __init__(self,name, health=100, description = 'Fast and Furious Fur Ball', basicAttackDamage=7, specialAttackDamage=10, defenseDamage=1, basicAttackName='scratch', specialAttackName='special scratch', defenseName='duck'):
        pass
        
    #String representation of the Monster.
    @abstractmethod 
    def __str__(self):
        pass
        
    #Name the monster we are fighting
    #The description is printed at the start to give
    #additional details
    @abstractmethod 
    def getName(self):
        pass
        
    @abstractmethod
    def getDescription(self):
        pass
        
    #Basic Attack Move
    #This will be the most common attack the monster makes
    #You are passed the monster you are fighting
    @abstractmethod 
    def basicAttack(self,enemy):
        pass
    
    #Print the name of the attack used
    @abstractmethod 
    def getBasicName(self):
        pass
    #Get the basic attack damage amount.
    @abstractmethod
    def getBasicAttackDamage(self):
        pass
    
    #Defense Move
    #This move is used less frequently to
    #let the monster defend itself
    @abstractmethod 
    def defenseAttack(self,enemy):
        pass
        
    #Print out the name of the attack used
    @abstractmethod 
    def getDefenseName(self):
        pass
    #Get the defnse attack damage amount
    @abstractmethod
    def getDefenseAttackDamage(self):
        pass
        
    #Special Attack
    #This move is used less frequently
    #but is the most powerful move the monster has
    @abstractmethod 
    def specialAttack(self,enemy):
        pass
        
    #get the special attack's name
    @abstractmethod 
    def getSpecialName(self):
        pass
    
    #get the special attack damage amount
    @abstractmethod
    def getSpecialAttackDamage(self):
        pass    
    
    #Health Management
    #A monster at health <= 0 is unconscious
    #This returns the current health level
    @abstractmethod 
    def getHealth(self):
        pass
    
    #This returns the maximum health set at creation.
    @abstractmethod
    def getMaximumHealth(self):
        pass
    #This function is used by the other monster to
    #either do damage (positive int) or heal (negative int)
    @abstractmethod 
    def doDamage(self,damage):
        pass
        
    #Reset Health for next match
    @abstractmethod 
    def resetHealth(self):
        pass
### DO NOT CHANGE ANYTHING ABOVE IN THIS monster CLASS ####


## TODO: Create a CustomMonster class that inherits the generic monster class.
class CustomMonster(Monster):
    def __init__(self, n, health=100, description = 'Fast and Furious Fur Ball', basicAttackDamage=7, specialAttackDamage=10, defenseDamage=1, basicAttackName='scratch', specialAttackName='special scratch', basicDefenseName='duck'):
        self.__name = n
        self.__maximumHealth = int(health)
        self.__health = int(health)
        self.__description = description
        self.__basicAttackDamage = basicAttackDamage
        self.__specialAttackDamage = specialAttackDamage
        self.__defenseDamage = defenseDamage
        self.__basicAttackName = basicAttackName
        self.__specialAttackName = specialAttackName
        self.__basicDefenseName = basicDefenseName
        
    def __str__(self):
        return "{}".format(self.__description)
    
    def getName(self):
        return "{}".format(self.__name)
    
    def getDescription(self):
        return "{}".format(self.__description)
    
    def getBasicName(self):
        return "{}".format(self.__basicAttackName)
    
    def getBasicAttackDamage(self):
        return self.__basicAttackDamage
    
    def getDefenseName(self):
        return "{}".format(self.__basicDefenseName)
    
    def getDefenseAttackDamage(self):
        return self.__defenseDamage
    
    def getSpecialName(self):
        return "{}".format(self.__specialAttackName)
    
    def getSpecialAttackDamage(self):
        return self.__specialAttackDamage
    
    def getHealth(self):
        return self.__health
    
    def getMaximumHealth(self):
        return self.__maximumHealth
    
    def doDamage(self, damage):
        self.__health = self.__health - damage
        
    def basicAttack(self, enemy):
        enemy.doDamage(self.getBasicAttackDamage())
    
    def defenseAttack(self, enemy):
        enemy.doDamage(self.getDefenseAttackDamage())
    
    def specialAttack(self, enemy):
        enemy.doDamage(self.getSpecialAttackDamage())
        
    def resetHealth(self):
        self.__health = self.__maximumHealth
