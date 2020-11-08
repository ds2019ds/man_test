import unittest
from random_number_generator import RandomGen

from unittest import mock, TestCase

# TODO when testing the invalid lists, do i need to test for string, float.. seperate cases?
# TODO for the unequal len list test, if i need to customise an exception class LenNotEqualError, then i need to do AssertRaise with this customised exception? arrrrgh long ting...

# TODO is the mock used correctly?

class TestRandomGen(TestCase):
    @mock.patch('random_number_generator.random.random', return_value=0.009)
    def test_next_num_is_neg_one(self, mock_random):
        rand_gen = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        num = rand_gen.next_num()
        self.assertEqual(-1, num)

    @mock.patch('random_number_generator.random.random', return_value=0.02)
    def test_next_num_is_zero(self, mock_random):
        rand_gen = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        num = rand_gen.next_num()
        self.assertEqual(0, num)

    @mock.patch('random_number_generator.random.random', return_value=0.8)
    def test_next_num_is_one(self, mock_random):
        rand_gen = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        num = rand_gen.next_num()
        self.assertEqual(1, num)

    @mock.patch('random_number_generator.random.random', return_value=0.95)
    def test_next_num_is_two(self, mock_random):
        rand_gen = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        num = rand_gen.next_num()
        self.assertEqual(2, num)

    @mock.patch('random_number_generator.random.random', return_value=0.9999)
    def test_next_num_is_three(self, mock_random):
        rand_gen = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
        num = rand_gen.next_num()
        self.assertEqual(3, num)

    def test_invalid_random_num_list(self):
        self.assertRaises(ValueError, RandomGen, [-1, 0, 1, 2, 'not a number'], [0.01, 0.3, 0.58, 0.1, 0.01])

    def test_invalid_probabilities_list(self):
        self.assertRaises(ValueError, RandomGen, [-1, 0, 1, 2, 3], ['not a number', 0.3, 0.58, 0.1, 0.01])

    def test_unequal_len_list(self):
        self.assertRaises(TypeError, RandomGen, [-1, 0, 1, 2, 3, 999], [0.01, 0.3, 0.58, 0.1, 0.01])

if __name__ == '__main__':
    unittest.main()
