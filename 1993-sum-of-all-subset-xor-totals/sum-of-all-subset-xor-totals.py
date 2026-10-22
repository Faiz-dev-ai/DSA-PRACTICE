class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def generate(index,xor_total):
            #base case
            if index == len(nums):
                return xor_total
            #if we take element 
            take = generate(index+1,xor_total^nums[index])
            dont_take = generate(index+1,xor_total)
            return take + dont_take
        return generate(0,0)
