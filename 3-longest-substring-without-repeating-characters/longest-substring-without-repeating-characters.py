class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        low = 0
        high = 0
        #hashset 
        seen = set()
        while high < len(s):
            while s[high] in seen:
                seen.remove(s[low])
                low = low + 1
            seen.add(s[high])
            max_length = max(max_length,len(seen))
            high += 1
        return max_length
        