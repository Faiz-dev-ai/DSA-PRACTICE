class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def power(x, n):
            # Base case
            if n == 0:
                return 1

            half = power(x, n // 2)

            if n % 2 == 0:
                return (half * half) % MOD
            else:
                return (x * half * half) % MOD

        count_4 = n // 2
        count_5 = n - (n // 2)

        return (power(5, count_5) * power(4, count_4)) % MOD