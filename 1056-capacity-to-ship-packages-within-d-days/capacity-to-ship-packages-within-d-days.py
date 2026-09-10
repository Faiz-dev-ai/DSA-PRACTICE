class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        while(low<=high):
            mid = (low + high)//2
            current = 0
            days_used = 1
            for weight in weights:
                if current+weight<=mid:
                    current = current + weight
                else:
                    days_used += 1
                    current = weight
            if days_used > days:
                low = mid + 1
            else:
                high = mid - 1
        return low 
        