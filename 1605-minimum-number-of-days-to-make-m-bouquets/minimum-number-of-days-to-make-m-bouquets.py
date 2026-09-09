class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)

        while low <= high:
            mid = (low + high) // 2

            streak = 0
            bouquets = 0

            for flower in bloomDay:
                if flower <= mid:
                    streak += 1

                    if streak == k:
                        bouquets += 1
                        streak = 0
                else:
                    streak = 0

            if bouquets < m:
                low = mid + 1
            else:
                high = mid - 1

        return low