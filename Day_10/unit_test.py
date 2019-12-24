from Day_10  import Asteroid, AsteroidField
import unittest
from math import pi,sqrt




class Test_vector(unittest.TestCase):

    def setUp(self):
        self.Origin_asteroid = Asteroid('O',1,1)
        self.asteroid_north = Asteroid('N',1,0)
        self.asteroid_south = Asteroid('S',1,2)
        self.asteroid_west = Asteroid('W',0,1)
        self.asteroid_east = Asteroid('E',2,1)
        self.asteroid_north_east = Asteroid('NE', 2,0)
        self.asteroid_north_west = Asteroid('NW', 0,0)
        self.asteroid_south_east = Asteroid('SE', 2,2)
        self.asteroid_south_west = Asteroid('SW', 0,2)

    def test_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_north),(round(pi*1.5,2),1))
    
    def test_south(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_south), (round(pi*0.5,2),1))

    def test_west(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_west), (round(pi,2),1))
    def test_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_east), (0,1))

    def test_north_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_north_east), (round(pi*1.75,2),round(sqrt(2),2)))

    def test_north_west(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_north_west), (round(pi*1.25,2),round(sqrt(2),2)))

    def test_south_east(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_south_east), (round(pi*0.25,2),round(sqrt(2),2)))

    def test_south_west(self):
        self.assertEqual(self.Origin_asteroid.vector(self.asteroid_south_west), (round(pi*0.75,2),round(sqrt(2),2)))

