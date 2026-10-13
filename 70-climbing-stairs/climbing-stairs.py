class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def climb(n):
            if n <= 1:
                return 1

            # Already calculated? Reuse it
            if n in memo:
                return memo[n]

            # Calculate
            answer = climb(n - 1) + climb(n - 2)

            # Store
            memo[n] = answer

            return answer

        return climb(n)