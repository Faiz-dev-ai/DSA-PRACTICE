class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer = []

        def isValid(current):
            steps = 0

            for ch in current:
                if ch == "(":
                    steps += 1
                else:
                    steps -= 1

                if steps < 0:
                    return False

            return steps == 0

        def generate(current):
            # Base case
            if len(current) == 2 * n:
                if isValid(current):
                    answer.append(current)
                return

            # Two choices
            generate(current + "(")
            generate(current + ")")

        generate("")

        return answer