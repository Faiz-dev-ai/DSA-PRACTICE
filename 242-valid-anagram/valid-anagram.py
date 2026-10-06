class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        for ch in s:
            map1[ch] = map1.get(ch,0)+1
        for ch in t:
            map2[ch] = map2.get(ch,0)+1
        if map1 == map2:
            return True
        else:
            return False        