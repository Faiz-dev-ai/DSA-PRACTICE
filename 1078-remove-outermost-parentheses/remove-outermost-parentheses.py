class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        answer = []
        for ch in s:
            if ch == '(':
                if depth > 0:
                    answer.append("(")
                depth += 1
            elif ch == ')':
                if depth > 1:
                    answer.append(")")
                depth -= 1
        return "".join(answer)
        