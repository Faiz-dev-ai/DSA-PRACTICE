class Solution:
    def generateBinaryStrings(self, n):
        answer = []

        def generate(current):

            # Base case
            if len(current) == n:
                answer.append(current)
                return

            # Starting state
            if current == "":
                generate(current + "0")
                generate(current + "1")

            # Previous bit is 0
            elif current[-1] == "0":
                generate(current + "0")
                generate(current + "1")

            # Previous bit is 1
            elif current[-1] == "1":
                generate(current + "0")

        generate("")
        return answer