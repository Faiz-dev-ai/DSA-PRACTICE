class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        answer = ""
        minimum = min(len(word) for word in strs)
        for i in range(minimum):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    return answer
            answer += strs[0][i]
        return answer
        
    