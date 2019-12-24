# read in data
# translate into x/y points
# for each point, calculate gradient and y intercept of straight line 
# to every other point. Count number of unique lines
# That is number of visible asteroids
from itertools import count

class MAPS():

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

    def best(self):

    # print(Field.asteroids_l)
        max_visible = 0
        for i,asteroid in enumerate(self.asteroids_l):
                # print(asteroid)
                visible = {(asteroid.vector(other_asteroid)[0]) for other_asteroid in self.asteroids_l if\
                             asteroid.vector(other_asteroid)!=None }
                # print(visible)
                # print (i,asteroid,len(visible))
                if len(visible) > max_visible:
                    max_visible = len(visible)
                    best_asteroid = asteroid

        return best_asteroid,max_visible
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
                
                
    Field = AsteroidField(MAPS.INPUT)

    best_location,visible = Field.best()
            
    print(f'the best asteroid for the detector is {best_location} with {visible} visible asteroids')

