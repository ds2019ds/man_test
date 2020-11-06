import random
import itertools

class RandomGen(object):
    # Values that may be returned by next_num()
    _random_nums = [-1, 0, 1, 2, 3]
    # _random_nums = [1,1,1,1,1]
    # Probability of the occurence of random_nums
    _probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    def next_num(self):
        """
        Returns one of the randomNums. When this method is called multiple times over a long period, it should return the numbers roughly with the initialized probabilities.
        """
        random_num = random.random()
        cum_weights = list(itertools.accumulate(self._probabilities))
        next_num = self._random_nums[self.locate_num(random_num, cum_weights)]
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
    ob = RandomGen()
    print(ob.next_num())
