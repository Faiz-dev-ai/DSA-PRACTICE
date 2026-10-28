class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        answer = []
        seen = {}
        def generate(index,current):
            key = tuple(sorted(current))
            if index == len(nums):
                if key not in seen:
                    seen[key] = True
                    answer.append(current.copy())
                return
            #generating children
            #take
            current.append(nums[index])
            generate(index+1,current)
            current.pop()
            #dont take
            generate(index+1,current)
            return answer
        return generate(0,[])    #DUPLICATES GENERATED 
#OPTIMIZATION MUST BE DONE 

