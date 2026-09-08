class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]: 
            return nums[0]
        if nums[-1] != nums[-2]: 
            return nums[-1]
        while(low <=high):
            mid = (low + high)//2
            if nums[mid] != nums[mid-1] and nums[mid]!= nums[mid+1]:#Direct value no neighbours 
                return nums[mid]
            elif nums[mid] == nums[mid+1]:
                if mid % 2 == 0:#order is correct
                    low = mid + 1
                else:
                    high = mid - 1
            elif nums[mid] == nums[mid-1]:
                if mid % 2 == 1:#order is correct
                    low = mid + 1#if order is correct then the element must be to right
                else:
                    high = mid - 1
                

