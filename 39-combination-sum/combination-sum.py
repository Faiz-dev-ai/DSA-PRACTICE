class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        answer = []

        def generate(index, current, total):

            # Base cases
            if total == target:
                answer.append(current.copy())
                return

            if total > target:
                return

            if index == len(candidates):
                return

            # TAKE
            current.append(candidates[index])
            generate(index, current, total + candidates[index])
            current.pop()

            # DON'T TAKE
            generate(index + 1, current, total)

        generate(0, [], 0)
        return answer