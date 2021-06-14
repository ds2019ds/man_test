import random

import itertools
from typing import List
#some changes
class RandomGen(object):

    def __init__(self, random_nums: List[int], probabilities: List[float]):
        """
        constructing random numbers list and probabilities list here, and cummulative weight based on probabilities.
        raise errors if input lists have invalid element type, or unequal length
        """
        self._random_nums = random_nums
        self._probabilities = probabilities

        if not all(isinstance(num, int) for num in self._random_nums):
            raise TypeError('random numbers need to be integers!')

        if not all(isinstance(probability, float) for probability in self._probabilities):
            raise TypeError('probabilities need to be float!')

        if len(self._random_nums) != len(self._probabilities):
            raise ValueError('Random Numbers list and Probabilities list are unequal in length')

        self.cum_weights = list(itertools.accumulate(self._probabilities))


    def next_num(self) -> int:
        """
        Returns one of the randomNums. When this method is called multiple times over a long period,
        it should return the numbers roughly with the initialized probabilities.
        """
        random_num = random.random()
        next_num = self._random_nums[self.locate_num(random_num, self.cum_weights)]
        return next_num

    @staticmethod
    def locate_num(num: float, list_to_search: List[float]) -> float:
        """
        a binary search to locate a number in a sorted list
        """
        lower_bound = 0
        upper_bound = len(list_to_search) - 1

        while lower_bound < upper_bound:
            mid = (lower_bound + upper_bound) // 2
            if num < list_to_search[mid]:
                upper_bound = mid
            else:
                lower_bound = mid + 1

        return lower_bound

if __name__=='__main__':
    rand_gen = RandomGen([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
    print(rand_gen.next_num())
