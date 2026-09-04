class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        # The Fix: Shift this line all the way to the left, outside the loop!
        return low