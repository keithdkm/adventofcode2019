# Goal given paths for two wires expressed as a list of relative moves orthogonal moves
# calculate the Manhattan distance from the origin to closest point where the wires cross 

# Parse each relative move and add a list of points for that move to a set
# repeat for the next wire 
# 
# run intersection
# return point in intersection set with lowest x+y
from itertools import chain

class Segment():
    REL_MOVE={  'U':(0,1),
                'D':(0,-1),
                'R':(1,0),
                'L':(-1,0)}
    def __init__(self,start,move):
        self.start = start  # segment start point
        self.move = move
        self.direction,self.length = Segment.REL_MOVE[self.move[0]],int(self.move[1:]) #Parse segment
        self.points_list = self.points() 
        self.last_point = self.points_list[-1]

    def __repr__(self):
        return f'Segment starting at {self.start} and ending at {self.points_list[-1]}'

    def points(self):
        '''
        generates a list of points that make up a segment
        '''
        res = []  # output list 
        point = self.start
        for i in range(self.length):
            point = tuple(map(sum,zip(point,self.direction)) )
            res.append(point)
        return res


class Wire():
    '''
    A wire is made up of list of segments. Each segment is a set of points
    '''

    def __init__(self,segment_list):
        self.start = (0,0)  # every wire starts ar origin
        self.num_segments = len(segment_list) # number of segments in Wire
        self.segment_list = segment_list # list of segments
        self.segments = self.build_segments() # creates list of Segments
        self.length = sum(s.length for s in self.segments)
  
        
    def __repr__(self):
        return f'Wire with {self.num_segments} segments and length {self.length}'
    
    def build_segments(self):
        segment_start_point = self.start
        s_list = []
        for s in self.segment_list:
            s_list.append(Segment(segment_start_point,s))
            segment_start_point = s_list[-1].last_point
        return s_list
    
    def all_points(self):
        '''
        returns all the points in a wire
        '''
        return chain.from_iterable(segment.points_list for segment in self.segments)

    def intersections(self,other):
        '''
        Returns all the intersection points with another wire 
        '''

        # add all points from both wires to two sets and return intersection 
        return set(self.all_points()).intersection(set(other.all_points()))

    def distance_from_origin(self,point):
        '''
        returns distance of point along wire.  assumes point is on wire  
        '''
        return list(self.all_points()).index(point)+1


def Manhattan_distance(point):
    '''
    Manhattan distance from origin
    '''
    x,y = point
    return abs(x) + abs(y)


wire_list=[]
with open('Day 3\input-2.txt','r') as f:
    for s_list in f.readlines():   # read file of wires, one line per wire
          segment_list = s_list.strip().split(',') 
          wire_list.append(Wire(segment_list))
           


intersection_points = wire_list[0].intersections(wire_list[1])
least_manhattan_distance = min(Manhattan_distance(point) for point in intersection_points)

print(f'Wire 1 is {wire_list[0].length} steps long')
print(f'The least Manahattan distance is {least_manhattan_distance} steps')

lowest_distance_along_wire = min(wire_list[0].distance_from_origin(point) + wire_list[1].distance_from_origin(point) for point in intersection_points)


print(f'Lowest combined distance to an intersection point is {lowest_distance_along_wire} steps')



