# read in orbit
# split tuples
# order tuples by first planet
# 

with open('Day_6\input.txt') as i:
    orbits = [tuple(o.strip().split(')'))for o in i.readlines()]

orbits = sorted(orbits , key = lambda x: x[0])
print(orbits)
class Planet():
    
    def __init__(self,name):
        self.name = name
        self.orbited_by = self.fetch_orbits_(orbits)
 

    def fetch_orbits_(self,orbit_list):
        return [Planet(p2) for (p1,p2) in orbit_list if p1==self.name]

    def __repr__(self):
        return f'Planet {self.name} orbited by {self.orbited_by}'
    
    def orbit_count(self):
        '''
        fetches all orbits for this planet
        '''
        return len(self.orbited_by) + sum(p.orbit_count() for p in self.orbited_by)

    def all_orbits(self):
        '''
        sums all the orbits for all the planets orbiting this one
        '''
        return self.orbit_count() + sum(p.all_orbits() for p in self.orbited_by)


COM = Planet('COM')
print (COM)
print (COM.all_orbits())