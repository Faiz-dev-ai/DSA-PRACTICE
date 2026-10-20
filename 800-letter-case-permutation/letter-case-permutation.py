class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        answer = []
        def generate(index,current):
            #base case
            if index == len(s):
                answer.append(current)
                return
            if s[index].isdigit():
                generate(index+1,current+s[index])
            else:
                generate(index+1,current+(s[index].lower()))
                generate(index+1,current+(s[index].upper()))
        generate(0,"")
        return answer