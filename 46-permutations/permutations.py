class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        answer = []
        used = [False]*len(nums)
        def generate(current):
            if len(current) == len(nums):
                answer.append(current.copy())
                return
            #generating the children
            for i in range(len(nums)):
                if used[i]:
                    continue
                current.append(nums[i])
                used[i] = True
                generate(current)
                current.pop()
                used[i] = False
            return answer
        return generate([])
        

