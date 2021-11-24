import unittest
# from sdk.main import get_money2,get_money1
from sdk.main import *
from sdk.subf import util
class TestABC(unittest.TestCase):
    def test_get_money2(self):
        result = get_money2('abc')
        self.assertTrue(result == 'abc'+'2' )
    def test_get_money1(self):
        result = get_money1('abc')
        self.assertTrue(result == 'abc'+'1' )    
    def test_date(self):
        s= util.get_date()
        import datetime
        self.assertTrue(type(s)== datetime.datetime)
