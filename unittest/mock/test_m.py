import unittest
from prod import ProductionClass 
from mock import MagicMock

class TestT(unittest.TestCase):
    def test_t(self):
        thing = ProductionClass()
        thing.func1 = MagicMock(return_value=3)
        thing.func1(3, 4, 5, key='value')
        thing.func1.assert_called_with(3, 4, 5, key='value')
        self.assertEqual(thing.func1(), 3)

if __name__ == '__main__':
    unittest.main()

