class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        memo={}
        def generate(total):
            if total in memo:
                return memo[total]
            if total == target:
                return 1
            if total>target:
                return 0
            ways = 0
        #generate children 
            for num in nums:
                child_answer = generate(total + num)
                ways += child_answer
            memo[total] = ways
            return ways 
        return generate(0)

            