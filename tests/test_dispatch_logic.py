import unittest
from hustle_mode.yield_optimizer import check_profitability

class TestDispatchLogic(unittest.TestCase):
    def test_profitable_ride(self):
        self.assertTrue(check_profitability(ride_cost=20.00, energy_cost=5.00))

if __name__ == '__main__':
    unittest.main()
  
