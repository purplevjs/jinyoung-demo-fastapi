import unittest
import pandas as pd
from LifeExpectancy import load_lifeExpectancy_data

class TestLifeExpectancyData(unittest.TestCase):

    def test_load_lifeExpectancy_data():
        life = load_lifeExpectancy_data()
        self.assertIsNotFalse(life) # type: ignore
        if life is not None:
            self.assertFalse(life.empty) # type: ignore

if __name__ == '__main__':
    unittest.main()
