class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        ans = float('inf')
        while(low<=high):
            mid = (low + high)//2
            if nums[low]<=nums[mid]:#check if array is sorted IFYES?
                ans = min(ans,nums[low])#then i know that the arr[low] is smaller and i save that and go to right
                low = mid + 1
            else:
                ans = min(ans,nums[mid])
                high = mid - 1 #go to left to check for the smallest element
        return ans