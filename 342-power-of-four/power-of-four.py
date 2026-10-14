class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        power = 1
        while(power<n):
            power *= 4
        return power == n
        