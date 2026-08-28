class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                k = i
                break
        if k == -1:#if the array given has non zeros dont do anything just return
            return
        i = k
        for j in range(i+1,len(nums)):
            if nums[j]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        
        