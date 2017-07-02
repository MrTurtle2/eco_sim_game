'''
Economic Simulation Game
David Buick & Leo Calder-Knight
2017
'''
class Human:
    '''base player and AI class'''
    
    population = 0
    def __init__(self, name, age, health, speed, weight, height, intellect, strength, inventory=[], skills=[], position, dead=False):
        '''name = string
           age = int
           health = int
           speed = int
           weight = int
           intellect = int
           strength = int
           inventory = list of list[item, quantity]
           skills = list of strings/objects
           position = coords [x,y]
           extend me please
        '''
        self.name = name
        self.age = age
        self.health = health 
        self.speed = speed
        self.weight = weight
        self.intellect = intellect
        self.strength = strength
        self.inventory = inventory
        self.skills = skills 
        self.position = position

        Human.population += 1
    
    def take_damage(self, damage):
        '''Human takes damage
        '''
        self.health -= damage
        if self.health <= 0:
            self.dead = True
            Human.population -= 1
    
    def learn_skill(self, skill):
        '''adds a skill
        '''
        self.skills.append(skill)
              
    def move_self(self, new_location):
        '''unsure of movement mechanics
        '''
        old_location = self.location # use to update map
        self.location = new_location
        #implement map update
        
    def get_item(self, item):
        '''picks up item at current location
        '''
        if item in self.inventory:
            i = self.inventory.index(item) 
            self.inventory[i][1] += item[1]
        else:
            self.inventory.append(item)
    
    def drop_item(self, item):
        '''drops item at current location
        '''
        i = self.inventory.index(item)
        current = self.inventory[i]
        quant = current[1]
        if quant < item[1]:
            print(self.name + ' does not have that many ' + item[0])
        else:
            quant -= item[1]
            new = [item[0], quant]
            self.inventory[i] = new
            
    def get_surroundings(self):
        '''returns what is in vision for human
        '''
        