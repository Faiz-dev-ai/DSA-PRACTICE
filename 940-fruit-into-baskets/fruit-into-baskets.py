class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        seen = {}
        low = 0
        max_len = 0
        for high in range(len(fruits)):
            seen[fruits[high]] = seen.get(fruits[high],0)+1
            while len(seen)>2:
                seen[fruits[low]] -= 1
                if seen[fruits[low]] == 0:
                    del seen[fruits[low]]
                low += 1
            max_len = max(max_len,high - low + 1)
        return max_len