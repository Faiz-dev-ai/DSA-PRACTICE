class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_ind = 0
        neg_ind = 1
        result = [0]*len(nums)
        for num in nums:
            if num > 0:
                result[pos_ind] = num
                pos_ind += 2
            if num < 0:
                result[neg_ind] = num
                neg_ind += 2
        return result