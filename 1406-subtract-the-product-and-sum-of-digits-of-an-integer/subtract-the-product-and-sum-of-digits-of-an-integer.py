class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        addition = 0
        n = str(n)
        for num in n:
            #for products
            product *= int(num)
            addition += int(num)
        return product - addition
            

