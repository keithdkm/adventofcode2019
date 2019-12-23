# read in data
# translate into x/y points
# for each point, calculate gradient and y intercept of straight line 
# to every other point. Count number of unique lines
# That is number of visible asteroids


class MAPS():
    with open('Day_10\\testinput0.txt','r') as f:
        ZERO = f.readlines() 
    with open('Day_10\\testinput1.txt','r') as f:
        ONE = f.readlines() 
    with open('Day_10\\testinput2.txt','r') as f:
        TWO = f.readlines()
    with open('Day_10\\testinput3.txt','r') as f:
        THREE = f.readlines() 
    with open('Day_10\\testinput4.txt','r') as f:
        FOUR = f.readlines() 
    with open('Day_10\\testinput5.txt','r') as f:
        FIVE = f.readlines()     
    with open('Day_10\\testinput6.txt','r') as f:
        SIX = f.readlines() 
    with open('Day_10\\input.txt','r') as f:
        INPUT = f.readlines() 


class AsteroidField():

    def __init__(self,fieldmap):

        self.astlist = self.fetch(fieldmap)

    def __repr__ (self):
         return f'an {self.width} by {self.length} asteroid field  with {len(self.astlist)} asteroids'

    def fetch(self,fieldmap):
        '''
        returns list of coordinates of asteroids and 
        the length and width of the field
        '''
        coord_list =set()
        for i,line in enumerate(fieldmap):
            for j,loc in enumerate(line):
                if loc != '.' and  loc != '\n':
                    coord_list.add(Asteroid(loc,j,i))

        # l = i+1
        # w = j+1

        return sorted(coord_list,key = lambda x:[x.x,x.y])

class Asteroid():
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Asteroid {self.name} at {self.x},{self.y}'

    def vector(self,other):
        '''
        calculates the slope of line between two asteroids
        '''
        if self.y==other.y:
            if self.x==other.x:
                return None
            elif self.x < other.x:
                m = 0.000000000001
                c = self.y
            else: 
                m = -0.000000000001
                c = self.y
            return m,c

        try:
            m = ((self.y - other.y)/abs(self.x - other.x))
            m1 = ((self.y - other.y)/(self.x - other.x))
            c = (self.y-m1*self.x)
        except ZeroDivisionError:
            if self.y > other.y :
                m = float('Inf')
                
                
            else:
                m = float('-Inf')
            c = None

        return m,c
            
Field1 = AsteroidField(MAPS.INPUT)
# print(Field1.astlist)
max_visible = 0
vectors =set()
for i,asteroid in enumerate(Field1.astlist):
        visible = {(asteroid.vector(other_asteroid)) for other_asteroid in Field1.astlist if\
                     asteroid.vector(other_asteroid)!=None}
        # print (i,asteroid,len(visible))
        if len(visible) > max_visible:
            max_visible = len(visible)
            best_asteroid = asteroid
print()
print (f'The best location for the monitoring station is {best_asteroid} with {max_visible} asteroids visible')
print (visible)

