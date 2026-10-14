class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # for i in range(n):
        #     if n == 2**i:
        #         return True
        # return False
        if n <= 0:
            return False
        power = 1
        while power<n:
            power *= 2
        return power == n
            