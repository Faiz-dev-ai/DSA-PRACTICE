class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        n = len(s)
        sign = 1
        i = 0

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Handle sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Build number
        while i < n and s[i].isdigit():
            answer = (answer * 10) + int(s[i])
            i += 1

        answer = sign * answer

        INT_MAX = (2 ** 31) - 1
        INT_MIN = -(2 ** 31)

        if answer > INT_MAX:
            return INT_MAX
        elif answer < INT_MIN:
            return INT_MIN

        return answer               