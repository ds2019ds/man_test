import unittest
from random_number_generator import RandomGen

from unittest import mock, TestCase

#TODO is the mock used correctly?
#TODO is it enough?
#TODO maybe the naming conventions are not good enough?
class TestRandomGen(TestCase):
    @mock.patch('random_number_generator.random.random', return_value=0.9)
    def test_next_num(self, mock_random):
        ob = RandomGen()
        num = ob.next_num()
        self.assertEqual(2, num)


if __name__ == '__main__':
    unittest.main()
