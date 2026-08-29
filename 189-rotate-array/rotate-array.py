class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k is larger than array size
        
        # Reusable Two-Pointer Mirror Function
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return nums
                
        # Step 1: Mirror Block A (0 to n - k - 1)
        reverse(0, n - k - 1)
        
        # Step 2: Mirror Block B (n - k to n - 1)
        reverse(n - k, n - 1)
        
        # Step 3: Mirror the whole world (0 to n - 1)
        reverse(0, n - 1)
