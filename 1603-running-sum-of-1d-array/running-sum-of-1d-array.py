class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        answer = []
        for i in range(len(nums)):
            total = 0
            for j in range(0,i+1):
                total += nums[j]
            answer.append(total)
        return answer
