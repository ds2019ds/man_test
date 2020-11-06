import unittest
from random_number_generator import RandomGen

from unittest import mock, TestCase

#somehting
class TestRandomGen(TestCase):
    @mock.patch('random_number_generator.random.random', return_value=0.9)
    def test_next_num(self, mock_random):
        ob = RandomGen()
        num = ob.next_num()
        self.assertEqual(2, num)


if __name__ == '__main__':
    unittest.main()
