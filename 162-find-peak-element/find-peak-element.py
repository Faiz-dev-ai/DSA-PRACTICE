class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        while low <= high:
            mid = (low + high) // 2

            left = nums[mid - 1] if mid > 0 else float('-inf')
            right = nums[mid + 1] if mid < len(nums) - 1 else float('-inf')

            if left <= nums[mid] >= right:
                return mid

            elif left > nums[mid]:
                high = mid - 1

            else:
                low = mid + 1