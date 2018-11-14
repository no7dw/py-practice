import unittest
from prod import ProductionClass 
from mock import MagicMock

class TestT(unittest.TestCase):
    def test_t(self):
        thing = ProductionClass()
        thing.method = MagicMock(return_value=3)
        thing.method(3, 4, 5, key='value')
        thing.method.assert_called_with(3, 4, 5, key='value')
        self.assertEqual(thing.method(), 3)

# if __name__ == '__main__':
#     unittest.main()

