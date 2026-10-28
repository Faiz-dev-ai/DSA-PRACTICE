class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = []
        total = 0
        seen = {0:1}
        count = 0
        for i in range(len(nums)):
            total += nums[i]
            prefix.append(total)

        for i in range(len(prefix)):
            needed = prefix[i] - k
            if needed in seen:
                count += seen[needed]

            seen[prefix[i]] = seen.get(prefix[i],0)+1
        return count

