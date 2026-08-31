class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = None
        cnt = 0
        for num in nums:
            if cnt == 0:#starting point
                el = num
                cnt = 1
            elif num == el:#if same teammate
                cnt += 1
            else:
                cnt -= 1#different teammate
        return el
        