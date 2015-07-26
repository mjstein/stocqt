from random import randint

class Random_num_gen():
    def __init__(self, min, max):
        self.min = min
        self.max = max
    def _generate_random_number(self):
      return randint(self.min,self.max)        
    def return_random_number_series(self, series_length):
        random_series=[]
        for i in range(0,series_length):
           random_series.append(self._generate_random_number)
        return random_series
