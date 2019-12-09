def fuel(mass):
    fuel_required = int(mass)//3 - 2
    if  fuel_required < 0:
        return 0
    else:
        return fuel_required + fuel(fuel_required)

    

with open('input.txt') as input_:
    res = sum(fuel(m) for m in input_.readlines())
    print(res)
