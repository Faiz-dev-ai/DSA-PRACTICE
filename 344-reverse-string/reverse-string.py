class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s)-1
        # while(left<right):
        #     s[left],s[right] = s[right],s[left]
        #     left += 1
        #     right -= 1
        # return s
        """USING RECURSION"""
        def reverse(left,right):
            if left >= right:
                return 
            s[left],s[right] = s[right],s[left]
            reverse(left + 1,right - 1)
        reverse(left,right)
        




        