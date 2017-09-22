class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1, n + 1):
            if i % 3 != 0 and i % 5 != 0:
                res.append(str(i))
            if i % 3 == 0 and i % 5 != 0:
                res.append('Fizz')
            if i % 5 == 0 and i % 3 != 0:
                res.append('Buzz')
            if i % 15 == 0:
                res.append('FizzBuzz')

        return res