class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        low = 0
        high = 0
        max_length = 0
        zeros = 0
        for high in range(len(nums)):
            if nums[high]==0:
                zeros+=1
            while zeros > 1:
                if nums[low]==0:
                    zeros-=1
                low+=1
            
            max_length = max(max_length,high-low)#we can remove the one from anywhere
        return max_length
            
