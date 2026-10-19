class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        result = []
        n = len(nums)
        for i in range(2*n):
            i = i%n
            result.append(nums[i])
        return result