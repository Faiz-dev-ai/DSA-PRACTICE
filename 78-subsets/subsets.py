class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        answer = []
        def generate(index,current):
            if index == len(nums):#base case I have reached the final now i need to append this current in the answer
                answer.append(current.copy())
                return#It returns towhoever has called the function 
            #Dont take 
            generate(index+1,current)
            #Takes
            current.append(nums[index])
            generate(index+1,current)#now you've explored the branch so now go back to node where you split up 
            current.pop()
        generate(0,[])
        return answer
