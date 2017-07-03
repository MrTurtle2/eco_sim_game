'''
Economic Simulation Game
David Buick & Leo Calder-Knight
2017
'''
class Human:
    '''base player and AI class'''
    
    population = 0
    def __init__(self, name, age, health, thirst, hunger, vitamin, energy, vision, hearing, agility, dexterity, intellect, strength, weight, height, location=[0,0], inventory=[], skills=[], dead=False):
        '''name = string
           age = int
           health = int (hit points)
           speed = int (general move speed determined by other attributes(equation pls))
           weight = int 
           intellect = int
           strength = int (carring capacity + manipulation)
           agility = int (reduces effect of rough terrain)
           dexterity = int (manipultion)
           vision = int (fov)
           hearing = int (sound fall off)
           vitamin = int (essential nutrient level)
           hunger = int (protein)
           energy = int (sugars + polymers)
           exposure = int (determined by location/surroundings)
           inventory = list of list['item', quantity]
           skills = list of strings/objects
           location = coords [x,y]
           extend me please
        '''
        self.name = name
        self.age = age
        self.health = health
        self.thirst = thirst
        self.vitamin = vitamin
        self.hunger = hunger        
        self.energy = energy
        self.vision = vision
        self.hearing = hearing        
        self.agility = agility        
        self.intellect = intellect
        self.strength = strength
        self.speed = self.get_speed() # determined by other attributes
        self.weight = weight
        self.height = height
        self.location = location
        self.inventory = inventory
        self.skills = skills 
        self.exposure = self.get_exposure() # determined by surroundings
        self.coretemp = 3650 #36.50 can add more s.f.

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
    
    def get_speed(self):
        '''updates human speed (wip)
        '''
    
    def get_exposure(self):
        '''updates exposure (wip)
        '''
        
        
person = Human('name', 20, 100, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 80, 180)     
        
        
        
    