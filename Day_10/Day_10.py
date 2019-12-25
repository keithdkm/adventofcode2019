# read in data
# translate into x/y points
# for each point, calculate gradient and y intercept of straight line 
# to every other point. Count number of unique lines
# That is number of visible asteroids
from math import sqrt,atan,pi
from itertools import count

class MAPS():

    with open('Day_10\\input.txt','r') as f:
        INPUT = f.readlines() 


class AsteroidField():

    def __init__(self,fieldmap):

        self.asteroids_l = self.fetch(fieldmap)

    def __repr__ (self):
         return f'an {self.width} by {self.length} asteroid field  with {len(self.asteroids_l)} asteroids'

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
            visible = set()
            visible_list = []
            for other_asteroid in self.asteroids_l:

                vector = asteroid.vector(other_asteroid)
                
                if vector[1]!=0:
                    visible.add(vector[0])
                # print(visible)
                # print (i,asteroid,len(visible))
            if len(visible) > max_visible:
                max_visible = len(visible)
                best_asteroid = asteroid
            visible_list = sorted(visible_list)
            visible = sorted(visible)

        return (best_asteroid.x,best_asteroid.y),max_visible


class Asteroid():
    _count = count(0)
    def __init__(self,name,x,y):
        self.id = next(self._count)
        self.name = name
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Asteroid {self.id} at {self.x},{self.y}'

    def vector(self,other):
        '''
        calculates the slope of line and distance between two asteroids
        '''
        if self.y==other.y and self.x==other.x:
            return 0,0
        
        y = (self.y - other.y)
        x = -(self.x - other.x)
        if x != 0:
            a =  atan (y/x) / pi
            if x>0  and y>=0 :
                q = 0  # point in first quadrant
            elif x < 0:
                q = 1 # point in second or third quadrants
            else:
                q = 2  # point in fourth quadrant

            r = a + q
            
            d = sqrt(y**2+x**2)
        else:
            if self.y > other.y :
                r = 0.5
            else:
                r = 1.5
           
            d = abs(y)
       
        
        r = round(r,4)
        d = round(d,3)

        return r,d


    # all_asteroids = [(other_asteroid,best_asteroid.vector(other_asteroid)) for other_asteroid in Field.asteroids_l if\
    #          asteroid.vector(other_asteroid)!=None]
    # for asteroid in all_asteroids:
    #     print(asteroid)

    # print (len(all_asteroids))


if __name__ == "__main__":

    Field = AsteroidField(MAPS.INPUT)

    best_location,visible = Field.best()

    print(f'the best asteroid for the detector is {best_location} with {visible} visible asteroids')

    