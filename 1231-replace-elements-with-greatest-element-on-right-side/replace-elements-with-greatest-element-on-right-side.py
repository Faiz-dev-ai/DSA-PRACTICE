class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = -1
        n = len(arr)
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = max_element
            if temp>max_element:
                max_element = temp 
        return arr
        