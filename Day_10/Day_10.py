# read in data
# translate into x/y points
# for each point, calculate gradient and y intercept of straight line 
# to every other point. Count number of unique lines
# That is number of visible asteroids
from math import sqrt,atan,pi
from itertools import count
from collections import Counter

class MAPS():

    with open('Day_10\\input.txt','r') as f:
        INPUT = f.readlines() 


class AsteroidField():
    ''' list of all asteroids in field
    '''
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
        max_visible = 0
        for i,asteroid in enumerate(self.asteroids_l):
            visible = set()
            
            for other_asteroid in [a for a in self.asteroids_l if a!=asteroid]:

                vector = asteroid.vector(other_asteroid)
                
                if vector[1]!=0:
                    visible.add(vector[0])
                   

            if len(visible) > max_visible:
                max_visible = len(visible)
                best_asteroid = asteroid
            

        return best_asteroid,max_visible


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
            return 0,0    # asteroid is itself
        
        y = (self.y - other.y)
        x = -(self.x - other.x)
        if y != 0:
            try:
                a =  atan (y/x) / pi
            except ZeroDivisionError:
                if y<0:                    
                    r = 1
                else:
                    r = 0
            else:
                if x>=0 :
                    q = 0.5  # asteroid in first quadrant
                else:
                    q = 1.5  # asteroid in fourth quadrant

                r = q - a
            finally: 
                d = sqrt(y**2+x**2)

        else:    # handles asteroids that are directly east or west
            if self.x > other.x :
                r = 1.5
            else:
                r = 0.5

            d = abs(x)

        r = round(r,4)   # radial psotion of other asteroid in relation to self
        d = round(d,3)   # distance of pther asteroid from self

        return r,d


    # all_asteroids = [(other_asteroid,best_asteroid.vector(other_asteroid)) for other_asteroid in Field.asteroids_l if\
    #          asteroid.vector(other_asteroid)!=None]
    # for asteroid in all_asteroids:
    #     print(asteroid)

    # print (len(all_asteroids))


if __name__ == "__main__":

    Field = AsteroidField(MAPS.INPUT)   #bould field of all asteroids

    best_asteroid,visible_count = Field.best()

    print()
    print('PART ONE')

    print(f'the best asteroid for the detector is {best_asteroid} with {visible_count} visible asteroids')
    
    # print(sorted([(asteroid,best_asteroid.vector(asteroid)) for asteroid in Field.asteroids_l],key=lambda x: x[1][1]))
    asteroid_angles = ([best_asteroid.vector(asteroid)[0] for asteroid in Field.asteroids_l])
    asteroid_lookup = {best_asteroid.vector(asteroid)[0]:asteroid for asteroid in Field.asteroids_l}
    # print(asteroid_lookup)
    asteroid_angles_counts = (Counter(asteroid_angles))
    print(asteroid_lookup[sorted(asteroid_angles_counts.items())[199][0]])
    # asteroid_200 = (sorted(k for k,d in asteroid_distances_counts.items() if d==1)[199])

    # print (f'200th asteroid is {asteroid_lookup[asteroid_200]}')


    # [X] adjust radial postion by a quarter turn
    # [X] invert radial positions so that North is first, then East, south and West
    # [X] start with list of all asteroids sorteed by  their radial position wrt to best satellite and then distance
    # [X] generate counts for each unique radial position (use Counter from collections)
    # loop through, removing 1 from each count, adding the number of lists at the start to the number
    # of asteroids destroyed.
    # If a count is zero, remove it from the list ( or possibly leave it and not count it in above step of count < 0)
    # if asteroids destroyed count>200, fugure out which of the radials contained the 200th. 
    # The number of completed loops - 1 is the index of the asteroid
    # go back to original list and retrieve asteroid coords
    # calcualt output