import random
import itertools

# TODO is the construtor used correctly?
# TODO should i create a new class LenNotEqualError?

# TODO need to add more doc strings!

class RandomGen(object):

    def __init__(self, random_nums, probabilities):
        self._random_nums = random_nums
        self._probabilities = probabilities

        if not all(isinstance(num, int) for num in self._random_nums):
            raise ValueError('random numbers need to be integers!')

        if not all(isinstance(probability, float) for probability in self._probabilities):
            raise ValueError('probabilities need to be float!')

        if len(self._random_nums) != len(self._probabilities):
            raise TypeError('Random Numbers list and Probabilities list are unequal in length')

        self.cum_weights = list(itertools.accumulate(self._probabilities))


    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities.
        """
        random_num = random.random()
        next_num = self._random_nums[self.locate_num(random_num, self.cum_weights)]
        return next_num

    @staticmethod
    def locate_num(num, list_to_search):
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
