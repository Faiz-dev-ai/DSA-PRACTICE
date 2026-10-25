class Solution:
    def countSubsequenceWithTargetSum(self, nums, k):
        #your code goes here
        def generate(index,total):
            #basecase
            if index == len(nums):
                if total == k:
                    return 1
                return 0
            take = generate(index+1,total+nums[index])
            dont_take = generate(index+1,total)
            return take + dont_take
        return generate(0,0)
