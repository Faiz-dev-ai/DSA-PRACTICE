def Occurence(nums,target):
    first = last = -1
    low = 0
    high = len(nums)-1
    while(low<=high):
        mid = (low+high)//2
        if nums[mid]==target:
            first = mid
            high = mid -1
        elif nums[mid]>target:
            high = mid -1
        else:
            low = mid + 1
    low = 0 
    high = len(nums)-1
    while(low<=high):
        mid = (low + high)//2
        if nums[mid] == target:
            last = mid
            low = mid + 1
        elif nums[mid]<target:
            low = mid + 1
        else:
            high = mid - 1
    return [first,last]
nums = [1,2,3,5,5,6,7]
target = 5
print(Occurence(nums,target))