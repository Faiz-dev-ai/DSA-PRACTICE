class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        total = 0
        min_len = float('inf')
        low = 0
        for high in range(len(nums)):
            total += nums[high]
            while(total >= target):
                length = high - low + 1
                min_len = min(length,min_len)
                total -= nums[low]
                low += 1
            
        return 0 if min_len == float('inf') else min_len