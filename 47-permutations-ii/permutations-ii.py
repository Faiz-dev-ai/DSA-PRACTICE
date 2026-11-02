class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        answer = []
        hashy = {}
        seen = set()
        def generate(current):
            if len(current) == len(nums):
                key = tuple(current)
                if key not in hashy:
                    hashy[key] = True
                    answer.append(current.copy())
                return
            #generating children
            for i in range(len(nums)):
                if i in seen:
                    continue
                #if i dont see 'i' in the seen we need to add that index we currently on in seen and add that element to the curret
                seen.add(i)
                current.append(nums[i])
                generate(current)
                #backtrack
                current.pop()
                seen.remove(i)
        generate([])
        return answer
                

