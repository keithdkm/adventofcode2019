

with open('Day_6\input.txt') as i:
    orbits = [tuple(o.strip().split(')'))for o in i.readlines()]
# build list of all orbits
orbits = sorted(orbits , key = lambda x: x[0])
# print(orbits)

all_planets = set(p for _,p in orbits) # excludes COM
# for each planet, calculate length of path to COM. 
# every planet will have a path and only one path to COM

total_orbits = 0

for planet in all_planets:  # for each unique planet
    next_planet = planet
    while next_planet != 'COM':  # search until at COM is found
        for orbit in orbits: #search through orbits looking for current planet
            if orbit[1] == next_planet: 
                next_planet=orbit[0]
                total_orbits += 1  
                break

print(total_orbits)









