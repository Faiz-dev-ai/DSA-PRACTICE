class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ones = 0
        low = 0
        high = 0
        zeros = 0
        for high in range(len(nums)):
            if nums[high] == 0:
                zeros += 1
            while zeros>k:
                if nums[low] == 0:
                    zeros -= 1
                low += 1
            max_ones = max(max_ones,high-low+1)
        return max_ones



        