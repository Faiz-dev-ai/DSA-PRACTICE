class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maximum = 0
        
        for j in range(len(accounts)):
            total = 0
            for i in range(len(accounts[0])):
                total += accounts[j][i]
            if total > maximum:
                maximum = total
        return maximum
