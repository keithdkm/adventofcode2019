from itertools import combinations
from operator import mul
class Planet():
    def __init__(self,name, moons):
        self.name = name
        self.moons = {moon[0]:Moon(*moon) for moon in moons}
        self.all_coord_groups = [set(),set(),set()]


    def __repr__(self):
        return f'''Planet {self.name} with  {[v for v in self.moons.values()]} '''

    
    def move_moons(self):
        ''' performs velocity calculations based on relative positions of each pair of moons
        then updates moon positions once all moon velocities have been adjusted
        '''

        def set_new_moon_velocities(m1,m2):
            def velocity_change(p1,p2):
                if p1>p2:
                    return -1
                elif p1<p2:
                    return 1
                else:
                    return 0

            moon_velocity_changes = [velocity_change(p1,p2) for p1,p2 in zip(m1.position,m2.position)]
            m1.set_velocity(moon_velocity_changes,add = True)
            m2.set_velocity(moon_velocity_changes,add = False)

        # update moon velocities based on relative positions
        moon_combinations = combinations( self.moons.values(),2)
        for m1,m2 in moon_combinations:
            set_new_moon_velocities(m1,m2)

        # update moon positions based upon new velocities
        for moon in self.moons.values():
            moon.set_position()
       
class Moon():
    def __init__(self,name,coords):
        self.name = name
        self.position = coords
        self.velocity = (0,0,0)
        self.orbit = 0
        self.position_over_time = [self.position]
        self.vel_over_time = []
        # self.pot_energy_over_time = []
        # self.kin_energy_over_time = []

    def __repr__(self):
        return f''' Moon {self.name:10s}: \
pos=<x={self.position[0]:3d}, y={self.position[1]:3d}, z={self.position[2]:3d}>, \
vel=<x={self.velocity[0]:3d}, y={self.velocity[1]:3d}, z={self.velocity[2]:3d}>'''

    
    def set_velocity(self,changes,add):
        self.velocity = tuple(v+c if add else v-c for v,c in zip(self.velocity,changes))
    
    def set_position(self):
        self.position = tuple(position+velocity for position,velocity in zip(self.position,self.velocity))
                                                                  # and can be recorded
    
    @property
    def pot_energy(self):
        return sum(abs(c) for c in self.position)

    @property
    def kin_energy(self):
        return sum(abs(v) for v in self.velocity)
    

def run_simulation(planet, max_sims=10000):
    # print('Starting Condition')
    # for moon in planet.moons.values():
    #     print(moon)

    new_coord_groups = list(zip(*[ m.position for m in planet.moons.values()]))  # record
    periods = 0
    found_periods = {0:[],1:[],2:[]}
    while  any(len(f)<2 for f in found_periods.values()) and periods < max_sims:  # keep running simulation until period is established for each coord
    
        periods += 1
        
        # print(periods)
        # search each set of x, y and z coords, looking for two periods where the values for a 
        # particular coord don't change. record period  and the coord values.
        # then search again looking for the next pairing with the
        # same value.  Keep running sim until all three periods have been determined ie two pairs 
        # values are found. Period of each axis is twice this number. Answer is LCM of the three numbers

        # TODO separate each coord periodicity to b calcualted sepaarately
        old_coord_groups = new_coord_groups  # save old moon positions
        planet.move_moons()     # move moons to next position
        new_coord_groups = list(zip(*[ m.position for m in planet.moons.values()]))  
            # separates the coords into ((x1,x2,x3,x4),(y1,y2,y3,y4),(z1,..)
        for i,(o,n) in enumerate(zip(old_coord_groups,new_coord_groups)): # are any of the coord
            if o==n:
               found_periods[i].append(periods)
            #    print(found_periods)
            # if periods%100==0:
            #     print(found_periods)
            
    pattern_repeats_after = 1
    for a in ():
        pattern_repeats_after *= a[1]-a[0]

    return([p[1]-p[0] for p in found_periods.values()])

def _gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def _lcm(x, y):
    lcm = (x*y)//_gcd(x,y)
    return lcm

if __name__ == '__main__':

    with open('Day_12\\input.txt','r') as f:
        moon_data = [(c[0],(int(c[1]),int(c[2]),int(c[3]))) for c in ((m.strip().split(',')) for m in f.readlines())]


    
    Jupiter = Planet('Jupiter',moon_data)
    sim_result = run_simulation(Jupiter,1000000)


    print(f'Moon periodicities are  {sim_result}')
    print(_lcm(_lcm(sim_result[0]*2,sim_result[1]*2),sim_result[2]*2))

    

