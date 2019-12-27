from Day_10  import Asteroid, AsteroidField
import unittest
from math import pi,sqrt




class Test_Asteroid_vector(unittest.TestCase):

    def setUp(self):
        self.Origin_asteroid = Asteroid('O',10,10)
        self.asteroid_north = Asteroid('N',10,9)
        self.asteroid_south = Asteroid('S',10,11)
        self.asteroid_west = Asteroid('W',9,10)
        self.asteroid_east = Asteroid('E',11,10)
        self.asteroid_north_east = Asteroid('NE', 11,9)
        self.asteroid_NNE = Asteroid('NNE',11,8)
        self.asteroid_north_west = Asteroid('NW', 9,9)
        self.asteroid_south_east = Asteroid('SE', 11,11)
        self.asteroid_south_west = Asteroid('SW', 9,11)
        self.root2 = round(sqrt(2),3)
        

    def test_north(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_north),(0.0,1))
    
    def test_south(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_south), (1.0,1))

    def test_west(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_west), (1.5,1))

    def test_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_east), (0.5,1))

    def test_north_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_north_east), (0.25,self.root2))
    def test_NNE(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_NNE)[0], 0.1476)

    def test_north_west(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_north_west), (1.75,self.root2))

    def test_south_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_south_east), (0.75,self.root2))

    def test_south_west(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_south_west), (1.25,self.root2))

class Test_final_output_Day10_part1(unittest.TestCase):

    def setUp(self):
        with open('Day_10\\testinput0.txt','r') as f:
            self.ZERO = f.readlines() 
        with open('Day_10\\testinput1.txt','r') as f:
            self.ONE = f.readlines() 
        with open('Day_10\\testinput2.txt','r') as f:
            self.TWO = f.readlines()
        with open('Day_10\\testinput3.txt','r') as f:
            self.THREE = f.readlines() 
        with open('Day_10\\testinput4.txt','r') as f:
            self.FOUR = f.readlines() 
        with open('Day_10\\testinput5.txt','r') as f:
            self.FIVE = f.readlines()     
        with open('Day_10\\testinput6.txt','r') as f:
            self.SIX = f.readlines() 

        self.ER_ZERO = 8
        self.ER_ONE  = 33
        self.ER_TWO =  35
        self.ER_THREE = 41
        self.ER_FOUR = 210


    def test_0(self):
        self.assertEqual(AsteroidField(self.ZERO).best()[1],self.ER_ZERO)
    def test_1(self):
        self.assertEqual(AsteroidField(self.ONE).best()[1],self.ER_ONE)
    def test_2(self):
        self.assertEqual(AsteroidField(self.TWO).best()[1],self.ER_TWO)
    def test_3(self):
        self.assertEqual(AsteroidField(self.THREE).best()[1],self.ER_THREE)
    def test_4(self):
        self.assertEqual(AsteroidField(self.FOUR).best()[1],self.ER_FOUR)

if __name__ == "__main__":
    unittest.main()
