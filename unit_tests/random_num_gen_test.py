import unittest
from random_num_gen import Random_num_gen

class Test_Random_num_gen(unittest.TestCase):

    def setUp(self):
      self.min = 1
      self.max = 2
      self.series_length = 2
      self.rg = Random_num_gen(self.min,self.max)
        

    def test_generate_random_number(self):
        rand_num = self.rg._generate_random_number()
        self.assertTrue((self.min <= rand_num) and (self.max >= rand_num))
    def test_return_random_number_series(self):
       rand_series = self.rg.return_random_number_series( self.series_length) 
       self.assertTrue(len(rand_series) == self.series_length)
         
if __name__ == '__main__':
 unittest.main()
