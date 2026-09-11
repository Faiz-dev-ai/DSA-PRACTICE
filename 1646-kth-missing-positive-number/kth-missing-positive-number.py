class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low = 1
        high = len(arr)+k
        while(low <= high):
            mid = (low + high)//2
            missing_count = 0
            left = 0
            right = len(arr)-1
            while(left<=right):
                m = (left + right)//2
                if arr[m]<=mid:
                    left = m+1
                else:
                    right = m-1
            missing_count = mid - left
            if missing_count<k:
                low = mid + 1
            else:
                high = mid - 1
        return low
        