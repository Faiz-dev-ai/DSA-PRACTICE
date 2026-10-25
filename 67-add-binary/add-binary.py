class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # a_bin = int(a,2)
        # b_bin = int(b,2)
        # total = a_bin + b_bin
        # return bin(total)[2:]      USING PYTHON
        
        #USING THE DSA METHOD 
        carry = 0
        i = len(a)-1
        j = len(b)-1
        result = ""
        while (i>=0 or j>=0 or carry):
            bit_a = int(a[i]) if i>=0 else 0
            bit_b = int(b[j]) if j>=0 else 0
            total = bit_a+bit_b+carry
            bit = total % 2
            i-=1
            j-=1
            carry = total//2
            result = str(bit) + result
        return result


