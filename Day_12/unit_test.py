import Day_12  
import unittest




class Test_final_output_Day12_part1(unittest.TestCase):

    def setUp(self):
        with open('Day_12\\Test1.txt','r') as f:
             
            moon_data = [(c[0],(int(c[1]),int(c[2]),int(c[3]))) for c in ((m.strip().split(',')) for m in f.readlines())]
            self.Saturn  = Day_12.Planet("Saturn",moon_data )
            print(self.Saturn)

        with open('Day_12\\Test2.txt','r') as f:
            moon_data = [(c[0],(int(c[1]),int(c[2]),int(c[3]))) for c in ((m.strip().split(',')) for m in f.readlines())]
            self.Venus  = Day_12.Planet("Venus",moon_data )
            print(self.Venus)
          
        

        self.ER_ONE = 179
        self.ER_TWO  = 1940
        self.ER_THREE = 2772


    # def test_1(self):
    #     self.assertEqual(Day_12.run_simulation(self.Saturn,10),self.ER_ONE)
    # def test_2(self):
    #     self.assertEqual(Day_12.run_simulation(self.Venus,100),self.ER_TWO)

    def test_part2_t1(self):
        self.assertEqual(Day_12.run_simulation(self.Saturn,5000),2772)

    def test_part2_t2(self):
        self.assertEqual(Day_12.run_simulation(self.Venus,100000),4686774924)
   

if __name__ == "__main__":
    unittest.main()
