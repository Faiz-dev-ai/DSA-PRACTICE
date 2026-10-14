class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #using the brute force method 
        # for i in range(n):
        #     if n == 3 ** i:
        #         return True
        # return False
        #OPTIMAL WAY 
        if n<=0:
            return False
        power = 1
        while(power<n):
            power *= 3
        #     if power == n:
        #         return True
        # return False
        return power == n
